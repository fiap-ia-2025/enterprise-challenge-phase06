CREATE TABLE SENSORES (
  id_sensor INT PRIMARY KEY,
  id_maquina INT,
  tipologia VARCHAR(30),
  FOREIGN KEY (id_maquina) REFERENCES MAQUINAS(id_maquina)
  );

insert into SENSORES (id_sensor, id_maquina, tipologia)
VALUES
(1, 1, 'nivel_enchimento'),
(2, 2, 'temperatura'),
(3, 3, 'vibracao');

SELECT * FROM SENSORES;
