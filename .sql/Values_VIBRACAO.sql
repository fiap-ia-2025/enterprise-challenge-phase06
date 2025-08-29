SELECT * FROM medicao_vibracao;

ALTER TABLE medicao_vibracao ADD COLUMN id_sensor;

UPDATE medicao_vibracao SET id_sensor = 3;

ALTER TABLE medicao_vibracao RENAME TO medicao_vibracao_old;

CREATE TABLE MEDICAO_VIBRACAO (
  id INT PRIMARY KEY,
  id_sensor INT,
  aceleracao_total FLOAT,
  status VARCHAR(20),
  FOREIGN KEY (id_sensor) REFERENCES SENSORES(id_sensor)
  );
 
 INSERT INTO MEDICAO_VIBRACAO (id, id_sensor, aceleracao_total, status)
 SELECT ID, id_sensor, Aceleracao_Total, Status
 FROM medicao_vibracao_old;
 
 DROP TABLE medicao_vibracao_old;
 

  