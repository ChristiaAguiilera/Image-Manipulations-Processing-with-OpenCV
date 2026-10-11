# 📡 Reto IoT: Alarma de Proximidad con ESP32

## 📌 Introducción al Reto
Este proyecto es un pequeño ejemplo práctico de Internet de las Cosas (IoT) enfocado en la interacción entre hardware y el entorno físico. El objetivo del reto es utilizar un **ESP32** junto con un **Sensor Ultrasónico (HC-SR04)** para medir distancias en tiempo real. 

El sistema incluye una alerta acústica: a medida que un objeto se acerca al sensor y cruza un umbral de distancia mínimo, se activará un **buzzer** emitiendo un sonido de advertencia y se mostrará una alerta en el monitor serie.

---

## 🛠️ Materiales Necesarios
* 1x Microcontrolador ESP32.
* 1x Sensor Ultrasónico HC-SR04.
* 1x Buzzer (Zumbador) activo o pasivo.
* Protoboard y cables jumper.
* Entorno de desarrollo (Arduino IDE).

---

## 🚀 Paso a Paso del Reto

### 1. Conexiones de Hardware (Wiring)
Realiza las conexiones en tu protoboard siguiendo este esquema:

| Componente | Pin del Componente | Pin en el ESP32 |
| :--- | :--- | :--- |
| **Sensor HC-SR04** | VCC | VIN o 5V |
| | GND | GND |
| | TRIG | GPIO 5 |
| | ECHO | GPIO 18 |
| **Buzzer** | Positivo (+) | GPIO 19 |
| | Negativo (-) | GND |

### 2. Configuración del Entorno
1. Abre **Arduino IDE**.
2. Asegúrate de tener instaladas las tarjetas ESP32 (`Herramientas > Placa > Gestor de tarjetas`).
3. Selecciona tu modelo de ESP32 y el puerto COM correcto.

### 3. Código del Proyecto
Copia y pega el siguiente código en tu Arduino IDE. Este script se encarga de emitir el pulso, calcular la distancia y activar el buzzer si el objeto está a menos de 15 cm.

```cpp
// Definición de pines
const int pinTrig = 5;
const int pinEcho = 18;
const int pinBuzzer = 19;

// Distancia de alerta en centímetros
const int distanciaAlerta = 15; 

long duracion;
float distancia;

void setup() {
  Serial.begin(115200);
  
  pinMode(pinTrig, OUTPUT);
  pinMode(pinEcho, INPUT);
  pinMode(pinBuzzer, OUTPUT);
  
  // Aseguramos que el buzzer inicie apagado
  digitalWrite(pinBuzzer, LOW);
}

void loop() {
  // Generación del pulso ultrasónico
  digitalWrite(pinTrig, LOW);
  delayMicroseconds(2);
  digitalWrite(pinTrig, HIGH);
  delayMicroseconds(10);
  digitalWrite(pinTrig, LOW);
  
  // Lectura del eco y cálculo de distancia
  duracion = pulseIn(pinEcho, HIGH);
  distancia = duracion * 0.034 / 2;
  
  // Mostrar en el Monitor Serie
  Serial.print("Distancia: ");
  Serial.print(distancia);
  Serial.println(" cm");
  
  // Lógica de la alarma
  if (distancia > 0 && distancia <= distanciaAlerta) {
    Serial.println("¡ALERTA! Objeto muy cerca.");
    digitalWrite(pinBuzzer, HIGH); // Enciende el buzzer
  } else {
    digitalWrite(pinBuzzer, LOW);  // Apaga el buzzer
  }
  
  delay(200); // Pequeña pausa antes de la siguiente medición
}
