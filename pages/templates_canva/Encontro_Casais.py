import streamlit as st
import os

def exibir():
    st.markdown("<h2 style='text-align: center; color: white; font-weight: bold;'>💝 MODELOS: ENCONTRO DE CASAIS</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #888; font-size: 0.95rem;'>Templates românticos e elegantes preparados para abençoar os casamentos, palestras e encontros de casais.</p>", unsafe_allow_html=True)
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

    # Lista estruturada com os links reais fornecidos de Feed e Story (Nomes: Casais 01.png a Casais 09.png)
    artes_casais = [
        {"nome": "Casais 01.png", "feed": "https://canva.link/msv8gl3sqy7npz5", "story": "https://canva.link/zzutlsgay10qxwf"},
        {"nome": "Casais 02.png", "feed": "https://canva.link/hslwncmvvvtf7ak", "story": "https://canva.link/btk3q9fcc8aqbih"},
        {"nome": "Casais 03.png", "feed": "https://canva.link/lcx663jmxfp8a97", "story": "https://canva.link/u0bxmf9frqmkup6"},
        {"nome": "Casais 04.png", "feed": "https://canva.link/yp65ooypn564tsl", "story": "https://canva.link/9j3vnsf574xqms7"},
        {"nome": "Casais 05.png", "feed": "https://canva.link/21vci3s007901xs", "story": "https://canva.link/4118u2gnihsi9nj"},
        {"nome": "Casais 06.png", "feed": "https://canva.link/tlzaafgcqpeur90", "story": "https://canva.link/kbl1e0nj0v9wtil"},
        {"nome": "Casais 07.png", "feed": "https://canva.link/yzzbhasx28h3vkr", "story": "https://canva.link/4pomejel4lqy93i"},
        {"nome": "Casais 08.png", "feed": "https://canva.link/kjb9z0faypk78j0", "story": "https://canva.link/dm83yuvyexh7wq9"},
        {"nome": "Casais 09.png", "feed": "https://canva.link/d7c5jcimb24h2r6", "story": "https://canva.link/37fcd3r6nu43hos"},
    ]

    # Grid organizada em 3 colunas de exibição
    col1, col2, col3 = st.columns(3)

    for idx, arte in enumerate(artes_casais):
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
                st.link_button("📱 FEED (1:1)", arte["feed"], use_container_width=True)
            with b_story:
                st.link_button("📐 STORY (9:16)", arte["story"], use_container_width=True)
            
            st.markdown("<br>", unsafe_allow_html=True)