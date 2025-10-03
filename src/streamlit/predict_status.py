import streamlit as st
import pandas as pd
import joblib

def reset_inputs():
    st.session_state['temperatura'] = 0.0
    st.session_state['nivel'] = 0.0
    st.session_state['vibracao'] = 0.0

def main():
    # Inicializa session_state antes de criar os widgets
    for var in ['temperatura', 'nivel', 'vibracao']:
        if var not in st.session_state:
            st.session_state[var] = 0.0

    # Carregar o modelo treinado
    model = joblib.load('./../../notebooks/decision_tree_model.pkl')

    st.title("💡 Previsão de Status com Decision Tree")
    st.write("Preencha os valores abaixo para prever o status:")

    # Inputs controlados por session_state
    temperatura = st.number_input("Temperatura (°C)", step=0.1, key='temperatura')
    nivel = st.number_input("Nível", step=0.1, key='nivel')
    vibracao = st.number_input("Vibração", step=0.1, key='vibracao')

    col1, col2 = st.columns(2)
    with col1:
        prever = st.button("Prever Status")
    with col2:
        limpar = st.button("Limpar Campos", on_click=reset_inputs)

    if prever:
        input_data = {
            'medicao': 0,
            'tipo_temperatura': False,
            'tipo_nivel': False,
            'tipo_vibracao': False
        }

        if temperatura != 0.0 and nivel == 0.0 and vibracao == 0.0:
            input_data['medicao'] = temperatura
            input_data['tipo_temperatura'] = True
        elif nivel != 0.0 and temperatura == 0.0 and vibracao == 0.0:
            input_data['medicao'] = nivel
            input_data['tipo_nivel'] = True
        elif vibracao != 0.0 and temperatura == 0.0 and nivel == 0.0:
            input_data['medicao'] = vibracao
            input_data['tipo_vibracao'] = True
        else:
            st.warning("Preencha apenas UM campo por vez para previsão.")
            return

        input_df = pd.DataFrame([input_data])[['medicao', 'tipo_temperatura', 'tipo_vibracao', 'tipo_nivel']]
        status_pred = model.predict(input_df)[0]
        status_map = {
            0: "ALERTA_Pre_falha",
            1: "FALHA_CRITICA",
            2: "NORMAL"
        }
        status_str = status_map.get(status_pred, "Desconhecido")
        st.success(f"Status previsto: **{status_str}**")