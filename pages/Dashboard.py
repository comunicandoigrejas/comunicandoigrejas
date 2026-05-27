import streamlit as st
import importlib
import os

# --- PAGINAS disponíveis no sistema com suas capas associadas ---
PAGINAS = [
    {"icone": "⛪", "titulo": "Cultos Gerais",        "modulo": "pages.Cultos_Gerais",        "capa": "Cultos Gerais 08.jpg"},
    {"icone": "🎉", "titulo": "Datas Comemorativas",  "modulo": "pages.Datas_Comemorativas",  "capa": None},
    {"icone": "👨‍👩‍👧‍👦", "titulo": "Culto da Família",     "modulo": "pages.Familia",              "capa": "Culto Familia 08.png"},
    {"icone": "🧔", "titulo": "Culto de Homens",       "modulo": "pages.Homens",               "capa": None},
    {"icone": "🧸", "titulo": "Culto Infantil",         "modulo": "pages.Infantil",             "capa": None},
    {"icone": "⚡", "titulo": "Culto de Jovens",       "modulo": "pages.Jovens",               "capa": None},
    {"icone": "🌸", "titulo": "Culto de Mulheres",     "modulo": "pages.Mulheres",             "capa": None},
    {"icone": "🍷", "titulo": "Culto de Ceia",          "modulo": "pages.Santa_Ceia",           "capa": None},
]

def exibir():
    # --- CSS GLOBAL E PERSONALIZADO DO DASHBOARD ---
    with open("style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
        
    st.markdown("""
        <style>
        /* Estilização dos botões verdes */
        div.stButton > button {
            background-color: #2da042 !important; 
            color: #ffffff !important;
            font-weight: bold !important;
            border-radius: 6px !important;
            border: none !important;
            height: 50px !important;
            transition: background-color 0.2s !important;
        }
        div.stButton > button:hover {
            background-color: #3ccb57 !important;
        }
        </style>
    """, unsafe_allow_html=True)

    # --- TÍTULO E SAUDAÇÃO ---
    st.markdown("<h1 style='text-align: center; color: white;'>CATEGORIAS</h1>", unsafe_allow_html=True)
    
    nome = st.session_state.get('nome_usuario', 'Irmão')
    plano = st.session_state.get('plano', 'PREMIUM')
    st.markdown(f"<p style='text-align: center; color: #888;'>👋 Olá, irmão {nome} | Abaixo estão as suas artes do plano {plano}</p>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    if 'pagina_atual' not in st.session_state:
        st.session_state.pagina_atual = None

    # --- 1. EXIBIÇÃO DA IMAGEM DE CAPA (NO TOPO) ---
    capa_carregar = None
    
    # Define qual capa mostrar: se nenhuma página foi clicada, mostra Cultos Gerais por padrão
    if st.session_state.pagina_atual is None:
        capa_carregar = "assets/Cultos Gerais 08.jpg"
    else:
        dados_pagina_ativa = next((p for p in PAGINAS if p['modulo'] == st.session_state.pagina_atual), None)
        if dados_pagina_ativa and dados_pagina_ativa['capa']:
            capa_carregar = f"assets/{dados_pagina_ativa['capa']}"

    # Renderiza a capa centralizada ocupando a largura ideal
    if capa_carregar:
        if os.path.exists(capa_carregar):
            # Cria colunas para centralizar e não deixar a imagem gigante em telas muito largas
            col_img_esq, col_img_centro, col_img_dir = st.columns([1, 4, 1])
            with col_img_centro:
                st.image(capa_carregar, use_container_width=True)
                st.markdown("<br>", unsafe_allow_html=True)

    # --- 2. GRID DE BOTÕES (ABAIXO DA IMAGEM DE CAPA) ---
    # Organizados em 4 colunas para ficarem bem distribuídos horizontalmente
    cols_botoes = st.columns(4)
    
    for i, pagina in enumerate(PAGINAS):
        with cols_botoes[i % 4]:
            temas_premium = ["Santa Ceia", "Mulheres", "Jovens"]
            e_premium = pagina['titulo'] in temas_premium
            label = f"{pagina['icone']}  {pagina['titulo']}"
            
            # Lógica de Bloqueio por Plano
            if e_premium and plano == "START":
                st.button(f"🔒 {pagina['titulo']}", key=f"btn_dash_lock_{pagina['modulo']}", disabled=True, use_container_width=True)
                st.caption("<center style='color:#666;'>Disponível no Premium</center>", unsafe_allow_html=True)
            else:
                if st.button(label, key=f"btn_dash_{pagina['modulo']}", use_container_width=True):
                    st.session_state.pagina_atual = pagina['modulo']
                    st.rerun()
            st.markdown("<br>", unsafe_allow_html=True)

    # --- 3. RENDERIZAÇÃO DOS MODELOS DA PÁGINA SELECIONADA ---
    if st.session_state.pagina_atual:
        st.markdown("---") # Linha divisória elegante
        
        try:
            modulo = importlib.import_module(st.session_state.pagina_atual)
            importlib.reload(modulo) 
            modulo.exibir()
        except Exception as e:
            st.error(f"Erro ao carregar a categoria: {e}")
            
    # --- ÁREA DE LOGOUT ---
    st.markdown("<br><br><br><hr style='border-color: #1f1f1f;'>", unsafe_allow_html=True)
    if st.button("🚪 DESLOGAR E VOLTAR À PÁGINA INICIAL", use_container_width=True, key="btn_logout_dash"):
        st.session_state.logado = False
        st.session_state.pagina_atual = None
        st.rerun()
