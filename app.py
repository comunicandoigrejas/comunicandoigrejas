# app.py
import streamlit as st

st.set_page_config(
    page_title="Comunicando Igrejas",
    layout="wide",
    page_icon="⛪",
    initial_sidebar_state="expanded"
)

# CSS Global
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

from modules.vitrine import exibir as vitrine_exibir
from modules.auth import tela_login

if 'logado' not in st.session_state:
    st.session_state.logado = False

if not st.session_state.logado:
    vitrine_exibir()
    st.markdown("---")
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        tela_login()

else:
    # === USUÁRIO LOGADO ===
    st.sidebar.markdown(f"### 👋 Olá, **{st.session_state.get('nome_usuario', 'Membro')}**")
    st.sidebar.markdown(f"**Plano:** {st.session_state.get('plano', 'START')}")
    
    if st.sidebar.button("🚪 Sair"):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.rerun()

    # Redireciona automaticamente para o Dashboard após login
    st.switch_page("pages/0_dashboard.py")
