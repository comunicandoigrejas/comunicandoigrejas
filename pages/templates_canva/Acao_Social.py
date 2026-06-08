import streamlit as st
import os

def exibir():
    st.markdown("<h2 style='text-align: center; color: white; font-weight: bold;'>⬜ MODELOS DISPONÍVEIS: AÇÃO SOCIAL</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #888; font-size: 0.95rem;'>Escolha o formato desejado para abrir o modelo editável diretamente no seu Canva.</p>", unsafe_allow_html=True)
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

    # Lista estruturada com as 9 mídias de Ação Social e seus respectivos links de Feed e Story (Formato PNG)
    artes_acao = [
        {"nome": "Ação 01.png", "feed": "https://canva.link/uew46jomhs413tk", "story": "https://canva.link/650id0yndi1cwez"},
        {"nome": "Ação 02.png", "feed": "https://canva.link/yw7ssns1snpyjo3", "story": "https://canva.link/bgfltnecs11kmoi"},
        {"nome": "Ação 03.png", "feed": "https://canva.link/07z9f9g4ihyio2g", "story": "https://canva.link/1f5rcnadil7z0v7"},
        {"nome": "Ação 04.png", "feed": "https://canva.link/knnu5mg8b0qvrcw", "story": "https://canva.link/mjld03s9p0kjgsw"},
        {"nome": "Ação 05.png", "feed": "https://canva.link/uk4xmq11ra01a5r", "story": "https://canva.link/j1d0shcg2vwijlx"},
        {"nome": "Ação 06.png", "feed": "https://canva.link/s1r5j071gjnuwca", "story": "https://canva.link/m7a7xh2jrt1m5zr"},
        {"nome": "Ação 07.png", "feed": "https://canva.link/lkt98biqwthzbx8", "story": "https://canva.link/l330pqmxkuho5q6"},
        {"nome": "Ação 08.png", "feed": "https://canva.link/t8z7ihf3a49vwtu", "story": "https://canva.link/ic93afjnzjiaezn"},
        {"nome": "Ação 09.png", "feed": "https://canva.link/g5h6nz66556bijr", "story": "https://canva.link/h9v99y5k8fcjyd3"},
    ]

    # Grid organizada em 3 colunas de exibição
    col1, col2, col3 = st.columns(3)

    for idx, arte in enumerate(artes_acao):
        # Distribuição uniforme dos cards pelas colunas
        coluna_alvo = col1 if idx % 3 == 0 else (col2 if idx % 3 == 1 else col3)
        
        with coluna_alvo:
            caminho_imagem = f"assets/{arte['nome']}"
            
            # Validação segura para exibir o arquivo .png da pasta assets/ com o nome acentuado conforme solicitado
            if os.path.exists(caminho_imagem):
                st.image(caminho_imagem, use_container_width=True)
            else:
                # Card alternativo amigável caso a imagem física não esteja na pasta assets/
                st.markdown(f"<div style='background-color: #1a1a1a; padding: 120px 10px; text-align: center; border-radius: 8px; color: #555; font-size:0.85rem;'>🖼️ {arte['nome']}<br>(Não encontrada em assets/)</div>", unsafe_allow_html=True)
            
            # Botões de redirecionamento direto para os templates do Canva
            b_feed, b_story = st.columns(2)
            with b_feed:
                st.link_button("📱 FEED", arte["feed"], use_container_width=True)
            with b_story:
                st.link_button("📐 STORY", arte["story"], use_container_width=True)
            
            st.markdown("<br>", unsafe_allow_html=True)