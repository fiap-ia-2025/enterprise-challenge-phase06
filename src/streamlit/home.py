import pandas as pd  # Manipula e carrega dados em tabelas (DataFrames)
import streamlit as st  # Cria a interface web interativa com Streamlit
import plotly.express as px

st.set_page_config(page_title="Manutenção preditiva em linhas de envase", layout="wide")

def main():

    # Estrutura do cabeçalho e layout da página
    st.title("💦 Dashboard - Manutenção preditiva em linhas de envase")
    st.markdown(
        "Este painel apresenta a leitura dos sensores de temperatura, vibração e nível de líquido")

    # Carregar os dados
    df_temperatura = pd.read_csv('./../../data/medicao_temperatura.csv')
    df_nivel = pd.read_csv('./../../data/medicao_nivel.csv')
    df_vibracao = pd.read_csv('./../../data/medicao_vibracao.csv')

    # Renomear colunas para evitar conflitos
    df_nivel = df_nivel.rename(columns={'Nivel_cm': 'Nivel'})
    df_vibracao = df_vibracao.rename(columns={'Aceleracao_Total': 'Vibracao'})
    st.title("Dashboard Industrial: Temperatura, Nível e Vibração")

    # =======================
    # KPIs e Métricas
    # =======================

    # Temperatura
    st.subheader("Temperatura")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Medições", len(df_temperatura))
    col2.metric("Temperatura Média (°C)", f"{df_temperatura['Temperatura'].mean():.2f}")
    col3.metric("Temperatura Máxima (°C)", f"{df_temperatura['Temperatura'].max():.2f}")
    col4.metric("Qtd. Alertas Temperatura", df_temperatura[df_temperatura['Status'] == 'ALERTA_Pre_falha'].shape[0])

    # Nível
    st.subheader("Nível")
    col5, col6, col7, col8 = st.columns(4)
    col5.metric("Nível Médio", f"{df_nivel['Nivel'].mean():.2f}")
    col6.metric("Nível Mínimo", f"{df_nivel['Nivel'].min():.2f}")
    col7.metric("Nível Máximo", f"{df_nivel['Nivel'].max():.2f}")
    col8.metric("Qtd. Leituras Críticas", df_nivel[df_nivel['Nivel'] < 2].shape[0])  # Exemplo: nível crítico < 2

    # Vibração
    st.subheader("Vibração")
    col9, col10, col11, col12 = st.columns(4)
    col9.metric("Vibração Média", f"{df_vibracao['Vibracao'].mean():.2f}")
    col10.metric("Vibração Máxima", f"{df_vibracao['Vibracao'].max():.2f}")
    col11.metric("Vibração Mínima", f"{df_vibracao['Vibracao'].min():.2f}")
    col12.metric("Qtd. Vibração Alta", df_vibracao[df_vibracao['Vibracao'] > 8].shape[0])  # Exemplo: vibração alta > 8

    # =======================
    # Gráficos
    # =======================

    # Temperatura ao longo do tempo
    fig_temp = px.line(df_temperatura, x='ID', y='Temperatura', title='Evolução da Temperatura')
    st.plotly_chart(fig_temp, use_container_width=True)

    # Nível ao longo do tempo
    fig_nivel = px.line(df_nivel, x='ID', y='Nivel', title='Evolução do Nível')
    fig_nivel.update_traces(line_color='green')
    st.plotly_chart(fig_nivel, use_container_width=True)

    # Vibração ao longo do tempo
    fig_vib = px.line(df_vibracao, x='ID', y='Vibracao', title='Evolução da Vibração')
    fig_vib.update_traces(line_color='orange')
    st.plotly_chart(fig_vib, use_container_width=True)

    # Distribuição dos Status de Temperatura
    if 'Status' in df_temperatura.columns:
        status_counts = df_temperatura['Status'].value_counts().reset_index()
        status_counts.columns = ['Status', 'Contagem']
        fig_status = px.bar(status_counts, x='Status', y='Contagem', color='Status', title='Distribuição dos Status de Temperatura')
        st.plotly_chart(fig_status, use_container_width=True)
