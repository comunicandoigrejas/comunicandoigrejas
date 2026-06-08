import streamlit as st
import importlib
import sys
import os

# --- CONFIGURAÇÃO DE ROTAS E DIRETÓRIOS ---
PASTA_CANVA = "pages.templates_canva"

PAGINAS_CANVA = [
    {"icone": "⬜", "titulo": "Ação Social",            "modulo": f"{PASTA_CANVA}.Acao_Social",           "capa": "Acao 03.png"},
    {"icone": "📅", "titulo": "Agenda",                "modulo": f"{PASTA_CANVA}.Agenda",                "capa": "Agenda 01.png"},
    {"icone": "🔄", "titulo": "Atualizações Semanais",  "modulo": f"{PASTA_CANVA}.Atualizacoes_Semanais",  "capa": "Atualizacoes_Semanais.png"},
    {"icone": "🌊", "titulo": "Batismo",               "modulo": f"{PASTA_CANVA}.Batismo",               "capa": "Batismo.png"},
    {"icone": "📢", "titulo": "Campanhas",             "modulo": f"{PASTA_CANVA}.Campanhas",             "capa": "Campanha 01.png"},
    {"icone": "⛪", "titulo": "Cultos Gerais",          "modulo": f"{PASTA_CANVA}.Cultos_Gerais",          "capa": "Cultos Gerais 08.jpg"},
    {"icone": "🏡", "titulo": "Culto de Célula",        "modulo": f"{PASTA_CANVA}.Culto_Celular",         "capa": "Culto_Celular.png"},
    {"icone": "👨‍👩‍👧‍👦", "titulo": "Culto da Família",       "modulo": f"{PASTA_CANVA}.Familia",               "capa": "Culto Familia 08.png"},
    {"icone": "🧔", "titulo": "Culto de Homens",        "modulo": f"{PASTA_CANVA}.Homens",                "capa": "Homens 01.png"},
    {"icone": "🧸", "titulo": "Culto Infantil",          "modulo": f"{PASTA_CANVA}.Infantil",              "capa": "Infantil 01.png"},
    {"icone": "⚡", "titulo": "Culto de Jovens",        "modulo": f"{PASTA_CANVA}.Jovens",                "capa": "Jovens 06.png"},
    {"icone": "🌍", "titulo": "Culto de Missões",       "modulo": f"{PASTA_CANVA}.Culto_Missoes",         "capa": "Culto_Missoes.png"},
    {"icone": "🌸", "titulo": "Culto de Mulheres",      "modulo": f"{PASTA_CANVA}.Mulheres",              "capa": "Mulher 09.png"},
    {"icone": "🍷", "titulo": "Culto de Ceia",          "modulo": f"{PASTA_CANVA}.Santa_Ceia",             "capa": "Santa Ceia 01.png"},
    {"icone": "🎉", "titulo": "Datas Comemorativas",    "modulo": f"{PASTA_CANVA}.Datas_Comemorativas",    "capa": "Comemorativa 14.png"},
    {"icone": "💍", "titulo": "Encontro de Casais",     "modulo": f"{PASTA_CANVA}.Encontro_Casais",       "capa": "Encontro_Casais.png"},
    {"icone": "🎪", "titulo": "Eventos",               "modulo": f"{PASTA_CANVA}.Eventos",               "capa": "Eventos.png"},
    {"icone": "ℹ️", "titulo": "Informações Gerais",     "modulo": f"{PASTA_CANVA}.Informacoes_Gerais",    "capa": "Informacoes_Gerais.png"},
    {"icone": "🎨", "titulo": "Outros Temas",           "modulo": f"{PASTA_CANVA}.Outros_Temas",          "capa": "Outros_Temas.png"},
]

PORTAIS = [
    {"titulo": "TEMPLATES CANVA",            "chave": "templates_canva", "icone": "🎨", "capa": "capa_canva.png",        "modulo": None},
    {"titulo": "BÔNUS",                      "chave": "bonus",           "icone": "🎁", "capa": "capa_bonus.png",        "modulo": "bonus"},
    {"titulo": "FERRAMENTAS",                "chave": "ferramentas",     "icone": "🛠️", "capa": "capa_ferramentas.png",   "modulo": "ferramentas"},
    {"titulo": "KIT MINISTÉRIO INFANTIL",     "chave": "kit_infantil",    "icone": "🧸", "capa": "capa_kit_infantil.png",  "modulo": "pages.kit_infantil.inicial"},
    {"titulo": "KIT SECRETARIA DE IGREJA",   "chave": "secretaria",      "icone": "📁", "capa": "capa_secretaria.png",   "modulo": "pages.secretaria.inicial"},
    {"titulo": "SERMÃOS PRONTOS",            "chave": "sermoes",         "icone": "📖", "capa": "capa_sermoes.png",       "modulo": "pages.sermoes.inicial"},
]

