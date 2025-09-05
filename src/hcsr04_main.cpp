#include <Arduino.h>
// Pinos do HC-SR04
#define TRIG_PIN 13
#define ECHO_PIN 12

// Constantes e variáveis para a medição
const float VELOCIDADE_SOM = 0.0343; // cm/microsegundo
long duracao;
float distancia_cm;

// Limites da classificação 
// Altura total do recipiente
const float ALTURA_MAXIMA = 20.0;
// Nível de enchimento considerado normal
const float NIVEL_NORMAL_MIN = 19.0;
const float NIVEL_NORMAL_MAX = 20.0;
// Nível de alerta
const float NIVEL_ALERTA_MIN = 0.0;
const float NIVEL_ALERTA_MAX = 18.0;

// Variáveis para a contagem de medições
int contador = 0;
const int num_medicoes = 500;

void setup() {
  Serial.begin(115200);

  // Define os pinos do sensor como entrada e saída
  pinMode(TRIG_PIN, OUTPUT);
  pinMode(ECHO_PIN, INPUT);

  // Imprime o cabeçalho para o CSV
  Serial.println("ID,Distancia_cm,Nivel_cm,Status");
}

void loop() {
  if (contador < num_medicoes) {
    // Limpa o pino TRIG
    digitalWrite(TRIG_PIN, LOW);
    delayMicroseconds(2);

    // Dispara o pulso no pino TRIG por 10 microssegundos
    digitalWrite(TRIG_PIN, HIGH);
    delayMicroseconds(10);
    digitalWrite(TRIG_PIN, LOW);

    // Lê a duração do pulso no pino ECHO
    duracao = pulseIn(ECHO_PIN, HIGH);

    // Calcula a distância em cm (tempo * velocidade do som / 2)
    distancia_cm = duracao * VELOCIDADE_SOM / 2;

    // Calcula o nível de enchimento (altura total - distância medida)
    float nivel_cm = ALTURA_MAXIMA - distancia_cm;

    // --- Classificação dos Resultados ---
    Serial.print(contador + 1);
    Serial.print(",");
    Serial.print(distancia_cm);
    Serial.print(",");
    Serial.print(nivel_cm);
    Serial.print(",");
    
    if (nivel_cm >= NIVEL_NORMAL_MIN && nivel_cm <= NIVEL_NORMAL_MAX) {
      Serial.println("NORMAL");
    } else if (nivel_cm >= NIVEL_ALERTA_MIN && nivel_cm < NIVEL_NORMAL_MIN) {
      Serial.println("ALERTA_Pre_falha");
    } else {
      Serial.println("FALHA_CRITICA");
    }

    contador++;
    
    delay(1000);
  }
}