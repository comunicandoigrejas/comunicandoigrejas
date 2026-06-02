import streamlit as st
import os

def exibir():
    st.markdown("<h2 style='text-align: center; color: white; font-weight: bold;'>🍷 MODELOS DISPONÍVEIS: CULTO DE SANTA CEIA</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #888; font-size: 0.95rem;'>Escolha o formato desejado para abrir o modelo editável diretamente no seu Canva.</p>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    # CSS específico para botões brancos, modernos e responsivos (Padrão Comunicando Igrejas)
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

    # Lista de artes com os links oficiais fornecidos (Feed 1-9 e Stories 10-18)
    artes_ceia = [
        {"nome": "Santa Ceia 01.png", "feed": "https://canva.link/eyimcjb5jn4xzxp", "story": "https://canva.link/thmtbru5gtr2fol"},
        {"nome": "Santa Ceia 02.png", "feed": "https://canva.link/jtpm4e7hkv0w10v", "story": "https://canva.link/pqkd9sl8vml77cr"},
        {"nome": "Santa Ceia 03.png", "feed": "https://canva.link/yoxx1xb1u75qsbr", "story": "https://canva.link/horp5w38mtpb401"},
        {"nome": "Santa Ceia 04.png", "feed": "https://canva.link/c6aejnpr44ykw6x", "story": "https://canva.link/r603qjatjdxnauv"},
        {"nome": "Santa Ceia 05.png", "feed": "https://canva.link/1xqm589mwj3h32g", "story": "https://canva.link/vcx273uwzjiw3hl"},
        {"nome": "Santa Ceia 06.png", "feed": "https://canva.link/7j7hm7kblev9twq", "story": "https://canva.link/je8ot4xvutj0a9l"},
        {"nome": "Santa Ceia 07.png", "feed": "https://canva.link/hkd5scmqv37derz", "story": "https://canva.link/5y3o80ylqzy22no"},
        {"nome": "Santa Ceia 08.png", "feed": "https://canva.link/8sgpmy1rh66yg2d", "story": "https://canva.link/kp0o9ur3d0q990d"},
        {"nome": "Santa Ceia 09.png", "feed": "https://canva.link/s3heq00y9mqp6nc", "story": "https://canva.link/i6t9uf447ubjusi"},
    ]

    # Grid de 3 colunas largas para exibição das mídias
    col1, col2, col3 = st.columns(3)

    for idx, arte in enumerate(artes_ceia):
        # Distribuição inteligente dos cards nas 3 colunas
        coluna_alvo = col1 if idx % 3 == 0 else (col2 if idx % 3 == 1 else col3)
        
        with coluna_alvo:
            caminho_imagem = f"assets/{arte['nome']}"
            
            # Verificação segura de arquivos dentro de assets/
            if os.path.exists(caminho_imagem):
                st.image(caminho_imagem, use_container_width=True)
            else:
                # Fallback caso ocorra alguma divergência no nome do arquivo na pasta assets
                st.markdown(f"<div style='background-color: #1a1a1a; padding: 120px 10px; text-align: center; border-radius: 8px; color: #555; font-size:0.85rem;'>🖼️ {arte['nome']}<br>(Não encontrada em assets/)</div>", unsafe_allow_html=True)
            
            # Botões de Feed e Story alinhados horizontalmente abaixo da imagem
            b_feed, b_story = st.columns(2)
            with b_feed:
                st.link_button("📱 FEED", arte["feed"], use_container_width=True, key=f"feed_ceia_{idx}")
            with b_story:
                st.link_button("📐 STORY", arte["story"], use_container_width=True, key=f"story_ceia_{idx}")
                
            st.markdown("<br><br>", unsafe_allow_html=True)
