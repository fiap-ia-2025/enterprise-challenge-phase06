# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
  <a href="https://www.fiap.com.br/">
    <img src="img/logo-fiap.png" alt="FIAP - Faculdade de Informática e Administração Paulista" border="0" width="40%" height="40%">
  </a>
</p>

---

# 📦 Enterprise Challenge - Sprint 3


## 👥 Grupo 26


## 👨‍🎓 Integrantes:
- Amanda Vieira Pires (RM5666330)
- Ana Gabriela Soares Santos (RM565235)
- Bianca Nascimento de Santa Cruz Oliveira (RM561390)
- Milena Pereira dos Santos Silva (RM565464)
- Nayana Mehta Miazaki (RM565045) 

## 👩‍🏫 Professores:
### Tutor(a)  
-  Lucas Gomes Moreira
### Coordenador(a)  
- André Godoi

---

# 📜 Descrição do Projeto
## 🚀 Introdução

Dando continuidade ao projeto de manutenção preditiva em linhas de envase, esta fase avança da simulação de sensores para a estruturação e análise de dados. Transformamos os dados coletados em um banco de dados relacional robusto e, a partir dele, desenvolvemos um modelo de Machine Learning para extrair insights valiosos. Esta etapa representa um ciclo completo de uma solução de digitalização industrial, conectando a coleta de dados, o armazenamento estruturado e a aplicação de inteligência preditiva.


Link do repositório Sprint 1: https://github.com/fiap-ia-2025/enterprise-challenge-phase03

---

## 🎯 Objetivo

- **Modelar um banco de dados relacional** funcional e normalizado para os dados dos sensores.
- **Criar um script SQL (`schema.sql`)** para definir a estrutura do banco.
- **Desenvolver um script Python (`import_data.py`)** para automatizar a criação e o povoamento do banco de dados a partir dos arquivos CSV.
- **Treinar um algoritmo de Machine Learning** para classificar o status operacional (`NORMAL`, `ALERTA_Pre_falha`, `FALHA_CRITICA`).
- **Gerar e justificar visualizações** que demonstrem a performance do modelo.
- **Documentar todo o processo** no GitHub, garantindo clareza e reprodutibilidade.

---

## 🔧 Pipeline de Solução e Execução

O projeto foi estruturado como um pipeline de dados semi-automatizado, garantindo um fluxo de trabalho eficiente desde a simulação até a análise preditiva.

- **Simulação de Sensores (Wokwi + PlatformIO):** O projeto utiliza múltiplos ambientes no PlatformIO, um para cada sensor (DS18B20, MPU6050, HC-SR04). Ao selecionar e compilar um ambiente, um script de pré-compilação (`update_diagram.py`) atualiza automaticamente o arquivo `diagram.json`, garantindo que o Wokwi sempre carregue o circuito correto para a simulação.
- **Coleta de Dados (Manual):** Os dados gerados no monitor serial do Wokwi são coletados e salvos nos respectivos arquivos `.csv` na pasta `data/`.
- **Estruturação de Dados (SQLite):** Um script Python (`import_data.py`) lê os arquivos `.csv`, cria um banco de dados SQLite com base em um esquema pré-definido (`schema.sql`) e popula as tabelas.
- **Machine Learning (Jupyter Notebook):** O notebook (`machine_learning.ipynb`) conecta-se ao banco de dados para treinar, testar e avaliar um modelo de classificação com `Scikit-learn`.

---

## 🚀 Como Executar o Projeto

### 📋 Pré-requisitos

- Python 3.8+
- Visual Studio Code com as extensões:
  - PlatformIO IDE: Essencial para compilar e simular o código do ESP32.
  - Wokwi for VS Code: Necessária para rodar a simulação dos circuitos.
  - Jupyter: Para executar os notebooks de análise.
  - SQLite Viewer: (Opcional) Para inspecionar o banco de dados.



### Passo a Passo
O processo completo é dividido em 3 fases principais: gerar os dados, estruturá-los no banco de dados e, finalmente, treinar o modelo de Machine Learning.

