import streamlit as st
import os

def exibir():
    st.markdown("<h2 style='text-align: center; color: white; font-weight: bold;'>⚡ MODELOS DISPONÍVEIS: CULTO DE JOVENS</h2>", unsafe_allow_html=True)
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

    # Lista estruturada com as 9 mídias de Jovens e seus respectivos links de Feed e Story (Formato PNG)
    artes_jovens = [
        {"nome": "Jovens 01.png", "feed": "https://canva.link/938q9vqsa53mzuv", "story": "https://canva.link/1jb9lkc2dovgukv"},
        {"nome": "Jovens 02.png", "feed": "https://canva.link/0x8p001ju1j1qjl", "story": "https://canva.link/0zr7yt3rp3lspc7"},
        {"nome": "Jovens 03.png", "feed": "https://canva.link/aozfozx5c5dquto", "story": "https://canva.link/tkd9ncckh940oib"},
        {"nome": "Jovens 04.png", "feed": "https://canva.link/humub8ax89g54lx", "story": "https://canva.link/vjpgoyswue3qf3t"},
        {"nome": "Jovens 05.png", "feed": "https://canva.link/pfjfd72ipvgf747", "story": "https://canva.link/k5mzdbf5esj7pxm"},
        {"nome": "Jovens 06.png", "feed": "https://canva.link/j1snf69eabg6dgx", "story": "https://canva.link/eacns05q4250u3w"},
        {"nome": "Jovens 07.png", "feed": "https://canva.link/zq3bh71b2ik6ljb", "story": "https://canva.link/7rgosnfoirw05u9"},
        {"nome": "Jovens 08.png", "feed": "https://canva.link/bb7ryp7x4rx45b0", "story": "https://canva.link/u1tbh2cmh1aijzc"},
        {"nome": "Jovens 09.png", "feed": "https://canva.link/0jb9pd688roy9ip", "story": "https://canva.link/h5hzd0zmdpjatg9"},
    ]

    # Grid organizada em 3 colunas de exibição
    col1, col2, col3 = st.columns(3)

    for idx, arte in enumerate(artes_jovens):
        # Distribuição uniforme dos cards pelas colunas
        coluna_alvo = col1 if idx % 3 == 0 else (col2 if idx % 3 == 1 else col3)
        
        with coluna_alvo:
            caminho_imagem = f"assets/{arte['nome']}"
            
            # Validação segura para exibir o arquivo .png da pasta assets/
            if os.path.exists(caminho_imagem):
                st.image(caminho_imagem, use_container_width=True)
            else:
                # Caso a prévia não esteja na pasta, cria um card escuro amigável informando o nome correto
                st.markdown(f"<div style='background-color: #1a1a1a; padding: 120px 10px; text-align: center; border-radius: 8px; color: #555; font-size:0.85rem;'>🖼️ {arte['nome']}<br>(Não encontrada em assets/)</div>", unsafe_allow_html=True)
            
            # Botões de redirecionamento direto para o Canva
            b_feed, b_story = st.columns(2)
            with b_feed:
                st.link_button("📱 FEED (1:1)", arte["feed"], use_container_width=True)
            with b_story:
                st.link_button("📐 STORY (9:16)", arte["story"], use_container_width=True)
            
            st.markdown("<br>", unsafe_allow_html=True)