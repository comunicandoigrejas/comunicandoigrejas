import streamlit as st
import os

def exibir():
    st.markdown("<h2 style='text-align: center; color: white; font-weight: bold;'>🌍 MODELOS: CULTO DE MISSÕES</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #888; font-size: 0.95rem;'>Templates profissionais criados para conscientização missionária, cultos de missões e envio de relatórios.</p>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    # CSS padrão para os botões brancos das artes (Identidade Comunicando Igrejas)
    st.markdown("""
        <style>
        div.stButton > button {
            background-color: #ffffff !important;
            color: #000000 !important;
            font-weight: bold !important;
            font-size: 0.85rem !important;
            border-radius: 4px !important;
            border: none !important;
            padding: 6px 12px !important;
            transition: background-color 0.2s !important;
        }
        div.stButton > button:hover {
            background-color: #e5e5e5 !important;
            color: #000000 !important;
        }
        </style>
    """, unsafe_allow_html=True)

    # Lista estruturada com os links fornecidos de Feed e Story (Nomes: Missões 01.png a Missões 09.png)
    artes_missoes = [
        {"nome": "Missoes 01.png", "feed": "https://canva.link/sdcxncap1uxadis", "story": "https://canva.link/tawlnztf97w4dxq"},
        {"nome": "Missoes 02.png", "feed": "https://canva.link/nt8r32mef186ihg", "story": "https://canva.link/9cg6nff9wmf4ibx"},
        {"nome": "Missoes 03.png", "feed": "https://canva.link/s9kewhit4oji96b", "story": "https://canva.link/s47mxq1gnchv78d"},
        {"nome": "Missoes 04.png", "feed": "https://canva.link/2lp7i9tjpmw0xlh", "story": "https://canva.link/kbzhy3hobztg6w7"},
        {"nome": "Missoes 05.png", "feed": "https://canva.link/rtn6s4fq2z3wi5l", "story": "https://canva.link/bn3ktogd7npzw0y"},
        {"nome": "Missoes 06.png", "feed": "https://canva.link/4e5bwf41fmbxy2g", "story": "https://canva.link/hm4frrnkf2ygg8a"},
        {"nome": "Missoes 07.png", "feed": "https://canva.link/xmht1f26jm10jxu", "story": "https://canva.link/sl74ebk440d409f"},
        {"nome": "Missoes 08.png", "feed": "https://canva.link/5pzmoqki4pf7htt", "story": "https://canva.link/3bfer7y7x4pt1jw"},
        {"nome": "Missoes 09.png", "feed": "https://canva.link/awh9yngmpglb35q", "story": "https://canva.link/ec2nu4bsin6odoc"},
    ]

    # Grid organizada em 3 colunas de exibição
    col1, col2, col3 = st.columns(3)

    for idx, arte in enumerate(artes_missoes):
        # Distribuição uniforme dos cards pelas colunas
        coluna_alvo = col1 if idx % 3 == 0 else (col2 if idx % 3 == 1 else col3)
        
        with coluna_alvo:
            caminho_imagem = f"assets/{arte['nome']}"
            
            # Validação para verificar se a prévia da imagem física existe na pasta assets/
            if os.path.exists(caminho_imagem):
                st.image(caminho_imagem, use_container_width=True)
            else:
                # Card alternativo amigável caso a imagem física não esteja na pasta assets/
                st.markdown(f"<div style='background-color: #0c0c0c; padding: 120px 10px; text-align: center; border-radius: 8px; color: #555; font-size:0.85rem; border: 1px solid #222;'>🖼️ {arte['nome']}<br>(Não encontrada em assets/)</div>", unsafe_allow_html=True)
            
            # Botões de redirecionamento direto para os templates do Canva
            b_feed, b_story = st.columns(2)
            with b_feed:
                st.link_button("📱 FEED", arte["feed"], use_container_width=True)
            with b_story:
                st.link_button("📐 STORY", arte["story"], use_container_width=True)
            
            st.markdown("<br>", unsafe_allow_html=True)