## 🔹 Fase 1: Geração de Dados Simulados (Wokwi)

Existem duas maneiras de gerar os dados. Escolha a que melhor se adapta à sua necessidade.

---

1. **Escolha o ambiente do sensor**  
   - Clique no ícone do PlatformIO (formiga) na barra lateral esquerda do VS Code.
   - Em PROJECT TASKS, expanda a lista e escolha o ambiente do sensor que deseja simular (ex: `sensor_nivel_hcsr04`).

2. **Compile o Código (Build):**  
   - Clique na opção Build dentro do ambiente escolhido. 
   - Aguarde a mensagem de SUCCESS no terminal. Esse processo também executa o script `update_diagram.py`, que atualiza o arquivo `diagram.json` com o circuito correto.

3. **Ajuste o `wokwi.toml`**  
   - Abra o arquivo `wokwi.toml` na raiz do projeto.
   - Altere a linha firmware para apontar para o arquivo `.elf` do sensor que você acabou de compilar. O caminho correto será exibido no terminal após o build.
     - Exemplo para o sensor de nível:
       
     ```toml
     firmware = ".pio/build/sensor_nivel_hcsr04/firmware.elf"
     ```

4. **Inicie a Simulação**  
   - Pressione F1 para abrir a paleta de comandos do VS Code. 
   - Digite e selecione Wokwi: Start Simulator.
   - A simulação iniciará em uma nova aba. Copie os dados gerados no Serial Monitor e salve-os no arquivo `.csv` correspondente dentro da pasta `data/`.

5. **Repita para os Outros Sensores**  
   - Para gerar os dados dos outros sensores, repita os passos de 1 a 4, selecionando o ambiente e atualizando o `wokwi.toml` para cada um.

---

## 🔹 Fase 2: Estruturação dos Dados

  1. Instale as dependências Python:
  ```bash
    pip install pandas scikit-learn matplotlib seaborn
  ```

  2. Execute o script de importação para criar e popular o banco de dados `hermes_db.sqlite` e populá-lo com os dados dos arquivos CSV:
  ```bash
    python scripts/import_data.py
  ```

## 🔹 Fase 3: Análise com Machine Learning

  1. (Opcional) Análise Exploratória:
       - Abra o notebook `notebooks/grafico.ipynb`.
       - Execute as células para gerar gráficos individuais para cada tipo de sensor, permitindo uma visualização inicial dos dados coletados.
         
  2. Clique em "Executar Tudo" (Run All). O notebook irá treinar o modelo e exibir a Matriz de Confusão com os resultados.
       - Abra o notebook principal `notebooks/machine_learning.ipynb`.
       - Clique em **"Executar Tudo" (Run All)**. O notebook irá carregar os dados do banco, treinar o modelo de classificação e exibir a Matriz de Confusão com os resultados finais.



## 📌 Justificativa da Escolha do Sensor

O sensor **DS18B20** foi escolhido para a leitura precisa de temperatura, o **MPU6050** para medir a vibração da máquina através de seu acelerômetro, e o **HC-SR04** para a medição do nível de enchimento sem contato com o produto. Em conjunto, esses sensores permitem simular um cenário realista de monitoramento em linhas de envase de bebidas, onde variações nessas três grandezas são indicadores críticos de possíveis falhas no processo.

---

## 🔌 Esquema dos Circuitos

## 💨 MPU6050
![Circuito MPU5060](img/mpu5060.JPG)

---

### 🧾 Trecho Representativo do Código MPU6050

O trecho abaixo representa a lógica principal do projeto, responsável por:

- Simular a leitura de vibração com base na aceleração detectada na máquina;
- Classificar o status do sistema em três níveis: `NORMAL`, `ALERTA_Pre_falha` ou `FALHA_CRITICA`;
- Exibir os dados simulados no Monitor Serial em formato CSV (separado por vírgulas), facilitando análise posterior ou exportação.

