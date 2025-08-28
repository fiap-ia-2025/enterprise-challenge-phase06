#include <OneWire.h>
#include <DallasTemperature.h>

// Pino GPIO onde o DS18B20 está conectado
#define one_wire_pino 4

// Configura uma instância da biblioteca OneWire
OneWire oneWire(one_wire_pino);

// Passa a referência OneWire para a biblioteca Dallas Temperature
DallasTemperature sensors(&oneWire);

// Variáveis para a contagem de medições
int contador = 0;
const int num_medicoes = 500;

// Variáveis para a classificação. 

const float TEMPERATURA_NORMAL_MIN = -1.0;
const float TEMPERATURA_NORMAL_MAX = 6.0;

const float TEMPERATURA_FALHA_CRITICA_MIN = -6.0;
const float TEMPERATURA_FALHA_CRITICA_MAX = 10.0;

void setup() {
  Serial.begin(115200);
  
  // Inicia a comunicação com o sensor
  sensors.begin();
  
   // Imprime o cabeçalho para o CSV
  Serial.println("ID, Temperatura, Status");
}

void loop() {
  // Verifica se o limite de medições foi alcançado
  if (contador < num_medicoes) {
    // Pede ao sensor para fazer a leitura da temperatura
    sensors.requestTemperatures(); 
    float temperatura = sensors.getTempCByIndex(0); // Lê a temperatura em Celsius do primeiro sensor

    // --- Classificação dos Resultados ---
    Serial.print(contador + 1);
    Serial.print(",");
    Serial.print(temperatura);
    Serial.print(",");
    
    if (temperatura >= TEMPERATURA_NORMAL_MIN && temperatura <= TEMPERATURA_NORMAL_MAX) {
      Serial.println("NORMAL");
    } else if (temperatura < TEMPERATURA_NORMAL_MIN || temperatura > TEMPERATURA_NORMAL_MAX) {
      
      if (temperatura >= TEMPERATURA_FALHA_CRITICA_MIN && temperatura <= TEMPERATURA_FALHA_CRITICA_MAX) {
         Serial.println("ALERTA_Pre_falha");
      } else {
         Serial.println("FALHA_CRITICA");
      }
    }
  
    contador++;
    
    delay(1000); 
  }
}