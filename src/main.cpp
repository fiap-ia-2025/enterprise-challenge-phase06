#include <Adafruit_Sensor.h>
#include <DHT.h>

#define DHTPIN 6       // Pino conectado ao sensor
#define DHTTYPE DHT22   // Modelo do sensor: DHT22

DHT dht(DHTPIN, DHTTYPE);  // Instancia o sensor

void setup() {
  Serial.begin(115200);
  Serial.println("Tempo_ms,Temperatura_C,Status");
  dht.begin();  // Inicializa o sensor
}

float simularTemperatura(unsigned long tempo_ms) {
  if (tempo_ms < 5000) {
    return 5.0 + random(0, 40) / 10.0;
  } else if (tempo_ms < 10000) {
    return 9.1 + random(0, 28) / 10.0;
  } else {
    return 12.0 + random(0, 30) / 10.0;
  }
}

String classificarStatus(float temperatura) {
  if (temperatura <= 9.0) {
    return "NORMAL";
  } else if (temperatura <= 11.9) {
    return "ALERTA_Pre_falha";
  } else {
    return "FALHA_CRITICA";
  }
}

void loop() {
  unsigned long tempo_atual = millis();

  float tempSimulada = simularTemperatura(tempo_atual);
  String status = classificarStatus(tempSimulada);

  
  Serial.print(tempo_atual);
  Serial.print(",");
  Serial.print(tempSimulada, 1);
  Serial.print(",");
  Serial.println(status);

  delay(1000);
}

