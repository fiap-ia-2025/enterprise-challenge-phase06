-- Deleta as tabelas se elas já existirem, para garantir que o script possa ser rodado várias vezes
DROP TABLE IF EXISTS MEDICAO_NIVEL;
DROP TABLE IF EXISTS MEDICAO_TEMPERATURA;
DROP TABLE IF EXISTS MEDICAO_VIBRACAO;
DROP TABLE IF EXISTS SENSORES;
DROP TABLE IF EXISTS MAQUINAS;

-- Cria a tabela de Máquinas
CREATE TABLE MAQUINAS (
  id_maquina INTEGER PRIMARY KEY,
  nome VARCHAR(30),
  localizacao VARCHAR(30)
);

-- Cria a tabela de Sensores
CREATE TABLE SENSORES (
  id_sensor INTEGER PRIMARY KEY,
  id_maquina INTEGER,
  tipologia VARCHAR(30),
  FOREIGN KEY (id_maquina) REFERENCES MAQUINAS(id_maquina)
);

-- Cria a tabela de Medição de Nível
CREATE TABLE MEDICAO_NIVEL (
  id INTEGER PRIMARY KEY,
  id_sensor INTEGER,
  distancia_cm REAL,
  nivel_cm REAL,
  status VARCHAR(20),
  FOREIGN KEY (id_sensor) REFERENCES SENSORES(id_sensor)
);

-- Cria a tabela de Medição de Temperatura
CREATE TABLE MEDICAO_TEMPERATURA (
  id INTEGER PRIMARY KEY,
  id_sensor INTEGER,
  medicao REAL,
  status VARCHAR(20),
  FOREIGN KEY (id_sensor) REFERENCES SENSORES(id_sensor)
);

-- Cria a tabela de Medição de Vibração
CREATE TABLE MEDICAO_VIBRACAO (
  id INTEGER PRIMARY KEY,
  id_sensor INTEGER,
  aceleracao_total REAL,
  status VARCHAR(20),
  FOREIGN KEY (id_sensor) REFERENCES SENSORES(id_sensor)
);