// ---- Para a medição de vibração com MPU5060 ----

#include <Wire.h>
#include <math.h>

// Endereço do MPU6050
const int MPU6050_ADDR = 0x68;

// Variáveis para armazenar os dados de aceleração
int16_t accX, accY, accZ;
double accTotal;

// Definição dos limites para classificação
const double LIMITE_ALERTA = 16500.0; 
const double LIMITE_FALHA = 25000.0;

// Variável para contar as medições
int contador = 0;
const int num_medicoes = 500;

void setup() {
  // inicia a comunicação serial para inserir os dados:
  Serial.begin(115200);
    // inicia a comunicação I2C
  Wire.begin();
  // inicia a comunicação com MPU6050
  Wire.beginTransmission(MPU6050_ADDR);
  Wire.write(0x6B); // Endereço do registro de gerenciamento de energia
  Wire.write(0);    // Desliga o modo de suspensão (sleep mode)
  Wire.endTransmission(true);
  
  Serial.println("MPU6050 iniciado com sucesso!");
  
  // Imprime o cabeçalho das colunas para o .csv
  Serial.println("ID,Aceleracao_Total,Status");
}


void loop() {
  if (contador < num_medicoes)
  // Solicita 6 bytes de dados do sensor
  Wire.beginTransmission(MPU6050_ADDR);
  Wire.write(0x3B); 
  Wire.endTransmission(false);
  Wire.requestFrom(MPU6050_ADDR, 6, true);
  
  // Lê e combina os bytes
  accX = Wire.read() << 8 | Wire.read();
  accY = Wire.read() << 8 | Wire.read();
  accZ = Wire.read() << 8 | Wire.read();
  
  // Calcula a aceleração total (vetor soma)
  // Usamos o teorema de Pitágoras em 3D para isso
  accTotal = sqrt(pow(accX, 2) + pow(accY, 2) + pow(accZ, 2));

  // --- Classificação dos Resultados ---
    Serial.print(contador + 1);
    Serial.print(",");
    Serial.print(accTotal);
    Serial.print(",");


  if (accTotal < LIMITE_ALERTA) {
    Serial.println("NORMAL");
  } else if (accTotal < LIMITE_FALHA) {
    Serial.println("ALERTA_Pre_falha");
  } else {
    Serial.println("FALHA_CRITICA");
  }

    contador++;

    delay(1000);
}

// ---- Para a medição de vibração com DS18B20 ----

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