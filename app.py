# app.py - Página Principal (Vitrine + Login)
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

# Importações
from modules.vitrine import exibir as vitrine_exibir
from modules.auth import tela_login

# Inicialização da sessão
if 'logado' not in st.session_state:
    st.session_state.logado = False

# ====================== FLUXO PRINCIPAL ======================
if not st.session_state.logado:
    # Tela Pública
    vitrine_exibir()
    st.markdown("---")
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        tela_login()
else:
    # Menu lateral para usuário logado
    st.sidebar.markdown(f"### 👋 Olá, **{st.session_state.get('nome_usuario', 'Membro')}**")
    st.sidebar.markdown(f"**Plano:** {st.session_state.get('plano', 'START')}")
    
    if st.sidebar.button("🚪 Sair da Área de Membros"):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.rerun()

    st.sidebar.success("✅ Use o menu lateral para navegar")
