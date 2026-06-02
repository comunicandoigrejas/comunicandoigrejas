import streamlit as st
import importlib
import sys
import os

# --- CONFIGURAÇÃO DE ROTAS E DIRETÓRIOS ---
PASTA_CANVA = "pages.templates_canva"

PAGINAS_CANVA = [
    {"icone": "⛪", "titulo": "Cultos Gerais",        "modulo": f"{PASTA_CANVA}.Cultos_Gerais",        "capa": "Cultos Gerais 08.jpg"},
    {"icone": "🎉", "titulo": "Datas Comemorativas",  "modulo": f"{PASTA_CANVA}.Datas_Comemorativas",  "capa": None},
    {"icone": "👨‍👩‍👧‍👦", "titulo": "Culto da Família",     "modulo": f"{PASTA_CANVA}.Familia",              "capa": "Culto Familia 08.png"},
    {"icone": "🧔", "titulo": "Culto de Homens",       "modulo": f"{PASTA_CANVA}.Homens",               "capa": None},
    {"icone": "🧸", "titulo": "Culto Infantil",         "modulo": f"{PASTA_CANVA}.Infantil",             "capa": None},
    {"icone": "⚡", "titulo": "Culto de Jovens",       "modulo": f"{PASTA_CANVA}.Jovens",               "capa": None},
    {"icone": "🌸", "titulo": "Culto de Mulheres",     "modulo": f"{PASTA_CANVA}.Mulheres",             "capa": None},
    {"icone": "🍷", "titulo": "Culto de Ceia",          "modulo": f"{PASTA_CANVA}.Santa_Ceia",           "capa": None},
]

PORTAIS = [
    {"titulo": "TEMPLATES CANVA",            "chave": "templates_canva", "icone": "🎨", "capa": "capa_canva.jpg",        "modulo": None},
    {"titulo": "BÔNUS",                      "chave": "bonus",           "icone": "🎁", "capa": "capa_bonus.jpg",        "modulo": "pages.bonus.inicial"},
    {"titulo": "FERRAMENTAS",                "chave": "ferramentas",     "icone": "🛠️", "capa": "capa_ferramentas.jpg",   "modulo": "pages.ferramentas.inicial"},
    {"titulo": "KIT MINISTÉRIO INFANTIL",     "chave": "kit_infantil",    "icone": "🧸", "capa": "capa_kit_infantil.jpg",  "modulo": "pages.kit_infantil.inicial"},
    {"titulo": "KIT SECRETARIA DE IGREJA",   "chave": "secretaria",      "icone": "📁", "capa": "capa_secretaria.jpg",   "modulo": "pages.secretaria.inicial"},
    {"titulo": "SERMÃOS PRONTOS",            "chave": "sermoes",         "icone": "📖", "capa": "capa_sermoes.jpg",       "modulo": "pages.sermoes.inicial"},
]

def renderizar_css_botoes():
    """Aplica a estilização limpa para os botões padrões do sistema."""
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

def carregar_modulo_dinamico(caminho_modulo):
    """Importa e executa o módulo limpando o cache para evitar travamentos."""
    try:
        # Se o módulo já foi carregado antes, remove do cache para forçar atualização limpa
        if caminho_modulo in sys.modules:
            del sys.modules[caminho_modulo]
            
        modulo = importlib.import_module(caminho_modulo)
        # Executa a função exibir() de dentro do arquivo alvo (ex: Cultos_Gerais.py)
        if hasattr(modulo, "exibir"):
            modulo.exibir()
        else:
            st.error(f"O módulo {caminho_modulo} não possui a função exibir().")
    except Exception as e:
        st.error(f"Erro ao carregar o módulo interno: {e}")

