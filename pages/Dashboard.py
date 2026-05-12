import streamlit as st
import importlib

# PAGINAS disponíveis no sistema
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
            # Definição de quais temas são exclusivos do PREMIUM
            temas_premium = ["Santa Ceia", "Mulheres", "Jovens"]
            e_premium = pagina['titulo'] in temas_premium
            
            label = f"{pagina['icone']}  {pagina['titulo']}"
            
            # Lógica de Bloqueio por Plano
            if e_premium and plano == "START":
                st.button(f"🔒 {pagina['titulo']}", key=f"btn_lock_{pagina['modulo']}", disabled=True, use_container_width=True)
                st.caption("Disponível no Premium")
            else:
                # O uso da KEY única evita o erro de "Multiple elements with the same ID"
                if st.button(label, key=f"btn_nav_{pagina['modulo']}", use_container_width=True):
                    st.session_state.pagina_atual = pagina['modulo']
                    st.rerun()

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("---")

    # Renderiza a página selecionada abaixo dos botões
    if st.session_state.pagina_atual:
        try:
            modulo = importlib.import_module(st.session_state.pagina_atual)
            importlib.reload(modulo) 
            modulo.exibir()
        except Exception as e:
            st.error(f"Erro ao carregar a categoria: {e}")
