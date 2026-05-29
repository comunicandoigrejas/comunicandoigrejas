import streamlit as st
import importlib
import os

# --- MAPEAMENTO DAS PÁGINAS E SUAS RESPECTIVAS CAPAS ---
PAGINAS = [
    {"icone": "⛪", "titulo": "Cultos Gerais",        "modulo": "pages.Cultos_Gerais",        "capa": "Cultos Gerais 08.jpg"},
    {"icone": "🎉", "titulo": "Datas Comemorativas",  "modulo": "pages.Datas_Comemorativas",  "capa": None},
    {"icone": "👨‍👩‍👧‍👦", "titulo": "Culto da Família",     "modulo": "pages.Familia",              "capa": "Culto Familia 08.png"},
    {"icone": "🧔", "titulo": "Culto de Homens",       "modulo": "pages.Homens",               "capa": None},
    {"icone": "🧸", "titulo": "Culto Infantil",         "modulo": "pages.Infantil",             "capa": None},
    {"icone": "⚡", "titulo": "Culto de Jovens",       "modulo": "pages.Jovens",               "capa": None},
    {"icone": "🌸", "titulo": "Culto de Mulheres",     "modulo": "pages.Mulheres",             "capa": None},
    {"icone": "🍷", "titulo": "Culto de Ceia",          "modulo": "pages.Santa_Ceia",           "capa": "Santa Ceia 04.png"},
]

def exibir():
    # --- CSS DOS BOTÕES VERDES DE ACESSO ---
    with open("style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
        
    st.markdown("""
        <style>
        div.stButton > button {
            background-color: #2da042 !important; 
            color: #ffffff !important;
            font-weight: bold !important;
            border-radius: 6px !important;
            border: none !important;
            height: 48px !important;
            transition: background-color 0.2s !important;
            margin-top: 5px !important;
        }
        div.stButton > button:hover {
            background-color: #3ccb57 !important;
        }
        </style>
    """, unsafe_allow_html=True)

    # Inicializa a variável de controle se ela não existir
    if 'pagina_atual' not in st.session_state:
        st.session_state.pagina_atual = None

    # --- FLUXO 1: SE NENHUMA PÁGINA FOI SELECIONADA, MOSTRA A VITRINE DE CAPAS ---
    if st.session_state.pagina_atual is None:
        st.markdown("<h1 class='gradient-title'>🏠 Dashboard</h1>", unsafe_allow_html=True)
        nome = st.session_state.get('nome_usuario', 'Irmão')
        plano = st.session_state.get('plano', 'PREMIUM')
        st.success(f"👋 Olá, **{nome}** | BEM VINDO AO PLANO: **{plano}**")
        st.markdown("<br> 🎨 ESCOLHA UM TEMA PARA ACESSAR AS ARTES:", unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)

        # Grid em 3 colunas para exibir os cards de capas + botões
        cols_vitrine = st.columns(3)
        
        for i, pagina in enumerate(PAGINAS):
            with cols_vitrine[i % 3]:
                # 1. Exibe a imagem de capa ACIMA do botão verde
                if pagina['capa']:
                    caminho_capa = f"assets/{pagina['capa']}"
                    if os.path.exists(caminho_capa):
                        st.image(caminho_capa, use_container_width=True)
                    else:
                        st.markdown(f"<div style='background-color: #1a1a1a; height: 180px; display: flex; align-items: center; justify-content: center; border-radius: 8px; color: #555; font-size:0.85rem; border: 1px dashed #333;'>🖼️ Capa: {pagina['titulo']}</div>", unsafe_allow_html=True)
                else:
                    st.markdown(f"<div style='background-color: #1a1a1a; height: 180px; display: flex; align-items: center; justify-content: center; border-radius: 8px; color: #444; font-size:0.85rem; border: 1px dashed #222;'>🖼️ Em breve: {pagina['titulo']}</div>", unsafe_allow_html=True)
                
                # 2. Exibe o Botão Verde LOGO ABAIXO da capa
                temas_premium = ["Santa Ceia", "Mulheres", "Jovens"]
                e_premium = pagina['titulo'] in temas_premium
                label = f"{pagina['icone']}  Acessar {pagina['titulo']}"
                
                if e_premium and plano == "START":
                    st.button(f"🔒 {pagina['titulo']}", key=f"btn_v_lock_{pagina['modulo']}", disabled=True, use_container_width=True)
                    st.caption("<center style='color:#666; font-size:0.8rem;'>Disponível no Premium</center>", unsafe_allow_html=True)
                else:
                    if st.button(label, key=f"btn_v_{pagina['modulo']}", use_container_width=True):
                        st.session_state.pagina_atual = pagina['modulo']
                        st.rerun() # Recarrega limpando a vitrine e indo para a página interna
                
                st.markdown("<br><br>", unsafe_allow_html=True)

    # --- FLUXO 2: SE UMA PÁGINA FOI SELECIONADA,DIRECIONA TOTALMENTE PARA ELA ---
    else:
        # Botão elegante para voltar ao menu principal de categorias
        if st.button("⬅️ VOLTAR PARA CATEGORIAS", use_container_width=True):
            st.session_state.pagina_atual = None
            st.rerun()
            
        st.markdown("<br>", unsafe_allow_html=True)
        
        try:
            modulo = importlib.import_module(st.session_state.pagina_atual)
            importlib.reload(modulo) 
            modulo.exibir() # Executa os modelos da página correspondente
        except Exception as e:
            st.error(f"Erro ao carregar a página: {e}")

    # --- RODAPÉ DE LOGOUT ---
    st.markdown("<br><br><br><hr style='border-color: #1f1f1f;'>", unsafe_allow_html=True)
    if st.button("🚪 DESLOGAR DO SISTEMA", use_container_width=True, key="btn_logout_final"):
        st.session_state.logado = False
        st.session_state.pagina_atual = None
        st.rerun()
