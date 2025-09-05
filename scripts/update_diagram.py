# Importa as variáveis de ambiente de compilação do PlatformIO
Import("env") # type: ignore

import os
import shutil

# Pega o nome do ambiente diretamente do PlatformIO, de forma confiável
# A variável 'env' é injetada pelo PlatformIO quando o script é executado
try:
    env_name = env.subst("$PIOENV") # type: ignore
except NameError:
    env_name = os.environ.get('PIOENV')


# Mapeamento dos nomes dos ambientes para os nomes dos arquivos JSON
json_map = {
    'sensor_temperatura_ds18b20': 'diagram_DS18B20.json',
    'sensor_nivel_hcsr04': 'diagram_HC-SR04.json',
    'sensor_vibracao_mpu6050': 'diagram_MPU6050.json'
}

# O resto da lógica permanece o mesmo
if env_name and env_name in json_map:
    # Define o caminho do arquivo de origem (ex: .json/diagram_DS18B20.json)
    source_json_name = json_map[env_name]
    source_path = os.path.join('.json', source_json_name)

    # Define o caminho do arquivo de destino (o diagram.json na raiz)
    destination_path = 'diagram.json'

    if os.path.exists(source_path):
        shutil.copy(source_path, destination_path)
        print(f"--- SUCESSO: Diagrama do Wokwi atualizado para o ambiente '{env_name}' ---")
    else:
        print(f"--- ERRO: Arquivo de origem não encontrado em '{source_path}' ---")
else:
    print(f"--- AVISO: Nenhum mapeamento de diagrama para o ambiente '{env_name}'. Pulando atualização. ---")