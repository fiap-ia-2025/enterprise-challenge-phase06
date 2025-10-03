import streamlit as st

# Importar as páginas
import home
import predict_status

# Sidebar customizada
st.sidebar.markdown(
    """
    <style>
    .sidebar-title {
        font-size: 28px;
        font-weight: bold;
        color: #0A58CA;
        margin-bottom: 20px;
    }
    .sidebar-logo {
        display: block;
        margin-left: auto;
        margin-right: auto;
        width: 60%;
        margin-bottom: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# (Opcional) Adicione um logo se quiser, basta colocar o caminho do arquivo
# st.sidebar.image("logo.png", use_column_width=True, output_format='PNG', caption="FIAP Challenge")

st.sidebar.markdown('<div class="sidebar-title">🚀 Enterprise Challenge</div>', unsafe_allow_html=True)
st.sidebar.markdown("---")
page = st.sidebar.radio("Escolha a página:", ("📊 Dashboard", "🤖 Previsão de Status"))

if page == "📊 Dashboard":
    home.main()
elif page == "🤖 Previsão de Status":
    predict_status.main()