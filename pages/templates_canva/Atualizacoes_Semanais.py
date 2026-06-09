import streamlit as st
import os

def exibir():
    st.markdown("<h2 style='text-align: center; color: white; font-weight: bold;'>🔄 MODELOS: ATUALIZAÇÕES SEMANAIS</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #888; font-size: 0.95rem;'>Acesse aqui os templates mais recentes adicionados nesta semana diretamente no seu Canva.</p>", unsafe_allow_html=True)
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

    # Lista estruturada com os links fornecidos de Feed e Story (Nomes: Semana 01.png a Semana 09.png)
    artes_semanais = [
        {"nome": "Semana 01.png", "feed": "https://canva.link/em59o7bryn4swu5", "story": "https://canva.link/ayq7ozj386aia2u"},
        {"nome": "Semana 02.png", "feed": "https://canva.link/oatpwek72tl4j4v", "story": "https://canva.link/9ql2esed3d8kvuf"},
        {"nome": "Semana 03.png", "feed": "https://canva.link/eanwtrk4hz0kqy2", "story": "https://canva.link/toicstsyxx9q49w"},
        {"nome": "Semana 04.png", "feed": "https://canva.link/1q0pnrspnd20v26", "story": "https://canva.link/3fffblplmho2w0n"},
        {"nome": "Semana 05.png", "feed": "https://canva.link/tvc7o8825fvsghl", "story": "https://canva.link/czo15mrccsjlpjd"},
        {"nome": "Semana 06.png", "feed": "https://canva.link/cktrenpo08qgmmz", "story": "https://canva.link/cuu00zjs26ofawb"},
        {"nome": "Semana 07.png", "feed": "https://canva.link/73c3dm4fkcfgdwq", "story": "https://canva.link/5j9sv1zmptqfbj1"},
        {"nome": "Semana 08.png", "feed": "https://canva.link/yh3yiatgwr5qjxv", "story": "https://canva.link/kp4zm51x2axzvhy"},
        {"nome": "Semana 09.png", "feed": "https://canva.link/nmgfn91v0jf65on", "story": "https://canva.link/w2m14mzq2omra9f"},
    ]

    # Grid organizada em 3 colunas de exibição
    col1, col2, col3 = st.columns(3)

    for idx, arte in enumerate(artes_semanais):
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