def renderizar_css_botoes():
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
        }
        div.stButton > button:hover {
            background-color: #3ccb57 !important;
        }
        </style>
    """, unsafe_allow_html=True)

def carregar_modulo_dinamico(caminho_modulo):
    try:
        if caminho_modulo in sys.modules:
            del sys.modules[caminho_modulo]
            
        modulo = importlib.import_module(caminho_modulo)
        
        if hasattr(modulo, "exibir"):
            modulo.exibir()
        else:
            st.error(f"❌ O módulo {caminho_modulo} não possui a função exibir().")
            
    except ModuleNotFoundError:
        st.error(f"❌ Módulo não encontrado: **{caminho_modulo}**")
        st.info("💡 Dica: Crie o arquivo correspondente para que o botão funcione.")
    except Exception as e:
        st.error(f"❌ Erro ao carregar **{caminho_modulo}**")
        with st.expander("Detalhes do erro"):
            st.exception(e)

def exibir():
    renderizar_css_botoes()

    if 'portal_atual' not in st.session_state:
        st.session_state.portal_atual = None
    if 'sub_pagina_canva' not in st.session_state:
        st.session_state.sub_pagina_canva = None

    # MENU PRINCIPAL
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
                    st.markdown(f"""
                        <div style='background-color: #0c0c0c; height: 160px; display: flex; 
                        align-items: center; justify-content: center; border-radius: 8px; 
                        color: #777; font-size:0.9rem; border: 1px solid #333; 
                        font-weight: bold; text-align: center; padding: 10px;'>
                        {portal['icone']}<br>{portal['titulo']}
                        </div>
                    """, unsafe_allow_html=True)
                
                if st.button(f"ACESSAR {portal['titulo']}", key=f"btn_p_{portal['chave']}", use_container_width=True):
                    st.session_state.portal_atual = portal['chave']
                    st.rerun()

    # VITRINE TEMPLATES CANVA
    elif st.session_state.portal_atual == "templates_canva" and st.session_state.sub_pagina_canva is None:
        if st.button("⬅️ VOLTAR AO MENU PRINCIPAL", use_container_width=True):
            st.session_state.portal_atual = None
            st.rerun()
            
        st.markdown("<h2 style='text-align: center; color: white; font-weight: bold;'>🎨 VITRINE DE TEMPLATES CANVA</h2>", unsafe_allow_html=True)

        cols_canva = st.columns(3)
        for i, pagina in enumerate(PAGINAS_CANVA):
            with cols_canva[i % 3]:
                caminho_capa = f"assets/{pagina['capa']}" if pagina.get('capa') else ""
                
                # CORREÇÃO CRUCIAL: Se a capa não existir fisicamente, o app não quebra e desenha o card cinza com o ícone!
                if caminho_capa and os.path.exists(caminho_capa):
                    st.image(caminho_capa, use_container_width=True)
                else:
                    st.markdown(f"""
                        <div style='background-color: #1a1a1a; height: 180px; display: flex; 
                        align-items: center; justify-content: center; border-radius: 8px; 
                        color: #eee; font-size:1rem; border: 1px dashed #444; font-weight: bold;
                        text-align: center; padding: 20px; margin-bottom: 5px;'>
                        <span style='font-size: 2rem;'>{pagina['icone']}</span><br><br>{pagina['titulo']}
                        </div>
                    """, unsafe_allow_html=True)
                
                if st.button(f"Acessar {pagina['titulo']}", key=f"btn_c_{i}", use_container_width=True):
                    st.session_state.sub_pagina_canva = pagina['modulo']
                    st.rerun()

    # PÁGINA INTERNA DE TEMPLATES
    elif st.session_state.portal_atual == "templates_canva" and st.session_state.sub_pagina_canva is not None:
        if st.button("⬅️ VOLTAR PARA TEMPLATES CANVA", use_container_width=True):
            st.session_state.sub_pagina_canva = None
            st.rerun()
        carregar_modulo_dinamico(st.session_state.sub_pagina_canva)

    # OUTROS PORTAIS
    else:
        if st.button("⬅️ VOLTAR AO MENU PRINCIPAL", use_container_width=True):
            st.session_state.portal_atual = None
            st.rerun()
        st.warning("🔧 Este módulo ainda está em desenvolvimento.")

    # LOGOUT
    st.markdown("<br><br><br><hr style='border-color: #1f1f1f;'>", unsafe_allow_html=True)
    if st.button("🚪 DESLOGAR DO SISTEMA", use_container_width=True):
        for key in list(st.session_state.keys()):
            if key not in ['logado']:
                del st.session_state[key]
        st.session_state.logado = False
        st.rerun()

if __name__ == "__main__":
    exibir()