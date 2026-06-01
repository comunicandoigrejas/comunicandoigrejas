import streamlit as st
import importlib
import os

# --- MAPEAMENTO DAS SUBCATEGORIAS DO CANVA (VITRINE INTERNA) ---
PAGINAS_CANVA = [
    {"icone": "⛪", "titulo": "Cultos Gerais",        "modulo": "pages.Cultos_Gerais",        "capa": "Cultos Gerais 08.jpg"},
    {"icone": "🎉", "titulo": "Datas Comemorativas",  "modulo": "pages.Datas_Comemorativas",  "capa": None},
    {"icone": "👨‍👩‍👧‍👦", "titulo": "Culto da Família",     "modulo": "pages.Familia",              "capa": "Culto Familia 08.png"},
    {"icone": "🧔", "titulo": "Culto de Homens",       "modulo": "pages.Homens",               "capa": None},
    {"icone": "🧸", "titulo": "Culto Infantil",         "modulo": "pages.Infantil",             "capa": None},
    {"icone": "⚡", "titulo": "Culto de Jovens",       "modulo": "pages.Jovens",               "capa": None},
    {"icone": "🌸", "titulo": "Culto de Mulheres",     "modulo": "pages.Mulheres",             "capa": None},
    {"icone": "🍷", "titulo": "Culto de Ceia",          "modulo": "pages.Santa_Ceia",           "capa": None},
]

# --- MAPEAMENTO DOS 6 GRANDES PORTAIS DO DASHBOARD PRINCIPAL ---
PORTAIS = [
    {"titulo": "TEMPLATES CANVA",            "chave": "templates_canva", "icone": "🎨", "capa": "capa_canva.jpg"},
    {"titulo": "BÔNUS",                      "chave": "bonus",           "icone": "🎁", "capa": "capa_bonus.jpg"},
    {"titulo": "FERRAMENTAS",                "chave": "ferramentas",     "icone": "🛠️", "capa": "capa_ferramentas.jpg"},
    {"titulo": "KIT MINISTÉRIO INFANTIL",     "chave": "kit_infantil",    "icone": "🧸", "capa": "capa_kit_infantil.jpg"},
    {"titulo": "KIT SECRETARIA DE IGREJA",   "chave": "secretaria",      "icone": "📁", "capa": "capa_secretaria.jpg"},
    {"titulo": "SERMÃOS PRONTOS",            "chave": "sermoes",         "icone": "📖", "capa": "capa_sermoes.jpg"},
]

