import streamlit as st
import os

def exibir():
    st.markdown("<h2 style='text-align: center; color: white; font-weight: bold;'>👨‍👩‍👧‍👦 MODELOS DISPONÍVEIS: CULTO DA FAMÍLIA</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #888; font-size: 0.95rem;'>Escolha o formato desejado para abrir o modelo editável diretamente no seu Canva.</p>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    # CSS específico para botões brancos, modernos e responsivos (Idêntico ao padrão Cultos Gerais)
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

    # Lista de artes com os links oficiais fornecidos do 01 ao 09 para Família
    artes_familia = [
        {"nome": "Culto Familia 01.png", "feed": "https://canva.link/pfrtk1xbvzm0p7r", "story": "https://canva.link/71a37o3fr02cex7"},
        {"nome": "Culto Familia 02.png", "feed": "https://canva.link/ci63w1sxkl9q1cd", "story": "https://canva.link/s56b64yxy82s4fa"},
        {"nome": "Culto Familia 03.png", "feed": "https://canva.link/c5q45ey5hya0vh6", "story": "https://canva.link/1h5tzgtblb5b44u"},
        {"nome": "Culto Familia 04.png", "feed": "https://canva.link/7lxxfbfdm9aea5r", "story": "https://canva.link/d18tcb80lbqr1po"},
        {"nome": "Culto Familia 05.png", "feed": "https://canva.link/218p8vv5gxqsqbg", "story": "https://canva.link/zuu6xix69i0e9ma"},
        {"nome": "Culto Familia 06.png", "feed": "https://canva.link/kykta04w5w40kak", "story": "https://canva.link/wpf8aa7xywsuyvt"},
        {"nome": "Culto Familia 07.png", "feed": "https://canva.link/e2el7wghnwrb0y1", "story": "https://canva.link/zo1hiz1w7uf9xv7"},
        {"nome": "Culto Familia 08.png", "feed": "https://canva.link/k0moqgzszdfvy0q", "story": "https://canva.link/ot8qilq8nfnzn25"},
        {"nome": "Culto Familia 09.png", "feed": "https://canva.link/0mgkheryu9by4qk", "story": "https://canva.link/wd42zxtruh1w68y"},
    ]

    # Grid de 3 colunas largas para exibição das mídias (Igual ao Cultos Gerais)
    col1, col2, col3 = st.columns(3)

    for idx, arte in enumerate(artes_familia):
        # Distribuição inteligente dos cards nas 3 colunas
        coluna_alvo = col1 if idx % 3 == 0 else (col2 if idx % 3 == 1 else col3)
        
        with coluna_alvo:
            caminho_imagem = f"assets/{arte['nome']}"
            
            # Verificação segura de arquivos dentro de assets/
            if os.path.exists(caminho_imagem):
                st.image(caminho_imagem, use_container_width=True)
            else:
                # Fallback caso ocorra alguma divergência no nome do arquivo na pasta
                st.markdown(f"<div style='background-color: #1a1a1a; padding: 120px 10px; text-align: center; border-radius: 8px; color: #555; font-size:0.85rem;'>🖼️ {arte['nome']}<br>(Não encontrada em assets/)</div>", unsafe_allow_html=True)
            
            # Botões dinâmicos com textos idênticos ao padrão enviado
            b_feed, b_story = st.columns(2)
            with b_feed:
                st.link_button("📱 FEED", arte["feed"], use_container_width=True, key=f"feed_fam_{idx}")
            with b_story:
                st.link_button("📐 STORY", arte["story"], use_container_width=True, key=f"story_fam_{idx}")
                
            st.markdown("<br><br>", unsafe_allow_html=True)