def exibir():
    renderizar_css_botoes()

    # Inicialização dos estados de navegação no session_state
    if 'portal_atual' not in st.session_state:
        st.session_state.portal_atual = None
    if 'sub_pagina_canva' not in st.session_state:
        st.session_state.sub_pagina_canva = None

    # --- NÍVEL 1: MENU PRINCIPAL ---
    if st.session_state.portal_atual is None:
        st.markdown("<h1 style='color: white;'>🏠 Painel Inicial</h1>", unsafe_allow_html=True)
        nome = st.session_state.get('nome_usuario', 'Irmão')
        
        st.success(f"👋 Olá, **{nome}** | Seu acesso está liberado!")
        st.markdown("### 🚀 Acesse os módulos do seu portal:")

        cols_portais = st.columns(3)
        for i, portal in enumerate(PORTAIS):
            with cols_portais[i % 3]:
                caminho_capa = f"assets/{portal['capa']}"
                if os.path.exists(caminho_capa):
                    st.image(caminho_capa, use_container_width=True)
                else:
                    st.markdown(f"<div style='background-color: #0c0c0c; height: 160px; display: flex; align-items: center; justify-content: center; border-radius: 8px; color: #777; font-size:0.9rem; border: 1px solid #333; font-weight: bold; text-align: center; padding: 10px;'>{portal['icone']}<br>{portal['titulo']}</div>", unsafe_allow_html=True)
                
                if st.button(f"ACESSAR {portal['titulo']}", key=f"btn_p_{portal['chave']}", use_container_width=True):
                    st.session_state.portal_atual = portal['chave']
                    st.rerun()

    # --- NÍVEL 2: VITRINE DO PORTAL "TEMPLATES CANVA" ---
    elif st.session_state.portal_atual == "templates_canva" and st.session_state.sub_pagina_canva is None:
        if st.button("⬅️ VOLTAR AO MENU PRINCIPAL", use_container_width=True):
            st.session_state.portal_atual = None
            st.rerun()
            
        st.markdown("<h2 style='text-align: center; color: white; font-weight: bold;'>🎨 VITRINE DE TEMPLATES CANVA</h2>", unsafe_allow_html=True)

        cols_canva = st.columns(3)
        for i, pagina in enumerate(PAGINAS_CANVA):
            with cols_canva[i % 3]:
                caminho_capa = f"assets/{pagina['capa']}" if pagina['capa'] else ""
                if caminho_capa and os.path.exists(caminho_capa):
                    st.image(caminho_capa, use_container_width=True)
                else:
                    st.markdown(f"<div style='background-color: #1a1a1a; height: 180px; display: flex; align-items: center; justify-content: center; border-radius: 8px; color: #555; font-size:0.85rem; border: 1px dashed #333;'>{pagina['icone']}<br>Capa: {pagina['titulo']}</div>", unsafe_allow_html=True)
                
                if st.button(f"Acessar {pagina['titulo']}", key=f"btn_c_{pagina['modulo']}", use_container_width=True):
                    st.session_state.sub_pagina_canva = pagina['modulo']
                    st.rerun()

    # --- NÍVEL 3: DENTRO DE UMA PÁGINA DE ARTES DO CANVA ---
    elif st.session_state.portal_atual == "templates_canva" and st.session_state.sub_pagina_canva is not None:
        if st.button("⬅️ VOLTAR PARA TEMPLATES CANVA", use_container_width=True):
            st.session_state.sub_pagina_canva = None
            st.rerun()
            
        carregar_modulo_dinamico(st.session_state.sub_pagina_canva)

    # --- NÍVEL 2 PÁGINAS ADICIONAIS (BÔNUS, FERRAMENTAS, ETC.) ---
    else:
        if st.button("⬅️ VOLTAR AO MENU PRINCIPAL", use_container_width=True):
            st.session_state.portal_atual = None
            st.rerun()
            
        info_portal = next((p for p in PORTAIS if p["chave"] == st.session_state.portal_atual), None)
        
        if info_portal and info_portal["modulo"]:
            carregar_modulo_dinamico(info_portal["modulo"])
        else:
            st.warning("Módulo não configurado ou arquivo inicial não encontrado.")

    # --- RODAPÉ DE LOGOUT DE SEGURANÇA ---
    st.markdown("<br><br><br><hr style='border-color: #1f1f1f;'>", unsafe_allow_html=True)
    if st.button("🚪 DESLOGAR DO SISTEMA", use_container_width=True, key="btn_logout_portal"):
        st.session_state.logado = False
        st.session_state.portal_atual = None
        st.session_state.sub_pagina_canva = None
        st.rerun()

# --- EXECUÇÃO DO ARQUIVO ---
if __name__ == "__main__":
    exibir()
