import streamlit as st
import os

def exibir():
    st.markdown("<h2 style='text-align: center; color: white; font-weight: bold;'>🌸 MODELOS DISPONÍVEIS: CULTO DE MULHERES</h2>", unsafe_allow_html=True)
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

    # Lista de artes com os links fornecidos (Feed 1-9 correspondendo aos Stories 1-9)
    artes_mulheres = [
        {"nome": "Mulher 01.png", "feed": "https://canva.link/pjb7gwme04jivm8", "story": "https://canva.link/sjtdnr3yeuibay6"},
        {"nome": "Mulher 02.png", "feed": "https://canva.link/ztltvrvt2ddptpo", "story": "https://canva.link/m9l1mvgo1h69oxf"},
        {"nome": "Mulher 03.png", "feed": "https://canva.link/sn56iqr7e6thknp", "story": "https://canva.link/av23sebcsbfbmsa"},
        {"nome": "Mulher 04.png", "feed": "https://canva.link/tkiat1wsjjnl4cv", "story": "https://canva.link/53knwou4mytb447"},
        {"nome": "Mulher 05.png", "feed": "https://canva.link/f3smio7sxi250tu", "story": "https://canva.link/9yug4l3b2pzqrj9"},
        {"nome": "Mulher 06.png", "feed": "https://canva.link/8r1iv2bsbrhvqxt", "story": "https://canva.link/3hjtos1ln8owd1f"},
        {"nome": "Mulher 07.png", "feed": "https://canva.link/iymrmt216r8oogi", "story": "https://canva.link/005smyf31qp8cm7"},
        {"nome": "Mulher 08.png", "feed": "https://canva.link/u22klxtfh35cv87", "story": "https://canva.link/zh98wpqwlur17qp"},
        {"nome": "Mulher 09.png", "feed": "https://canva.link/71h5pcv3asr9x0y", "story": "https://canva.link/enbvqpalt002nuu"},
    ]

    # Grid organizada em 3 colunas para exibição das miniaturas das artes
    col1, col2, col3 = st.columns(3)

    for idx, arte in enumerate(artes_mulheres):
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
                st.link_button("📱 FEED", arte["feed"], use_container_width=True, key=f"feed_mulheres_{idx}")
            with b_story:
                st.link_button("📐 STORY", arte["story"], use_container_width=True, key=f"story_mulheres_{idx}")
                
            st.markdown("<br><br>", unsafe_allow_html=True)
