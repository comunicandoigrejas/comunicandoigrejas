# app.py
import streamlit as st

# ==================== CONFIGURAÇÃO DA PÁGINA ====================
st.set_page_config(
    page_title="Comunicando Igrejas",
    layout="wide",
    page_icon="⛪",
    initial_sidebar_state="expanded"
)

# ==================== CARREGAR CSS ====================
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# ==================== IMPORTAÇÕES ====================
from modules.vitrine import exibir as vitrine_exibir
from modules.auth import tela_login

# Temas
import modules.tema_geral as tema_geral
import modules.tema_familia as tema_familia
import modules.tema_jovens as tema_jovens
import modules.tema_mulheres as tema_mulheres
import modules.tema_homens as tema_homens
import modules.tema_infantil as tema_infantil
import modules.tema_santa_ceia as tema_santa_ceia
import modules.tema_comemorativo as tema_comemorativo

# ==================== INICIALIZAÇÃO DE SESSÃO ====================
if 'logado' not in st.session_state:
    st.session_state.logado = False
    st.session_state.nome_usuario = ""
    st.session_state.plano = ""

# ==================== FLUXO PRINCIPAL ====================
if not st.session_state.logado:
    # === TELA PÚBLICA (VITRINE + LOGIN) ===
    vitrine_exibir()
    
    st.markdown("---")
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        tela_login()

else:
    # === ÁREA RESTRITA (LOGADO) ===
    st.sidebar.markdown(f"### 👋 Olá, **{st.session_state.nome_usuario}**")
    st.sidebar.markdown(f"**Plano:** {st.session_state.plano}")
    
    # Opção padrão caso não tenha página definida
    if 'pagina' not in st.session_state:
        st.session_state.pagina = "Dashboard"

    opcao = st.sidebar.radio(
        "Navegue pelos Temas:",
        [
            "🏠 Dashboard",
            "⛪ Cultos Gerais",
            "👨‍👩‍👧‍👦 Família",
            "🔥 Jovens",
            "🌸 Mulheres",
            "🧔 Homens",
            "🧸 Infantil",
            "🍷 Santa Ceia",
            "🎉 Datas Comemorativas",
            "💬 Suporte"
        ],
        index=0 if st.session_state.pagina == "Dashboard" else None
    )

    if st.sidebar.button("🚪 Sair da Área de Membros"):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.rerun()

    # ==================== ROTEAMENTO INTELIGENTE ====================
    pagina_atual = st.session_state.pagina

    if opcao == "🏠 Dashboard" or pagina_atual == "Dashboard":
        from modules.dashboard import exibir as dashboard_exibir
        dashboard_exibir()

    elif opcao == "⛪ Cultos Gerais" or pagina_atual == "Cultos Gerais":
        tema_geral.exibir()
    elif opcao == "👨‍👩‍👧‍👦 Família" or pagina_atual == "Família":
        tema_familia.exibir()
    elif opcao == "🔥 Jovens" or pagina_atual == "Jovens":
        tema_jovens.exibir()
    elif opcao == "🌸 Mulheres" or pagina_atual == "Mulheres":
        tema_mulheres.exibir()
    elif opcao == "🧔 Homens" or pagina_atual == "Homens":
        tema_homens.exibir()
    elif opcao == "🧸 Infantil" or pagina_atual == "Infantil":
        tema_infantil.exibir()
    elif opcao == "🍷 Santa Ceia" or pagina_atual == "Santa Ceia":
        tema_santa_ceia.exibir()
    elif opcao == "🎉 Datas Comemorativas" or pagina_atual == "Datas Comemorativas":
        tema_comemorativo.exibir()
    elif opcao == "💬 Suporte" or pagina_atual == "Suporte":
        st.info("📌 Módulo de Suporte em desenvolvimento. Em breve!")
