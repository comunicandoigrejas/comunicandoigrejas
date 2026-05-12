# app.py - Página Principal
import streamlit as st

st.set_page_config(
    page_title="Comunicando Igrejas",
    layout="wide",
    page_icon="⛪",
    initial_sidebar_state="expanded"
)

# Carregar CSS Global
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Importações necessárias
from modules.vitrine import exibir as vitrine_exibir
from modules.auth import tela_login

if 'logado' not in st.session_state:
    st.session_state.logado = False
    st.session_state.nome_usuario = ""
    st.session_state.plano = ""

if not st.session_state.logado:
    vitrine_exibir()
    st.markdown("---")
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        tela_login()
else:
    st.sidebar.markdown(f"### 👋 Olá, **{st.session_state.nome_usuario}**")
    st.sidebar.markdown(f"**Plano:** {st.session_state.plano}")
    
    if st.sidebar.button("🚪 Sair"):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.rerun()
