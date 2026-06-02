import streamlit as st
import os

def exibir():
    st.markdown("<h2 style='text-align: center; color: white; font-weight: bold;'>🧔 MODELOS DISPONÍVEIS: CULTO DE HOMENS</h2>", unsafe_allow_html=True)
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

    # Lista de artes com os links fornecidos (Feed 1-9 correspondendo aos Stories 10-18)
    artes_homens = [
        {"nome": "Homens 01.png", "feed": "https://canva.link/3gd80uzk67fa9zx", "story": "https://canva.link/8782e9k7lgjuudd"},
        {"nome": "Homens 02.png", "feed": "https://canva.link/3kf68co9fo04y5n", "story": "https://canva.link/gdnctsw310ny6vy"},
        {"nome": "Homens 03.png", "feed": "https://canva.link/m1kw7gwmkarzbfu", "story": "https://canva.link/hg5qzh7xlj3d2hr"},
        {"nome": "Homens 04.png", "feed": "https://canva.link/ktmf3y35gpfwuu6", "story": "https://canva.link/bu9m06yggew05wz"},
        {"nome": "Homens 05.png", "feed": "https://canva.link/pegwjm9zcpguws2", "story": "https://canva.link/xvp9fnw3k6vkbow"},
        {"nome": "Homens 06.png", "feed": "https://canva.link/jmo0ejpdah7jb8a", "story": "https://canva.link/k7rfif3qyyzvkpz"},
        {"nome": "Homens 07.png", "feed": "https://canva.link/nhja72jf0trb07l", "story": "https://canva.link/q3otylx0rb8vanl"},
        {"nome": "Homens 08.png", "feed": "https://canva.link/op0vvvl6m7irgnd", "story": "https://canva.link/xcfyhe180hx6cn6"},
        {"nome": "Homens 09.png", "feed": "https://canva.link/xs23sezwxjd29db", "story": "https://canva.link/jlup3bj9nbx8arb"},
    ]

    # Grid organizada em 3 colunas para exibição das miniaturas das artes
    col1, col2, col3 = st.columns(3)

    for idx, arte in enumerate(artes_homens):
        # Distribuição uniforme dos itens entre as colunas 1, 2 e 3
        coluna_alvo = col1 if idx % 3 == 0 else (col2 if idx % 3 == 1 else col3)
        
        with coluna_alvo:
            caminho_imagem = f"assets/{arte['nome']}"
            
            # Validação para verificar se a imagem correspondente está na pasta assets/
            if os.path.exists(caminho_imagem):
                st.image(caminho_imagem, use_container_width=True)
            else:
                # Caso a imagem ainda não tenha subido, exibe o aviso com o nome esperado
                st.markdown(f"<div style='background-color: #1a1a1a; padding: 120px 10px; text-align: center; border-radius: 8px; color: #555; font-size:0.85rem;'>🖼️ {arte['nome']}<br>(Não encontrada em assets/)</div>", unsafe_allow_html=True)
            
            # Botões horizontais para direcionar aos templates correspondentes do Canva
            b_feed, b_story = st.columns(2)
            with b_feed:
                st.link_button("📱 FEED", arte["feed"], use_container_width=True, key=f"feed_homens_{idx}")
            with b_story:
                st.link_button("📐 STORY", arte["story"], use_container_width=True, key=f"story_homens_{idx}")
                
            st.markdown("<br><br>", unsafe_allow_html=True)