```cpp
// Trecho representativo da leitura e visualização dos dados do MPU6050

// Definição dos limites para classificação em NORMAL, ALERTA_Pre_falha ou FALHA_CRITICA
const double LIMITE_ALERTA = 16500.0; 
const double LIMITE_FALHA = 25000.0;

// Exibe os dados formatados no Monitor Serial
Serial.print(contador + 1);
Serial.print(",");
Serial.print(accTotal);
Serial.print(",");

// Classificação do status no Monitor Serial
if (accTotal < LIMITE_ALERTA) {
  Serial.println("NORMAL");
} else if (accTotal < LIMITE_FALHA) {
  Serial.println("ALERTA_Pre_falha");
} else {
  Serial.println("FALHA_CRITICA");
}

```
---

### ⚙️ Funcionamento do Sistema MPU6050

1. O ESP32 simulado lê a aceleração da máquina a cada 1 segundo através do MPU6050.
2. A vibração é simulada com valores variados, dependendo da movimentação dos eixos X, Y e Z.
3. Os dados são classificados automaticamente em três status:
   - **NORMAL**: até 16500.0LSB/g
   - **ALERTA_Pre_falha**: de 16500.0LSB/g até 25000.0LSB/g
   - **FALHA_CRITICA**: acima de 25000.0LSB/g
4. Os dados são exibidos no **Monitor Serial** no formato CSV:  
   `ID, Aceleracao_Total, Status`

---

### 🔌 Simulação no Wokwi - MPU6050 e ESP32
![Simulação MPU6050](img/mpu5060_terminal.JPG)

---

### 🧪 Exemplo de Dados Coletados MPU6050

| ID | Aceleracao_Total| Status          |
|----------|----------------|------------------|
| 32   | 5049.47           | NORMAL           |
| 97    | 18426.64         | ALERTA_Pre_falha |
| 213    | 52453.14         | FALHA_CRITICA    |

---

### 📊 Gráfico Gerado MPU6050

![Gráfico de Vibração](img/grafico_mpu5060.png)

### 📝 Estrutura e Racional do Gráfico MPU6050

O gráfico gerado apresenta a variação da aceleração simulada ao longo das medições, com o eixo X representando as medições (totalizando 500 medições) e o eixo Y representando a vibração em LSB/g (Least Significant Bit por g). Para facilitar a interpretação, a classificação foi colorida conforme **classificação automática do status operacional**:

- **NORMAL (verde)**: Aceleração abaixo de 16500.0LSB/g - operação dentro do esperado.
- **ALERTA_Pre_falha (laranja)**: Aceleração de 16500.0LSB/g até 25000.0LSB/g - possível acerelação demasiada, atenção recomendada.
- **FALHA_CRITICA (vermelho)**: Aceleração acima de 25000.0LSB/g - – indicativo de falha crítica, requer ação imediata.

---

## 🌡️ DS18B20
![Circuito DS18B20](img/DS18B20.JPG)

### 🧾 Trecho Representativo do Código DS18B20

O trecho abaixo representa a lógica principal do projeto, responsável por:

- Simular a leitura de temperatura de bebidas geladas com envase a frio;
- Classificar o status do sistema em três níveis: `NORMAL`, `ALERTA_Pre_falha` ou `FALHA_CRITICA`;
- Exibir os dados simulados no Monitor Serial em formato CSV (separado por vírgulas), facilitando análise posterior ou exportação.

```cpp
// Trecho representativo da leitura e visualização dos dados do DS18B20

// Definição dos limites para classificação em NORMAL, ALERTA_Pre_falha ou FALHA_CRITICA
const float TEMPERATURA_NORMAL_MIN = -1.0;
const float TEMPERATURA_NORMAL_MAX = 6.0;
const float TEMPERATURA_FALHA_CRITICA_MIN = -6.0;
const float TEMPERATURA_FALHA_CRITICA_MAX = 10.0;

// Exibe os dados formatados no Monitor Serial
Serial.print(contador + 1);
Serial.print(",");
Serial.print(temperatura);
Serial.print(",");

// Classificação do status no Monitor Serial
if (temperatura >= TEMPERATURA_NORMAL_MIN && temperatura <= TEMPERATURA_NORMAL_MAX) {
  Serial.println("NORMAL");
} else if (temperatura < TEMPERATURA_NORMAL_MIN || temperatura > TEMPERATURA_NORMAL_MAX) 
      
  if (temperatura >= TEMPERATURA_FALHA_CRITICA_MIN && temperatura <= TEMPERATURA_FALHA_CRITICA_MAX) {
      Serial.println("ALERTA_Pre_falha");
  } else {
      Serial.println("FALHA_CRITICA");
      }

```
---

