import cv2
import time
import math
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

# ==========================================
# CONFIGURAÇÃO DE COMUNICAÇÃO ARDUINO / MOCK
# ==========================================
USE_MOCK = True       # True = Teste na tela | False = Envia para o Arduino
PORTA_SERIAL = 'COM3' # Ajuste a porta se conectar o Arduino
BAUD_RATE = 115200

ser = None
if not USE_MOCK:
    try:
        import serial
        ser = serial.Serial(PORTA_SERIAL, BAUD_RATE, timeout=0.1)
        time.sleep(2)
        print(f"Conectado ao Arduino na porta {PORTA_SERIAL}")
    except Exception as e:
        print(f"Erro ao conectar na serial: {e}. Mudando para modo MOCK.")
        USE_MOCK = True

# Conexões das 21 landmarks da mão
HAND_CONNECTIONS = [
    (0, 1), (1, 2), (2, 3), (3, 4),        # Polegar
    (0, 5), (5, 6), (6, 7), (7, 8),        # Indicador
    (5, 9), (9, 10), (10, 11), (11, 12),   # Médio
    (9, 13), (13, 14), (14, 15), (15, 16), # Anelar
    (13, 17), (17, 18), (18, 19), (19, 20),# Mínimo
    (0, 17)                                # Base
]

base_options = python.BaseOptions(model_asset_path="hand_landmarker.task")
options = vision.HandLandmarkerOptions(
    base_options=base_options,
    running_mode=vision.RunningMode.VIDEO,
    num_hands=1,
    min_hand_detection_confidence=0.5,
    min_hand_presence_confidence=0.5,
    min_tracking_confidence=0.5
)

def calcular_dedos_levantados(pontos):
    """
    Retorna uma lista de 5 valores [Polegar, Indicador, Médio, Anelar, Mínimo]
    1 = aberto / levantado, 0 = fechado / dobrado
    """
    dedos = []

    
    dist_ponta = math.hypot(pontos[4][0] - pontos[17][0], pontos[4][1] - pontos[17][1])
    dist_base = math.hypot(pontos[3][0] - pontos[17][0], pontos[3][1] - pontos[17][1])
    dedos.append(1 if dist_ponta > dist_base else 0)

    
    pontas = [8, 12, 16, 20]
    articulacoes = [6, 10, 14, 18]

    for p, a in zip(pontas, articulacoes):
        dedos.append(1 if pontos[p][1] < pontos[a][1] else 0)

    return dedos

cap = cv2.VideoCapture(0)

with vision.HandLandmarker.create_from_options(options) as detector:
    while cap.isOpened():
        sucesso, frame = cap.read()
        if not sucesso:
            print("Não foi possível acessar a câmera.")
            break

        frame = cv2.flip(frame, 1)
        h, w, _ = frame.shape

        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb_frame)
        timestamp_ms = int(time.time() * 1000)

        resultado = detector.detect_for_video(mp_image, timestamp_ms)

        if resultado.hand_landmarks:
            for hand_landmarks in resultado.hand_landmarks:
                pontos = [(int(lm.x * w), int(lm.y * h)) for lm in hand_landmarks]

                
                for inicio, fim in HAND_CONNECTIONS:
                    cv2.line(frame, pontos[inicio], pontos[fim], (0, 255, 0), 2)
                for cx, cy in pontos:
                    cv2.circle(frame, (cx, cy), 5, (0, 0, 255), -1)

                
                estado_dedos = calcular_dedos_levantados(pontos)
                msg = f"Dedos: {estado_dedos}"
                cv2.putText(frame, msg, (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)

                
                if not USE_MOCK and ser and ser.is_open:
                    dados = f"{','.join(map(str, estado_dedos))}\n"
                    ser.write(dados.encode())

        cv2.imshow("Mao Robotica - Rastreamento", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
if ser and ser.is_open:
    ser.close()
cv2.destroyAllWindows()