#include <Servo.h>

Servo servos[5];
// Pinos PWM onde os 5 servos serão conectados:
// 0: Polegar (pino 3), 1: Indicador (pino 5), 2: Médio (pino 6), 3: Anelar (pino 9), 4: Mínimo (pino 10)
const int pinos[5] = {3, 5, 6, 9, 10};

void setup() {
  Serial.begin(115200);
  for (int i = 0; i < 5; i++) {
    servos[i].attach(pinos[i]);
    servos[i].write(0); // Inicia com a mão aberta
  }
}

void loop() {
  if (Serial.available() > 0) {
    String linha = Serial.readStringUntil('\n');
    linha.trim();

    int d[5];
    // Lê o formato: d0,d1,d2,d3,d4 (ex: 1,1,1,1,1 ou 180,0,0,180,180)
    if (sscanf(linha.c_str(), "%d,%d,%d,%d,%d", &d[0], &d[1], &d[2], &d[3], &d[4]) == 5) {
      for (int i = 0; i < 5; i++) {
        // Se você mandar 0 ou 1: converte para 0° ou 180°
        int angulo = (d[i] <= 1) ? (d[i] * 180) : constrain(d[i], 0, 180);
        servos[i].write(angulo);
      }
    }
  }
}