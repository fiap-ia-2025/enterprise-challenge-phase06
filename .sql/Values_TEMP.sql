SELECT * FROM medicao_temperatura;

ALTER TABLE medicao_temperatura ADD COLUMN id_sensor;

UPDATE medicao_temperatura SET id_sensor = 2;

ALTER TABLE medicao_temperatura RENAME TO medicao_temperatura_old;

CREATE TABLE MEDICAO_TEMPERATURA (
  id INT PRIMARY KEY,
  id_sensor INT,
  medicao FLOAT,
  status VARCHAR(20),
  FOREIGN KEY (id_sensor) REFERENCES SENSORES(id_sensor)  
  );
  
INSERT INTO MEDICAO_TEMPERATURA (id, id_sensor, medicao, status)
SELECT ID, id_sensor, _Temperatura, _Status
FROM medicao_temperatura_old;

DROP TABLE medicao_temperatura_old;