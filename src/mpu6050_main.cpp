#include <Arduino.h>

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

  // Incrementa o contador
  contador++;

  // Pequeno atraso
  delay(1000);
}
