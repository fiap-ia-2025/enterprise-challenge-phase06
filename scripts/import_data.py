# Arquivo: scripts/import_data.py (versão ajustada e robusta)

import sqlite3
import pandas as pd
import os

# --- CAMINHOS DINÂMICOS ---
# Obtém o caminho absoluto do diretório onde o script está (a pasta /scripts)
script_dir = os.path.dirname(os.path.abspath(__file__))
# Obtém o caminho do diretório raiz do projeto (um nível acima da pasta /scripts)
project_dir = os.path.dirname(script_dir)

# Constrói os caminhos para os arquivos necessários a partir da raiz do projeto
db_path = os.path.join(project_dir, 'data', 'hermes_db.sqlite')
schema_path = os.path.join(project_dir, '.sql', 'schema.sql')
nivel_csv_path = os.path.join(project_dir, 'data', 'medicao_nivel.csv')
temp_csv_path = os.path.join(project_dir, 'data', 'medicao_temperatura.csv')
vibracao_csv_path = os.path.join(project_dir, 'data', 'medicao_vibracao.csv')


# Conecta ao banco de dados (ou cria se não existir no caminho especificado)
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# 1. Executa o script para criar as tabelas
print("Criando o schema do banco de dados...")
with open(schema_path, 'r') as f:
    schema_script = f.read()
cursor.executescript(schema_script)
print("Schema criado com sucesso.")

# 2. Insere os dados fixos (Máquinas e Sensores)
print("Inserindo dados em MAQUINAS e SENSORES...")
cursor.execute("INSERT INTO MAQUINAS (id_maquina, nome, localizacao) VALUES (1, 'enchedora', 'area_envase_1');")
cursor.execute("INSERT INTO MAQUINAS (id_maquina, nome, localizacao) VALUES (2, 'pasteurizadora', 'area_pasteurizacao');")
cursor.execute("INSERT INTO MAQUINAS (id_maquina, nome, localizacao) VALUES (3, 'lavadora_e_sopradora', 'area_envase_3');")

cursor.execute("INSERT INTO SENSORES (id_sensor, id_maquina, tipologia) VALUES (1, 1, 'nivel_enchimento');")
cursor.execute("INSERT INTO SENSORES (id_sensor, id_maquina, tipologia) VALUES (2, 2, 'temperatura');")
cursor.execute("INSERT INTO SENSORES (id_sensor, id_maquina, tipologia) VALUES (3, 3, 'vibracao');")
print("Dados inseridos.")

# 3. Importa os dados dos CSVs para as tabelas de medição
print("Importando dados dos CSVs...")

# Importar medições de nível
df_nivel = pd.read_csv(nivel_csv_path)
df_nivel['id_sensor'] = 1 # Associar ao sensor de nível
df_nivel = df_nivel.rename(columns={'ID': 'id', 'Distancia_cm': 'distancia_cm', 'Nivel_cm': 'nivel_cm', 'Status': 'status'})
df_nivel[['id', 'id_sensor', 'distancia_cm', 'nivel_cm', 'status']].to_sql('MEDICAO_NIVEL', conn, if_exists='append', index=False)

# Importar medições de temperatura
df_temp = pd.read_csv(temp_csv_path)
df_temp['id_sensor'] = 2 # Associar ao sensor de temperatura
df_temp.columns = df_temp.columns.str.strip()
df_temp = df_temp.rename(columns={'ID': 'id', 'Temperatura': 'medicao', 'Status': 'status'})
df_temp[['id', 'id_sensor', 'medicao', 'status']].to_sql('MEDICAO_TEMPERATURA', conn, if_exists='append', index=False)

# Importar medições de vibração
df_vibracao = pd.read_csv(vibracao_csv_path)
df_vibracao['id_sensor'] = 3 # Associar ao sensor de vibração
df_vibracao = df_vibracao.rename(columns={'ID': 'id', 'Aceleracao_Total': 'aceleracao_total', 'Status': 'status'})
df_vibracao[['id', 'id_sensor', 'aceleracao_total', 'status']].to_sql('MEDICAO_VIBRACAO', conn, if_exists='append', index=False)

print("Importação dos CSVs concluída.")

# Salva as alterações e fecha a conexão
conn.commit()
conn.close()

print(f"Banco de dados '{db_path}' criado e populado com sucesso!")