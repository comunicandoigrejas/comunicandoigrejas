import streamlit as st
import os

def exibir():
    st.markdown("<h2 style='text-align: center; color: white; font-weight: bold;'>🎉 MODELOS DISPONÍVEIS: DATAS COMEMORATIVAS</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #888; font-size: 0.95rem;'>Escolha o formatado desejado para abrir o modelo editável diretamente no seu Canva.</p>", unsafe_allow_html=True)
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

    # Lista estruturada com as 15 artes e seus respectivos links oficiais de Feed e Story
    artes_comemorativas = [
        {"nome": "Datas Comemorativas 01.png", "feed": "https://canva.link/sxvloj2bx2zsp8u", "story": "https://canva.link/771udu9xp9cxp1f"},
        {"nome": "Datas Comemorativas 02.png", "feed": "https://canva.link/tk3k2s2hqif1dsp", "story": "https://canva.link/e259o5byvc79m03"},
        {"nome": "Datas Comemorativas 03.png", "feed": "https://canva.link/6d8xjqfp8s9ftq8", "story": "https://canva.link/3jrunuiwrejkcqr"},
        {"nome": "Datas Comemorativas 04.png", "feed": "https://canva.link/bdfhu1jdfo7n183", "story": "https://canva.link/jk1wlowljn9etet"},
        {"nome": "Datas Comemorativas 05.png", "feed": "https://canva.link/wrrtv5cotfcv2ff", "story": "https://canva.link/pbk9rlozylgdmv3"},
        {"nome": "Datas Comemorativas 06.png", "feed": "https://canva.link/pgwxgbr4fhx18c7", "story": "https://canva.link/9pnhvcb13vtlopb"},
        {"nome": "Datas Comemorativas 07.png", "feed": "https://canva.link/gzjcqcekh3jm24w", "story": "https://canva.link/m12mx83irk9l7o0"},
        {"nome": "Datas Comemorativas 08.png", "feed": "https://canva.link/4kptl4x693xfb2z", "story": "https://canva.link/up5ko39u9876tug"},
        {"nome": "Datas Comemorativas 09.png", "feed": "https://canva.link/t9p7l9azdp666q6", "story": "https://canva.link/ipydm7u701zbcw0"},
        {"nome": "Datas Comemorativas 10.png", "feed": "https://canva.link/sgrrawaqgwfrbsd", "story": "https://canva.link/c54o69jbn3z6yd7"},
        {"nome": "Datas Comemorativas 11.png", "feed": "https://canva.link/13lvjkyim37o7rj", "story": "https://canva.link/pfkkj8p4fkwxy6d"},
        {"nome": "Datas Comemorativas 12.png", "feed": "https://canva.link/4wggpocbjjtxtqd", "story": "https://canva.link/d7inwhu2buy9yjs"},
        {"nome": "Datas Comemorativas 13.png", "feed": "https://canva.link/eo2eli5c4ttctyd", "story": "https://canva.link/arfkl6dqugk1bkh"},
        {"nome": "Datas Comemorativas 14.png", "feed": "https://canva.link/oi4pkedd0cxgvti", "story": "https://canva.link/gkfa8a7i8mlpxwb"},
        {"nome": "Datas Comemorativas 15.png", "feed": "https://canva.link/3n44wxkrar8pbfn", "story": "https://canva.link/ptr9avt6mo1hywf"},
    ]

    # Grid organizada em 3 colunas largas para exibição das mídias
    col1, col2, col3 = st.columns(3)

    for idx, arte in enumerate(artes_comemorativas):
        # Distribuição uniforme e inteligente dos cards entre as colunas 1, 2 e 3
        coluna_alvo = col1 if idx % 3 == 0 else (col2 if idx % 3 == 1 else col3)
        
        with coluna_alvo:
            caminho_imagem = f"assets/{arte['nome']}"
            
            # Validação para verificar de forma segura se o arquivo de imagem correspondente está na pasta assets/
            if os.path.exists(caminho_imagem):
                st.image(caminho_imagem, use_container_width=True)
            else:
                # Fallback amigável caso a imagem ainda não tenha sido enviada ao repositório
                st.markdown(f"<div style='background-color: #1a1a1a; padding: 120px 10px; text-align: center; border-radius: 8px; color: #555; font-size:0.85rem;'>🖼️ {arte['nome']}<br>(Não encontrada em assets/)</div>", unsafe_allow_html=True)
            
            # Botões dinâmicos horizontais apontando direto para os templates do Canva
            b_feed, b_story = st.columns(2)
            with b_feed:
                st.link_button("📱 FEED (1:1)", arte["feed"], use_container_width=True)
            with b_story:
                st.link_button("📐 STORY (9:16)", arte["story"], use_container_width=True)
            
            st.markdown("<br>", unsafe_allow_html=True)