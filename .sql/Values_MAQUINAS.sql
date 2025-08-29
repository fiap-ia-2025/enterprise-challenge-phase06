CREATE TABLE MAQUINAS (
  id_maquina int PRIMARY KEY,
  nome varchar(20),
  localizacao varchar(20)
);

INSERT INTO MAQUINAS (id_maquina, nome, localizacao)
VALUES 
  (1, 'enchedora', 'area_envase_1'),
  (2, 'pasteurizadora', 'area_pasteurizacao'),
  (3, 'lavadora_e_sopradora_de_garrafas', 'area_envase_3');
  
SELECT * FROM MAQUINAS 