### ⚙️ Funcionamento do Sistema DS18B20

1. O ESP32 simulado lê a temperatura da máquina a cada 1 segundo através do DS18B20.
2. A temperatura é simulada com valores variados, conforme a oscilação.
3. Os dados são classificados automaticamente em três status:
   - **NORMAL**: até 6ºC
   - **ALERTA_Pre_falha**: de 6ºC até 10ºC
   - **FALHA_CRITICA**: acima de 10ºC
4. Os dados são exibidos no **Monitor Serial** no formato CSV:  
   `ID, Temperatura, Status`

---

### 🔌 Simulação no Wokwi - DS18B20 e ESP32
![Simulação DS18B20](img/ds18b20_terminal.JPG)


### 🧪 Exemplo de Dados Coletados DS18B20

| ID | Temperatura | Status          |
|----------|----------------|------------------|
| 17   | 1.37          | NORMAL           |
| 65   | 8.38         | ALERTA_Pre_falha |
| 118   | 14.25         | FALHA_CRITICA    |

### 📊 Gráfico Gerado DS18B20

![Gráfico de Temperatura](img/grafico_DS18B20.png)

### 📝 Estrutura e Racional do Gráfico DS18B20

O gráfico gerado apresenta a variação da temnperatura simulada ao longo das medições (totalizando 500 medições). Para facilitar a interpretação, a classificação foi colorida conforme **classificação automática do status operacional**:

- **NORMAL (verde)**: Temperatura abaixo de 6ºC - operação dentro do esperado.
- **ALERTA_Pre_falha (laranja)**: Temmperatura de 6ºC até 10ºC - possível acerelação demasiada, atenção recomendada.
- **FALHA_CRITICA (vermelho)**: Temperatura acima de 10ºC - – indicativo de falha crítica, requer ação imediata.


## 〰️ HC-SR04
![Circuito HC-SR04](img/HC-SR04.JPG)


### 🧾 Trecho Representativo do Código HC-SR04

O trecho abaixo representa a lógica principal do projeto, responsável por:

- Simular a leitura de nível de enchimento dos recipientes de bebidas;
- Classificar o status do sistema em três níveis: `NORMAL`, `ALERTA_Pre_falha` ou `FALHA_CRITICA`;
- Exibir os dados simulados no Monitor Serial em formato CSV (separado por vírgulas), facilitando análise posterior ou exportação.

```cpp
// Trecho representativo da leitura e visualização dos dados do HC-SR04

// Definição dos limites para classificação em NORMAL, ALERTA_Pre_falha ou FALHA_CRITICA
const float ALTURA_MAXIMA = 20.0;
const float NIVEL_NORMAL_MIN = 19.0;
const float NIVEL_NORMAL_MAX = 20.0;
const float NIVEL_ALERTA_MIN = 16.0;
const float NIVEL_ALERTA_MAX = 19.0;

// Exibe os dados formatados no Monitor Serial
 Serial.print(contador + 1);
    Serial.print(",");
    Serial.print(distancia_cm);
    Serial.print(",");
    Serial.print(nivel_cm);
    Serial.print(",");

 // Classificação do status no Monitor Serial   
    if (nivel_cm >= NIVEL_NORMAL_MIN && nivel_cm <= NIVEL_NORMAL_MAX) {
      Serial.println("NORMAL");
    } else if (nivel_cm >= NIVEL_ALERTA_MIN && nivel_cm < NIVEL_NORMAL_MIN) {
      Serial.println("ALERTA_Pre_falha");
    } else {
      Serial.println("FALHA_CRITICA");
    }

```

---

