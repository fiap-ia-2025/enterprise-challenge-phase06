# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
  <a href="https://www.fiap.com.br/">
    <img src="img/logo-fiap.png" alt="FIAP - Faculdade de Informática e Administração Paulista" border="0" width="40%" height="40%">
  </a>
</p>

---

# 📦 Enterprise Challenge - Sprint 2
<!-- Título do projeto: curto, claro, direto. Pode destacar o problema e a tecnologia principal -->

## 👥 Grupo 
<!-- Nome oficial do grupo, se houver. Pode usar um nome criativo também -->

## 👨‍🎓 Integrantes:
- Amanda Vieira Pires (RM565045)
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

## 📜 Descrição do Projeto
## 🎯 Objetivo

- Criar um circuito virtual com ESP32 e sensor DHT22 no Wokwi;
- Simular variações de temperatura conforme diferentes momentos de operação;
- Classificar os valores em três categorias: `NORMAL`, `ALERTA_Pre_falha` e `FALHA_CRITICA`;
- Registrar os dados via Monitor Serial;
- Exportar os dados simulados para CSV;
- Gerar um gráfico simples com base nos dados simulados;
- Documentar todo o processo no GitHub com prints, código e análise.

---

## 🔧 Estrutura de Simulação

- **Plataforma de Simulação:** Wokwi
- **Microcontrolador:** ESP32 (simulado)
- **Linguagem:** C++ (com base na plataforma PlataformIO com VS Code)
- **Sensor Utilizado:**  
  - `DHT22`: sensor digital de temperatura e umidade
- **Biblioteca `DHT` da Adafruit**

---

## 📌 Justificativa da Escolha do Sensor

O sensor **DHT22** foi escolhido por sua ampla utilização na indústria para controle ambiental, oferecendo leitura precisa de **temperatura e umidade**, o que permite simular falhas térmicas em ambientes como linhas de produção.

---

## 🔌 Esquema do Circuito
![Circuito DHT22](circuito.png)

---

## ⚙️ Funcionamento do Sistema

1. O ESP32 simulado lê a temperatura do sensor DHT22 a cada 1 segundo.
2. A temperatura é simulada com valores variados, dependendo do tempo de execução.
3. Os dados são classificados automaticamente em três status:
   - **NORMAL**: até 9,0°C
   - **ALERTA_Pre_falha**: de 9,1°C até 11,9°C
   - **FALHA_CRITICA**: acima de 12,0°C
4. Os dados são exibidos no **Monitor Serial** no formato CSV:  
   `Tempo_ms,Temperatura_C,Status`

---

## 🧪 Exemplo de Dados Coletados

| Tempo_ms | Temperatura_C | Status           |
|----------|----------------|------------------|
| 485      | 6.3            | NORMAL           |
| 5839     | 10.4           | ALERTA_Pre_falha |
| 10839    | 13.2           | FALHA_CRITICA    |


---

## 📊 Gráfico Gerado

![Gráfico de Temperatura e Status](grafico.png)

---

## 🔍 Insights Iniciais

- As faixas de temperatura simuladas refletem **comportamentos distintos operacionais**, com **zonas claras de risco** após os 10 segundos de simulação.
- A visualização permite **identificar tendências de aquecimento anormal**, o que, em um cenário real, poderia acionar ações preventivas de manutenção.
- A classificação automática em tempo real permite embasar **modelos de predição futuros** com base em dados históricos simulados.

---

## 📁 Estrutura do Repositório

```bash
/enterprise-challenge-phase04
├── src/
│   ├──main.cpp
│
├── diagram.json                # Circuito simulado no Wokwi
├──  platformio.ini             # Configuração do PlatformIO
├──  wokwi.toml                 # Caminho para firmware na simulação
├── dados_temperatura.csv       # Registro dos dados
│
├── img/                        # Imagens utilizadas no README
│   ├── circuito.png            # Print do circuito no Wokwi
│   ├── logo_fiap.png           # Logo da faculdade
│   ├── grafico.png             # Imagem do gráfico
│
├── .gitignore                  # Arquivos/pastas ignorados pelo Git
└── README.md                   # Documentação geral do projeto
```
---

## 🧠 Conclusão

A simulação do sensor DHT22 no Wokwi permitiu compreender o fluxo completo de aquisição de dados com o ESP32, incluindo geração de dados simulados, categorização automatizada, e preparação para análise em Python. 

---

## 📜 Licença

Este projeto está licenciado sob os termos da licença **CC BY 4.0**.

---
