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
            margin-top: 8px !important;
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
    st.markdown("<br><br>", unsafe_allow_html=True)

    if 'pagina_atual' not in st.session_state:
        st.session_state.pagina_atual = None

    # --- GRID DE VITRINE (IMAGEM + BOTÃO LOGO ABAIXO) ---
    # Organizados em colunas para criar uma galeria de temas linda
    cols_vitrine = st.columns(3) # Exibe de 3 em 3 categorias por linha para dar um excelente destaque às capas
    
    for i, pagina in enumerate(PAGINAS):
        with cols_vitrine[i % 3]:
            # 1. Busca e renderiza a imagem da capa acima do botão
            if pagina['capa']:
                caminho_capa = f"assets/{pagina['capa']}"
                if os.path.exists(caminho_capa):
                    st.image(caminho_capa, use_container_width=True)
                else:
                    # Fallback elegante caso a imagem ainda não esteja na pasta assets
                    st.markdown(f"<div style='background-color: #111; height: 180px; display: flex; align-items: center; justify-content: center; border-radius: 6px; border: 1px dashed #333; color: #555; font-size: 0.85rem;'>🖼️ Capa {pagina['titulo']}</div>", unsafe_allow_html=True)
            else:
                # Caso a categoria não tenha capa definida ainda, deixa um espaço ou mockup padronizado
                st.markdown(f"<div style='background-color: #111; height: 180px; display: flex; align-items: center; justify-content: center; border-radius: 6px; border: 1px dashed #333; color: #444; font-size: 0.85rem;'>🖼️ Breve - Capa {pagina['titulo']}</div>", unsafe_allow_html=True)
            
            # 2. Configuração do Botão Verde posicionado logo abaixo da sua respectiva imagem
            temas_premium = ["Santa Ceia", "Mulheres", "Jovens"]
            e_premium = pagina['titulo'] in temas_premium
            label = f"{pagina['icone']}  {pagina['titulo']}"
            
            if e_premium and plano == "START":
                st.button(f"🔒 {pagina['titulo']}", key=f"btn_vitrine_lock_{pagina['modulo']}", disabled=True, use_container_width=True)
                st.caption("<center style='color:#666;'>Disponível no Premium</center>", unsafe_allow_html=True)
            else:
                if st.button(label, key=f"btn_vitrine_{pagina['modulo']}", use_container_width=True):
                    st.session_state.pagina_atual = pagina['modulo']
                    st.rerun()
            
            st.markdown("<br><br>", unsafe_allow_html=True)

    # --- 3. RENDERIZAÇÃO DOS MODELOS DA PÁGINA SELECIONADA ---
    # Quando o irmão clicar em qualquer botão verde da vitrine, os modelos abrem logo aqui abaixo
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