### ⚙️ Funcionamento do Sistema HC-SR04

1. O ESP32 simulado lê a distância do líquido até o sensor HC-SR04 a cada 1 segundo.
2. A temperatura é simulada com valores variados, conforme a oscilação.
3. Os dados são classificados automaticamente em três status:
   - **NORMAL**: acima de 20cm
   - **ALERTA_Pre_falha**: de 16 a 18cm
   - **FALHA_CRITICA**: abaixo de 16cm
4. Os dados são exibidos no **Monitor Serial** no formato CSV:  
   `ID, Distancia_cm, Nivel_cm, Status`

---

### 🔌 Simulação no Wokwi - HC-SR04 e ESP32
![Simulação HC-SR04](img/HC-SR04_terminal.JPG)

### 🧪 Exemplo de Dados Coletados HC-SR04

| ID | Distancia_cm | Nivel_cm         | Status          |
|----|--------------|------------------|-----------------|
| 29 | 1.94         | 23.06            | NORMAL          |
| 99 | 7.97         | 17.03            | ALERTA_Pre_falha|
| 213| 9.07         | 15.93            | FALHA_CRITICA   |

### 📊 Gráfico Gerado HC-SR04

![Gráfico de Nível de Enchimento](img/grafico_HC-SR04.png)

### 📝 Estrutura e Racional do Gráfico HC-SR04

O gráfico gerado apresenta a variação do nível de enchimentos dos recipientes simulado ao longo das medições (totalizando 500 medições). Para facilitar a interpretação, a classificação foi colorida conforme **classificação automática do status operacional**:

- **NORMAL (verde)**: Nível de 19 a 20cm - operação dentro do esperado.
- **ALERTA_Pre_falha (laranja)**: Nível de 16 a 18cm - possível acerelação demasiada, atenção recomendada.
- **FALHA_CRITICA (vermelho)**: Nível abaixo de 16cm - – indicativo de falha crítica, requer ação imediata.

---

## ✅ Insights Iniciais

- **NORMAL**
- **ALERTA_Pre_falha**
- **FALHA_CRITICA**

Essa análise demonstra que o sistema de simulação e classificação está funcionando conforme esperado, permitindo a identificação clara de mudanças na vibração, temperatura e nível de enchimento. Isso é essencial para o monitoramento preventivo e tomada de decisão.

Essa categorização tem como objetivo simular o comportamento de um sistema embarcado que não apenas coleta dados, mas também realiza uma **análise embarcada**, classificando os dados com base em faixas de operação seguras ou críticas. Essa estratégia permite que o dispositivo reaja localmente ou envie alertas para a nuvem em casos de falha iminente, antecipando paradas e aumentando a confiabilidade do processo industrial.

Os gráficos apresentados anteriormente, também fornecem uma visão clara da transição entre os diferentes estados, evidenciando o momento em que o sistema passa de uma operação estável para condições críticas.

---

## 📊 Banco de Dados

Para armazenar os dados de forma estruturada, foi projetado um banco de dados relacional simples e eficiente, implementado em SQLite. Esta abordagem garante a integridade e facilita as consultas complexas necessárias para a análise de Machine Learning.

### Diagrama Entidade-Relacionamento (DER)
O diagrama abaixo ilustra a modelagem, com suas entidades, atributos e relacionamentos.

![Modelagem de dados](img/modelagem.JPG)

### Descrição das Entidades e Relacionamentos

A modelagem de dados foi estruturada para refletir o ambiente industrial de forma clara e normalizada:

* **MAQUINAS:** Entidade central que representa os equipamentos físicos na linha de produção.
    * `id_maquina`: Chave primária para identificação única.
    * `nome`, `localizacao`: Atributos que descrevem a máquina.

* **SENSORES:** Representa os dispositivos de coleta de dados instalados nas máquinas.
    * `id_sensor`: Chave primária.
    * `id_maquina`: Chave estrangeira que estabelece o relacionamento **(1:N)** com a tabela `MAQUINAS`, indicando que **uma máquina pode ter vários sensores**.
    * `tipologia`: Descreve o tipo de dado que o sensor coleta (temperatura, vibração, etc.).

