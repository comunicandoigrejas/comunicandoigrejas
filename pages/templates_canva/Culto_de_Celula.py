import streamlit as st
import os

def exibir():
    st.markdown("<h2 style='text-align: center; color: white; font-weight: bold;'>🏡 MODELOS: CULTO DE CÉLULA</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #888; font-size: 0.95rem;'>Templates preparados para a divulgação dos pequenos grupos, células e cultos nos lares da sua comunidade.</p>", unsafe_allow_html=True)
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

    # Lista estruturada com os links fornecidos de Feed e Story (Nomes: CELULA 01.png a CELULA 09.png)
    artes_celula = [
        {"nome": "CELULA 01.png", "feed": "https://canva.link/lspbyhq7bsi9gl2", "story": "https://canva.link/0sq59n91itjt9ot"},
        {"nome": "CELULA 02.png", "feed": "https://canva.link/vbd1uib2fnoca5d", "story": "https://canva.link/428rowo2dv4olbc"},
        {"nome": "CELULA 03.png", "feed": "https://canva.link/lpfw73g8zplg4tc", "story": "https://canva.link/9oqxapklq2k0slb"},
        {"nome": "CELULA 04.png", "feed": "https://canva.link/nl6cdeinxqa3ruq", "story": "https://canva.link/h4swpq1rjyc0fmf"},
        {"nome": "CELULA 05.png", "feed": "https://canva.link/skxzmwfy9due7g3", "story": "https://canva.link/iq0mwe8iywglb2y"},
        {"nome": "CELULA 06.png", "feed": "https://canva.link/m54rrot5yw2ednr", "story": "https://canva.link/l2r5w4oiim6acla"},
        {"nome": "CELULA 07.png", "feed": "https://canva.link/auhohz4egimqurk", "story": "https://canva.link/8hmyvm4m5j9ho2j"},
        {"nome": "CELULA 08.png", "feed": "https://canva.link/ec4h29dxunrup81", "story": "https://canva.link/koqec2guhvfwznv"},
        {"nome": "CELULA 09.png", "feed": "https://canva.link/ec4h29dxunrup81", "story": "https://canva.link/dxszym8iibw8bhs"},
    ]

    # Grid organizada em 3 colunas de exibição
    col1, col2, col3 = st.columns(3)

    for idx, arte in enumerate(artes_celula):
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