def exibir():
    # --- CSS DOS BOTÕES VERDES DE ACESSO ---
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

    # Inicializa os estados de navegação se não existirem
    if 'portal_atual' not in st.session_state:
        st.session_state.portal_atual = None
    if 'sub_pagina_canva' not in st.session_state:
        st.session_state.sub_pagina_canva = None

    # --- NÍVEL 1: MENU PRINCIPAL DO DASHBOARD (OS 6 GRANDES PORTAIS) ---
    if st.session_state.portal_atual is None:
        st.markdown("<h1 style='color: white;'>🏠 Painel Inicial</h1>", unsafe_allow_html=True)
        nome = st.session_state.get('nome_usuario', 'Irmão')
        # Definindo um plano padrão caso não esteja definido no login
        if 'plano' not in st.session_state:
            st.session_state.plano = "PREMIUM"
        
        st.success(f"👋 Olá, **{nome}** | Seu acesso está liberado!")
        st.markdown("<br>### 🚀 Acesse os módulos do seu portal:", unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)

        # Grade de 3 colunas para os 6 portais principais
        cols_portais = st.columns(3)
        
        for i, portal in enumerate(PORTAIS):
            with cols_portais[i % 3]:
                # Imagem de capa do Portal
                caminho_capa = f"assets/{portal['capa']}"
                if os.path.exists(caminho_capa):
                    st.image(caminho_capa, use_container_width=True)
                else:
                    st.markdown(f"<div style='background-color: #0c0c0c; height: 160px; display: flex; align-items: center; justify-content: center; border-radius: 8px; color: #777; font-size:0.9rem; border: 1px solid #333; font-weight: bold; text-align: center; padding: 10px;'>{portal['icone']}<br>{portal['titulo']}</div>", unsafe_allow_html=True)
                
                # Botão verde logo abaixo da capa
                if st.button(f"ACESSAR MÓDULO", key=f"btn_portal_{portal['chave']}", use_container_width=True):
                    st.session_state.portal_atual = portal['chave']
                    st.rerun()
                
                st.markdown("<br><br>", unsafe_allow_html=True)

    # --- NÍVEL 2: DENTRO DO PORTAL "TEMPLATES CANVA" (VITRINE DE ARTES) ---
    elif st.session_state.portal_atual == "templates_canva" and st.session_state.sub_pagina_canva is None:
        if st.button("⬅️ VOLTAR AO MENU PRINCIPAL", use_container_width=True):
            st.session_state.portal_atual = None
            st.rerun()
            
        st.markdown("<h2 style='text-align: center; color: white; font-weight: bold;'>🎨 VITRINE DE TEMPLATES CANVA</h2>", unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)

        # Grade de 3 colunas para as subcategorias de artes do Canva
        cols_canva = st.columns(3)
        
        for i, pagina in enumerate(PAGINAS_CANVA):
            with cols_canva[i % 3]:
                # Imagem de capa da categoria
                if pagina['capa']:
                    caminho_capa = f"assets/{pagina['capa']}"
                    if os.path.exists(caminho_capa):
                        st.image(caminho_capa, use_container_width=True)
                    else:
                        st.markdown(f"<div style='background-color: #1a1a1a; height: 180px; display: flex; align-items: center; justify-content: center; border-radius: 8px; color: #555; font-size:0.85rem; border: 1px dashed #333;'>🖼️ Capa: {pagina['titulo']}</div>", unsafe_allow_html=True)
                else:
                    st.markdown(f"<div style='background-color: #1a1a1a; height: 180px; display: flex; align-items: center; justify-content: center; border-radius: 8px; color: #444; font-size:0.85rem; border: 1px dashed #222;'>🖼️ Em breve: {pagina['titulo']}</div>", unsafe_allow_html=True)
                
                # Botão verde para acessar as artes específicas
                if st.button(f"{pagina['icone']}  Acessar {pagina['titulo']}", key=f"btn_sub_{pagina['modulo']}", use_container_width=True):
                    st.session_state.sub_pagina_canva = pagina['modulo']
                    st.rerun()
                
                st.markdown("<br><br>", unsafe_allow_html=True)

    # --- NÍVEL 3: DENTRO DE UMA PÁGINA ESPECÍFICA DO CANVA ---
    elif st.session_state.portal_atual == "templates_canva" and st.session_state.sub_pagina_canva is not None:
        if st.button("⬅️ VOLTAR PARA TEMPLATES CANVA", use_container_width=True):
            st.session_state.sub_pagina_canva = None
            st.rerun()
            
        st.markdown("<br>", unsafe_allow_html=True)
        try:
            modulo = importlib.import_module(st.session_state.sub_pagina_canva)
            importlib.reload(modulo) 
            modulo.exibir()
        except Exception as e:
            st.error(f"Erro ao carregar a página de artes: {e}")

    # --- PORTAIS ADICIONAIS: BÔNUS, FERRAMENTAS, KITS, ETC. ---
    else:
        if st.button("⬅️ VOLTAR AO MENU PRINCIPAL", use_container_width=True):
            st.session_state.portal_atual = None
            st.rerun()
            
        st.markdown(f"<br><h2 style='text-align: center; color: white;'>{st.session_state.portal_atual.upper().replace('_', ' ')}</h2>", unsafe_allow_html=True)
        st.info("Área em desenvolvimento. Em breve todos os materiais exclusivos estarão disponíveis aqui, abençoado!")

    # --- RODAPÉ DE LOGOUT DE SEGURANÇA ---
    st.markdown("<br><br><br><hr style='border-color: #1f1f1f;'>", unsafe_allow_html=True)
    if st.button("🚪 DESLOGAR DO SISTEMA", use_container_width=True, key="btn_logout_portal"):
        st.session_state.logado = False
        st.session_state.portal_atual = None
        st.session_state.sub_pagina_canva = None
        st.rerun()
