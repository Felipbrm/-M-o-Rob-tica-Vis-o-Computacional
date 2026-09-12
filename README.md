# 🤖 Mão Robótica — Visão Computacional

Projeto de uma mão robótica controlada por movimentos da mão humana utilizando **Python, OpenCV, MediaPipe e Arduino**.

O sistema utiliza a câmera do computador para identificar a mão do usuário e detectar o estado de cada dedo em tempo real. As informações identificadas podem ser enviadas para um Arduino, que será responsável pelo controle dos servomotores da mão robótica.

## 🎯 Objetivo

Desenvolver um sistema capaz de reconhecer movimentos da mão humana e reproduzi-los em uma mão robótica.

O projeto tem como objetivo estudar e integrar conceitos de:

* Visão computacional
* Inteligência artificial
* Reconhecimento de gestos
* Programação em Python
* Comunicação serial
* Arduino
* Robótica
* Servomotores

## 🧠 Como funciona

O funcionamento do projeto segue o seguinte fluxo:

```text
Mão humana
     ↓
Webcam
     ↓
OpenCV
     ↓
MediaPipe
     ↓
21 pontos da mão
     ↓
Identificação dos dedos
     ↓
Estado dos dedos [0/1]
     ↓
Comunicação Serial
     ↓
Arduino
     ↓
Servomotores
     ↓
Mão robótica
```

O sistema identifica cinco dedos:

| Dedo         | Valor  |
| ------------ | ------ |
| 👍 Polegar   | 0 ou 1 |
| ☝️ Indicador | 0 ou 1 |
| 🖕 Médio     | 0 ou 1 |
| 💍 Anelar    | 0 ou 1 |
| 🤏 Mínimo    | 0 ou 1 |

Onde:

```text
1 = dedo levantado
0 = dedo fechado
```

Por exemplo:

```text
[1, 1, 1, 1, 1]
```

representa uma mão aberta.

Enquanto:

```text
[0, 0, 0, 0, 0]
```

representa uma mão fechada.

## 🛠️ Tecnologias utilizadas

* 🐍 Python
* 👁️ OpenCV
* 🖐️ MediaPipe
* 🔌 Arduino
* ⚙️ Servomotores
* 📡 Comunicação Serial
* 📷 Webcam

## 📂 Estrutura do projeto

```text
mao-robotica/
│
├── python/
│   ├── main.py
│   └── hand_landmarker.task
│
├── arduino/
│   └── mao_robotica.ino
│
├── simulacao/
│   └── index.html
│
├── README.md
└── requirements.txt
```

## 📦 Instalação

Primeiro, instale as bibliotecas necessárias:

```bash
pip install opencv-python mediapipe pyserial
```

Depois, coloque o arquivo:

```text
hand_landmarker.task
```

na pasta do código Python.

## ▶️ Executando

Execute:

```bash
python main.py
```

A webcam será aberta e o sistema começará a identificar a mão.

Durante o funcionamento, os 21 pontos da mão serão exibidos na tela.

Pressione:

```text
Q
```

para encerrar o programa.

## 🔌 Comunicação com Arduino

O projeto possui dois modos:

```python
USE_MOCK = True
```

### Modo de teste

Quando:

```python
USE_MOCK = True
```

o programa funciona somente no computador, permitindo testar o reconhecimento da mão sem precisar conectar o Arduino.

### Modo Arduino

Quando:

```python
USE_MOCK = False
```

o Python tenta estabelecer uma comunicação serial com o Arduino.

A porta pode ser configurada em:

```python
PORTA_SERIAL = "COM3"
```

E a velocidade:

```python
BAUD_RATE = 115200
```

## 🚀 Próximas etapas

* [ ] Criar controle individual dos cinco servomotores
* [ ] Integrar Python com Arduino
* [ ] Sincronizar os movimentos da mão humana com a mão robótica
* [ ] Melhorar a identificação dos dedos
* [ ] Criar diferentes gestos
* [ ] Criar uma simulação 3D da mão robótica
* [ ] Adicionar interface gráfica
* [ ] Melhorar estabilidade e precisão do rastreamento
* [ ] Documentar a montagem física da mão

## 📚 Aprendizado

Este projeto está sendo desenvolvido como um projeto de estudo para aprofundar conhecimentos em **Engenharia de Software, Python, visão computacional, inteligência artificial, Arduino e robótica**.

## 👨‍💻 Autor

**Felipe Ribeiro**

Estudante de Engenharia de Software e desenvolvedor em formação.

---

⭐ Projeto desenvolvido para fins de estudo e experimentação em robótica e visão computacional.
