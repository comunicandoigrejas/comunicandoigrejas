import streamlit as st
import importlib
import os

# PAGINAS disponíveis no sistema com as suas respetivas capas corrigidas
PAGINAS = [
    {"icone": "⛪", "titulo": "Cultos Gerais",        "modulo": "pages.Cultos_Gerais",        "capa": "Cultos Gerais 08.jpg"},
    {"icone": "🎉", "titulo": "Datas Comemorativas",  "modulo": "pages.Datas_Comemorativas",  "capa": None},
    {"icone": "👨‍👩‍👧‍👦", "titulo": "Família",              "modulo": "pages.Familia",              "capa": "Culto Familia 08.png"},
    {"icone": "🧔", "titulo": "Homens",               "modulo": "pages.Homens",               "capa": None},
    {"icone": "🧸", "titulo": "Infantil",             "modulo": "pages.Infantil",             "capa": None},
    {"icone": "🔥", "titulo": "Jovens",               "modulo": "pages.Jovens",               "capa": None},
    {"icone": "🌸", "titulo": "Mulheres",             "modulo": "pages.Mulheres",             "capa": None},
    {"icone": "🍷", "titulo": "Santa Ceia",           "modulo": "pages.Santa_Ceia",           "capa": None},
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
            temas_premium = ["Santa Ceia", "Mulheres", "Jovens"]
            e_premium = pagina['titulo'] in temas_premium
            
            label = f"{pagina['icone']}  {pagina['titulo']}"
            
            if e_premium and plano == "START":
                st.button(f"🔒 {pagina['titulo']}", key=f"btn_lock_{pagina['modulo']}", disabled=True, use_container_width=True)
                st.caption("Disponível no Premium")
            else:
                if st.button(label, key=f"btn_nav_{pagina['modulo']}", use_container_width=True):
                    st.session_state.pagina_atual = pagina['modulo']
                    st.rerun()

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("---")

    # --- RENDERIZAÇÃO DA CAPA DA CATEGORIA SELECIONADA ---
    if st.session_state.pagina_atual:
        # Procura os dados da página ativa para saber qual é a imagem da capa
        dados_pagina_atual = next((p for p in PAGINAS if p['modulo'] == st.session_state.pagina_atual), None)
        
        if dados_pagina_atual and dados_pagina_atual['capa']:
            capa_nome = dados_pagina_atual['capa']
            caminho_capa = f"assets/{capa_nome}"
            
            # Validação e exibição segura da imagem de capa antes do conteúdo da página
            if os.path.exists(caminho_capa):
                st.image(caminho_capa, use_container_width=True)
                st.markdown("<br>", unsafe_allow_html=True)
            elif os.path.exists(capa_nome):
                st.image(capa_nome, use_container_width=True)
                st.markdown("<br>", unsafe_allow_html=True)

        # Carrega o conteúdo dos modelos (ex: Familia.py ou Cultos_Gerais.py)
        try:
            modulo = importlib.import_module(st.session_state.pagina_atual)
            importlib.reload(modulo) 
            modulo.exibir()
        except Exception as e:
            st.error(f"Erro ao carregar a categoria: {e}")
