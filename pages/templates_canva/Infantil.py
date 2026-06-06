import streamlit as st
import os

def exibir():
    st.markdown("<h2 style='text-align: center; color: white; font-weight: bold;'>🧸 MODELOS DISPONÍVEIS: CULTO INFANTIL</h2>", unsafe_allow_html=True)
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

    # Lista estruturada com as 9 mídias e seus respectivos links oficiais de Feed e Story
    artes_infantil = [
        {"nome": "Culto Infantil 01.jpg", "feed": "https://canva.link/v4kmuk6aklzvx4t", "story": "https://canva.link/cfsvbw2tu16gcxy"},
        {"nome": "Culto Infantil 02.jpg", "feed": "https://canva.link/7v0vr69th916y3r", "story": "https://canva.link/kbgu19at8m8ux4y"},
        {"nome": "Culto Infantil 03.jpg", "feed": "https://canva.link/h2rupxa1wjdpefy", "story": "https://canva.link/95qzq4up1h8evg7"},
        {"nome": "Culto Infantil 04.jpg", "feed": "https://canva.link/apapuidnikn6wu5", "story": "https://canva.link/mijp8nc7bb22zv7"},
        {"nome": "Culto Infantil 05.jpg", "feed": "https://canva.link/1nlqibv2yrkfis9", "story": "https://canva.link/p03j3dp2l6q0lg7"},
        {"nome": "Culto Infantil 06.jpg", "feed": "https://canva.link/fr8e79rz1h2otxi", "story": "https://canva.link/lb2u82yrhbcahua"},
        {"nome": "Culto Infantil 07.jpg", "feed": "https://canva.link/xieny074bew0uv8", "story": "https://canva.link/jllanhplkfris0h"},
        {"nome": "Culto Infantil 08.jpg", "feed": "https://canva.link/w5nzea5xy65otnt", "story": "https://canva.link/9sztooeifsyc9dr"},
        {"nome": "Culto Infantil 09.jpg", "feed": "https://canva.link/5n55y3s83qhd6j2", "story": "https://canva.link/rasx5l5kp23mfc8"},
    ]

    # Grid organizada em 3 colunas de exibição
    col1, col2, col3 = st.columns(3)

    for idx, arte in enumerate(artes_infantil):
        # Distribuição uniforme dos cards pelas colunas
        coluna_alvo = col1 if idx % 3 == 0 else (col2 if idx % 3 == 1 else col3)
        
        with coluna_alvo:
            caminho_imagem = f"assets/{arte['nome']}"
            
            # Validação segura para exibir a imagem da pasta assets/
            if os.path.exists(caminho_imagem):
                st.image(caminho_imagem, use_container_width=True)
            else:
                # Caso a prévia não esteja na pasta, cria um card cinza amigável informando o nome correto
                st.markdown(f"<div style='background-color: #1a1a1a; padding: 120px 10px; text-align: center; border-radius: 8px; color: #555; font-size:0.85rem;'>🖼️ {arte['nome']}<br>(Não encontrada em assets/)</div>", unsafe_allow_html=True)
            
            # Botões de redirecionamento direto para o Canva
            b_feed, b_story = st.columns(2)
            with b_feed:
                st.link_button("📱 FEED (1:1)", arte["feed"], use_container_width=True)
            with b_story:
                st.link_button("📐 STORY (9:16)", arte["story"], use_container_width=True)
            
            st.markdown("<br>", unsafe_allow_html=True)