import streamlit as st
import os

def exibir():
    st.markdown("<h2 style='text-align: center; color: white; font-weight: bold;'>⛪ MODELOS DISPONÍVEIS: CULTOS GERAIS</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #888; font-size: 0.95rem;'>Escolha o formato desejado para abrir o modelo editável diretamente no seu Canva.</p>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    # CSS específico para deixar os botões brancos, modernos e alinhados
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

    # Mapeamento exato dos arquivos .jpg da sua pasta assets
    # Substitua os '#' pelos seus links oficiais de edição do Canva
    artes_cultos = [
        {"nome": "Cultos Gerais 01.jpg", "feed": "#", "story": "#"},
        {"nome": "Cultos Gerais 02.jpg", "feed": "#", "story": "#"},
        {"nome": "Cultos Gerais 03.jpg", "feed": "#", "story": "#"},
        {"nome": "Cultos Gerais 04.jpg", "feed": "#", "story": "#"},
        {"nome": "Cultos Gerais 05.jpg", "feed": "#", "story": "#"},
        {"nome": "Cultos Gerais 06.jpg", "feed": "#", "story": "#"},
        {"nome": "Cultos Gerais 07.jpg", "feed": "#", "story": "#"},
        {"nome": "Cultos Gerais 08.jpg", "feed": "#", "story": "#"},
    ]

    # Grid amplo de 3 colunas para exibição das mídias
    col1, col2, col3 = st.columns(3)

    for idx, arte in enumerate(artes_cultos):
        # Distribui os cards entre as colunas 1, 2 e 3 de forma limpa
        coluna_alvo = col1 if idx % 3 == 0 else (col2 if idx % 3 == 1 else col3)
        
        with coluna_alvo:
            caminho_imagem = f"assets/{arte['nome']}"
            
            # Verificação da existência do arquivo .jpg
            if os.path.exists(caminho_imagem):
                st.image(caminho_imagem, use_container_width=True)
            else:
                # Caixa alternativa caso falte alguma imagem na pasta assets
                st.markdown(f"<div style='background-color: #1a1a1a; padding: 120px 10px; text-align: center; border-radius: 8px; color: #555; font-size:0.85rem;'> 🖼️ {arte['nome']}<br>(Não encontrada em assets/)</div>", unsafe_allow_html=True)
            
            # Sub-grid inferior contendo apenas as duas opções (FEED e STORY) lado a lado
            b_feed, b_story = st.columns(2)
            with b_feed:
                st.link_button("📱 FEED", arte["feed"], use_container_width=True, key=f"feed_{idx}")
            with b_story:
                st.link_button("📐 STORY", arte["story"], use_container_width=True, key=f"story_{idx}")
                
            st.markdown("<br><br>", unsafe_allow_html=True)
