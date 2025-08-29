SELECT * FROM MEDICAO_NIVEL;

ALTER TABLE MEDICAO_NIVEL ADD COLUMN id_sensor INTEGER;

UPDATE MEDICAO_NIVEL SET id_sensor = 1;

ALTER TABLE MEDICAO_NIVEL RENAME TO MEDICAO_NIVEL_OLD;

CREATE TABLE MEDICAO_NIVEL (
  id INT PRIMARY KEY, 
  id_sensor INT, 
  distancia_cm FLOAT, 
  nivel_cm FLOAT, 
  status VARCHAR(20),
  foreign key (id_sensor) REFERENCES SENSORES(id_sensor)
  );
  
INSERT INTO MEDICAO_NIVEL (id, id_sensor, distancia_cm, nivel_cm, status)
SELECT ID, id_sensor, Distancia_cm, Nivel_cm, Status
FROM MEDICAO_NIVEL_OLD;

DROP TABLE MEDICAO_NIVEL_OLD;