import streamlit as st
import importlib

# REMOVIDO: st.set_page_config() — já está definido no app.py

PAGINAS = [
    {"icone": "⛪", "titulo": "Cultos Gerais",        "modulo": "pages.Cultos_Gerais"},
    {"icone": "🎉", "titulo": "Datas Comemorativas",  "modulo": "pages.Datas_Comemorativas"},
    {"icone": "👨‍👩‍👧‍👦", "titulo": "Família",              "modulo": "pages.Familia"},
    {"icone": "🧔", "titulo": "Homens",               "modulo": "pages.Homens"},
    {"icone": "🧸", "titulo": "Infantil",             "modulo": "pages.Infantil"},
    {"icone": "🔥", "titulo": "Jovens",               "modulo": "pages.Jovens"},
    {"icone": "🌸", "titulo": "Mulheres",             "modulo": "pages.Mulheres"},
    {"icone": "🍷", "titulo": "Santa Ceia",           "modulo": "pages.Santa_Ceia"},
]

def exibir():
    with open("style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    # CSS extra para os cards de navegação do dashboard
    st.markdown("""
        <style>
        div.stButton > button:first-child {
            background-color: #0c0c0c !important;
            color: #ffffff !important;
            border: 1px solid #1f1f1f !important;
            border-radius: 15px !important;
            padding: 30px 20px !important;
            font-size: 1.1rem !important;
            font-weight: 600 !important;
            transition: all 0.3s ease !important;
            box-shadow: none !important;
        }
        div.stButton > button:first-child:hover {
            border-color: #FF2D95 !important;
            box-shadow: 0 0 15px rgba(255, 45, 149, 0.3) !important;
            transform: translateY(-2px);
            color: #FF2D95 !important;
        }
        </style>
    """, unsafe_allow_html=True)

    nome = st.session_state.get('nome_usuario', 'Irmão')
    plano = st.session_state.get('plano', 'START')

    st.markdown("<h1 class='gradient-title'>🏠 Dashboard</h1>", unsafe_allow_html=True)
    st.success(f"👋 Olá, **{nome}** | Plano: **{plano}**")
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("### 🎨 Escolha um tema para acessar as artes:")
    st.markdown("<br>", unsafe_allow_html=True)

    if 'pagina_atual' not in st.session_state:
        st.session_state.pagina_atual = None

    # Grid de botões: 4 colunas
    cols = st.columns(4)
    for i, pagina in enumerate(PAGINAS):
        with cols[i % 4]:
            label = f"{pagina['icone']}  {pagina['titulo']}"
            if st.button(label, key=f"btn_{pagina['modulo']}", use_container_width=True):
                st.session_state.pagina_atual = pagina['modulo']
                st.rerun()

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("---")

    # Renderiza a página selecionada abaixo dos botões
    if st.session_state.pagina_atual:
        try:
            modulo = importlib.import_module(st.session_state.pagina_atual)
            importlib.reload(modulo)  # garante que recarrega corretamente
            modulo.exibir()
        except Exception as e:
            st.error(f"Erro ao carregar a página: {e}")

    # Botão de logout na sidebar
    if st.sidebar.button("🚪 Sair da conta"):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.rerun()