* **MEDICAO_VIBRACAO / TEMPERATURA / NIVEL:** Tabelas que armazenam os dados históricos de cada sensor.
    * `id`: Chave primária para cada registro de medição.
    * `id_sensor`: Chave estrangeira que estabelece o relacionamento **(1:N)** com a tabela `SENSORES`, indicando que **um sensor pode realizar múltiplas medições** ao longo do tempo.
    * `aceleracao_total`, `medicao`, `nivel_cm`: Atributos que guardam o valor numérico da leitura.
    * `status`: Campo que armazena a classificação da medição, fundamental para o treinamento do modelo de ML.

### Automação da Criação e Povoamento

Para garantir a consistência e reprodutibilidade do projeto, todo o processo de criação e povoamento do banco foi automatizado:

1.  **`schema.sql`:** Um único script contém todo o código DDL (Data Definition Language) para criar as tabelas e definir os relacionamentos (`FOREIGN KEY`), garantindo a integridade referencial.
2.  **`import_data.py`:** Este script Python utiliza a biblioteca `sqlite3` e `pandas` para:
    * Criar o banco `hermes_db.sqlite` executando o `schema.sql`.
    * Inserir os dados estáticos das máquinas e tipos de sensores.
    * Ler os arquivos `medicao_*.csv`, processá-los e inseri-los nas tabelas de medição correspondentes.

```python
# Trecho do import_data.py que popula a tabela de vibração
df_vibracao = pd.read_csv('data/medicao_vibracao.csv')
df_vibracao['id_sensor'] = 3 # Associa ao sensor de vibração
df_vibracao = df_vibracao.rename(columns={'ID': 'id', 'Aceleracao_Total': 'aceleracao_total', 'Status': 'status'})
df_vibracao.to_sql('MEDICAO_VIBRACAO', conn, if_exists='append', index=False)
  
```

### Integração com Ferramentas de Visualização

O banco de dados foi modelado de forma relacional e centralizada não apenas para servir ao modelo de Machine Learning, mas também para funcionar como uma fonte de dados robusta para ferramentas de Business Intelligence (BI). Em uma implementação industrial, os dados armazenados poderiam ser conectados a plataformas como **Power BI**, **Tableau** ou **Grafana** para a criação de dashboards interativos. Isso permitiria que os gestores da linha de produção monitorem a saúde dos equipamentos em tempo real, analisem tendências históricas e tomem decisões mais assertivas baseadas em dados visuais.

---

# 📜 Etapas

## 1. Cadastro de máquinas
Há necessidade de cadastrar todas as máquinas da indústria.

📊 **Dados Necessários**
- Nome da máquina
- Localização da máquina dentro da indústria

## 2. Identificação dos sensores
Há necessidade de identificação de todos os sensores presentes nas máquinas.

📊 **Dados Necessários**
- Tipologia
- Máquina localizada

## 3. Recebimento de dados de sensores
O sistema deverá receber os dados de cada sensor.

📊 **Dados Recebidos**
- Medição
- Status

## 4. Banco de dados
A partir das informações recebidas e registradas, deverão ser armazenadas em um banco de dados. 

> Os relacionamentos entre as entidades irão proporcionar insights valiosos que poderão ser detectados pelo modelo preditivo.

---

# 🖥️ Machine Learning

O objetivo do modelo de Machine Learning é classificar o status de operação com base nas leituras dos sensores. O processo foi documentado no notebook `machine_learning.ipynb`.

1.  **Carga e Unificação dos Dados**
    
    Os dados de todas as tabelas de medição foram unificados com uma consulta SQL diretamente no banco de dados, criando um único DataFrame para o treinamento.

    ```python
    # Unifica os dados de todos os sensores
    query = """
    SELECT 'nivel' as tipo, nivel_cm as medicao, status FROM MEDICAO_NIVEL
    UNION ALL
    SELECT 'temperatura' as tipo, medicao, status FROM MEDICAO_TEMPERATURA
    UNION ALL
    SELECT 'vibracao' as tipo, aceleracao_total as medicao, status FROM MEDICAO_VIBRACAO;
    """
    df = pd.read_sql_query(query, conn)
    ```

