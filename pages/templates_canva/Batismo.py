import streamlit as st
import os

def exibir():
    st.markdown("<h2 style='text-align: center; color: white; font-weight: bold;'>🌊 MODELOS: BATISMO</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #888; font-size: 0.95rem;'>Templates profissionais preparados para anunciar e celebrar as águas do batismo na sua igreja.</p>", unsafe_allow_html=True)
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

    # Lista estruturada com os links fornecidos de Feed e Story (Nomes: BATISMO 01.png a BATISMO 09.png)
    artes_batismo = [
        {"nome": "BATISMO 1.png", "feed": "https://canva.link/5mgpeczdop4rzkh", "story": "https://canva.link/cpkzu27h3m5l1de"},
        {"nome": "BATISMO 2.png", "feed": "https://canva.link/tax5mwtodsdfhuz", "story": "https://canva.link/r73eb5j0x4dish7"},
        {"nome": "BATISMO 3.png", "feed": "https://canva.link/yj70m5guvds95bq", "story": "https://canva.link/ud7615op0j63t52"},
        {"nome": "BATISMO 4.png", "feed": "https://canva.link/4xh076mj6hq2nye", "story": "https://canva.link/kcnvbtg5sf3qm1f"},
        {"nome": "BATISMO 5.png", "feed": "https://canva.link/bw3ggb8qwbgdhz1", "story": "https://canva.link/49es7f9czx6fj3u"},
        {"nome": "BATISMO 6.png", "feed": "https://canva.link/xv07y6cf66xtm0a", "story": "https://canva.link/ft5tb7f6p2ju3m1"},
        {"nome": "BATISMO 7.png", "feed": "https://canva.link/0x0w4ncywturgiu", "story": "https://canva.link/5ja4j9ita2fa253"},
        {"nome": "BATISMO 8.png", "feed": "https://canva.link/syn2dek9a7n4bz3", "story": "https://canva.link/e48qcaoyb68fmbd"},
        {"nome": "BATISMO 9.png", "feed": "https://canva.link/ws3qmkyvyq80v5j", "story": "https://canva.link/06zq17wqbdnyrh0"},
    ]

    # Grid organizada em 3 colunas de exibição
    col1, col2, col3 = st.columns(3)

    for idx, arte in enumerate(artes_batismo):
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