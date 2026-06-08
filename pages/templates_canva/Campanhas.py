import streamlit as st
import os

def exibir():
    st.markdown("<h2 style='text-align: center; color: white; font-weight: bold;'>📢 MODELOS DISPONÍVEIS: CAMPANHAS</h2>", unsafe_allow_html=True)
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

    # Lista estruturada com as 9 mídias de Campanhas e seus respectivos links de Feed e Story (Formato PNG)
    artes_campanhas = [
        {"nome": "Campanha 01.png", "feed": "https://canva.link/kovmljl4a51n4rq", "story": "https://canva.link/fzb6gvwyk3k1tey"},
        {"nome": "Campanha 02.png", "feed": "https://canva.link/lla5sibnkolydr1", "story": "https://canva.link/55xsoyoruexheq6"},
        {"nome": "Campanha 03.png", "feed": "https://canva.link/1h8jmnpcex7imul", "story": "https://canva.link/r44zzq2b3x2ij3x"},
        {"nome": "Campanha 04.png", "feed": "https://canva.link/ch4u159vta4xxev", "story": "https://canva.link/r9ndzqsjz1sujdq"},
        {"nome": "Campanha 05.png", "feed": "https://canva.link/psl1y6mt6l27a0j", "story": "https://canva.link/zfhhey5rst7oguo"},
        {"nome": "Campanha 06.png", "feed": "https://canva.link/qt7t1fpy3jgajv1", "story": "https://canva.link/iglxynh80s3bb86"},
        {"nome": "Campanha 07.png", "feed": "https://canva.link/se6w27h03m08xx8", "story": "https://canva.link/l1kf11ei6nlwtad"},
        {"nome": "Campanha 08.png", "feed": "https://canva.link/4ka1wby3zuf4jx5", "story": "https://canva.link/mo9c0f6gg4thkvq"},
        {"nome": "Campanha 09.png", "feed": "https://canva.link/bif7gkfm0ssgpq7", "story": "https://canva.link/98leyfudr2ov300"},
    ]

    # Grid organizada em 3 colunas de exibição
    col1, col2, col3 = st.columns(3)

    for idx, arte in enumerate(artes_campanhas):
        # Distribuição uniforme dos cards pelas colunas
        coluna_alvo = col1 if idx % 3 == 0 else (col2 if idx % 3 == 1 else col3)
        
        with coluna_alvo:
            caminho_imagem = f"assets/{arte['nome']}"
            
            # Validação segura para exibir o arquivo .png da pasta assets/
            if os.path.exists(caminho_imagem):
                st.image(caminho_imagem, use_container_width=True)
            else:
                # Caso a imagem de prévia não esteja na pasta, cria um card amigável informando o nome esperado
                st.markdown(f"<div style='background-color: #1a1a1a; padding: 120px 10px; text-align: center; border-radius: 8px; color: #555; font-size:0.85rem;'>🖼️ {arte['nome']}<br>(Não encontrada em assets/)</div>", unsafe_allow_html=True)
            
            # Botões de redirecionamento direto para os templates do Canva
            b_feed, b_story = st.columns(2)
            with b_feed:
                st.link_button("📱 FEED (1:1)", arte["feed"], use_container_width=True)
            with b_story:
                st.link_button("📐 STORY (9:16)", arte["story"], use_container_width=True)
            
            st.markdown("<br>", unsafe_allow_html=True)