2.  **Treinamento do Modelo**
    
    Foi utilizado um modelo de Árvore de Decisão (DecisionTreeClassifier), escolhido por sua simplicidade e interpretabilidade. Os dados foram divididos em 70% para treino e 30% para teste.

3.  **Resultados e Avaliação**
    
    O modelo alcançou uma acurácia de 100% no conjunto de teste. Este resultado perfeito é esperado, pois os dados foram gerados com regras de classificação claras. Isso valida que o modelo aprendeu perfeitamente as regras definidas, servindo como uma excelente prova de conceito. Todavia, em um cenário real, os dados teriam mais "ruído" e as fronteiras entre as classes não seriam tão perfeitas, o que levaria a uma acurácia menor, mas ainda assim o modelo seria útil.
    
    Para visualizar a performance, foi gerada uma Matriz de Confusão.

    ![Matriz de Confusão](img/matriz_confusao.png)

4.  **Justificativa da Visualização**
    
    A Matriz de Confusão é a ferramenta padrão para avaliar modelos de classificação. A diagonal principal mostra o número de previsões corretas para cada classe. No nosso caso, todos os valores estão na diagonal principal, confirmando que o modelo classificou todas as 450 amostras de teste corretamente, sem nenhum erro. Isso é muito mais informativo do que apenas a acurácia geral.


## 📁 Estrutura do Repositório

```bash
/enterprise-challenge-phase04
/
├── .sql/
│   └── schema.sql                  # Script DDL para criação da estrutura do banco
│
├── data/
│   ├── medicao_nivel.csv           # Dados simulados do sensor de nível
│   ├── medicao_temperatura.csv     # Dados simulados do sensor de temperatura
│   └── medicao_vibracao.csv        # Dados simulados do sensor de vibração
│
├── .json/
│   ├── diagram_DS18B20.json        # Diagrama de circuito para o Wokwi
│   ├── diagram_HC-SR04.json        # "
│   └── diagram_MPU6050.json        # "
│
├── notebooks/
│   ├── grafico.ipynb               # (Opcional) Notebook para geração de gráficos avulsos
│   └── machine_learning.ipynb      # Notebook principal com o treino e avaliação do modelo
│
├── scripts/
│   ├── update_diagram.py           # Script para atualizar o diagrama do Wokwi automaticamente
|   └── import_data.py              # Script para popular banco de dados com dados de medição
│
├── src/
│   ├── ds18b20_main.cpp            # Código-fonte da simulação para o sensor de temperatura
│   ├── hcsr04_main.cpp             # Código-fonte da simulação para o sensor de nível
│   └── mpu6050_main.cpp            # Código-fonte da simulação para o sensor de vibração
│
├── .gitignore                      # Arquivos ignorados pelo Git
├── diagram.json                    # Arquivo de diagrama ATUAL do Wokwi (gerado via script)
├── platformio.ini                  # Configuração do PlatformIO com múltiplos ambientes
├── README.md                       # Esta documentação
└── wokwi.toml                      # Configuração do Wokwi para carregar o firmware
```
---

## 🧠 Conclusão

Nesta fase do projeto, evoluímos da simulação de dados para a construção de uma solução de dados completa e integrada. A criação de um banco de dados relacional e a automação da importação de dados estabeleceram uma base sólida e escalável. A aplicação de um modelo de Machine Learning demonstrou com sucesso a capacidade de extrair insights preditivos, validando o pipeline de ponta a ponta. O projeto agora não apenas coleta e armazena dados, mas também os utiliza para gerar inteligência, cumprindo plenamente os objetivos da manutenção preditiva.

---

## 🎬 Vídeo Explicativo

Assista ao vídeo de até 5 minutos explicando e justificando o projeto desta fase:

[Link para o vídeo no YouTube (Não Listado)]()

---

## 📜 Licença

Este projeto está licenciado sob os termos da licença **CC BY 4.0**.

---
