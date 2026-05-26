import streamlit as st
import os

def exibir():
    st.markdown("<h2 style='text-align: center; color: white; font-weight: bold;'>⛪ MODELOS DISPONÍVEIS: CULTOS GERAIS</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #888; font-size: 0.95rem;'>Escolha o formato desejado para abrir o modelo editável diretamente no seu Canva.</p>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    # CSS específico para botões brancos, modernos e responsivos (Alinhado com a identidade do Comunicando Igrejas)
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

    # Lista de artes com os links oficiais fornecidos do 01 ao 09
    artes_cultos = [
        {"nome": "Cultos Gerais 01.jpg", "feed": "https://canva.link/q1iy99fiuhdij9v", "story": "https://canva.link/39a7aig9rylbfx3"},
        {"nome": "Cultos Gerais 02.jpg", "feed": "https://canva.link/13bboathtx0kcbw", "story": "https://canva.link/shzp2bd8087nxhc"},
        {"nome": "Cultos Gerais 03.jpg", "feed": "https://canva.link/8dp6aqomdei1p93", "story": "https://canva.link/43cyvpd0io65bmd"},
        {"nome": "Cultos Gerais 04.jpg", "feed": "https://canva.link/iilqcqz88khx5ct", "story": "https://canva.link/m26hso5xwnzb2ot"},
        {"nome": "Cultos Gerais 05.jpg", "feed": "https://canva.link/40seh7gwmul8fq5", "story": "https://canva.link/ordyq2ibhkk7mnw"},
        {"nome": "Cultos Gerais 06.jpg", "feed": "https://canva.link/m81a1vp0ax97as1", "story": "https://canva.link/412ueqr89q5w16u"},
        {"nome": "Cultos Gerais 07.jpg", "feed": "https://canva.link/8fya2w3xw2pc7s7", "story": "https://canva.link/82yli7fl2qghus9"},
        {"nome": "Cultos Gerais 08.jpg", "feed": "https://canva.link/m2prw20152k1z3w", "story": "https://canva.link/tepbqpuxlvog6fw"},
        {"nome": "Cultos Gerais 09.jpg", "feed": "https://canva.link/q3z3x2p5mkwu7m3", "story": "https://canva.link/1xl45srw25q1a8h"},
    ]

    # Grid de 3 colunas largas para exibição das mídias
    col1, col2, col3 = st.columns(3)

    for idx, arte in enumerate(artes_cultos):
        # Distribuição inteligente dos cards nas 3 colunas
        coluna_alvo = col1 if idx % 3 == 0 else (col2 if idx % 3 == 1 else col3)
        
        with coluna_alvo:
            caminho_imagem = f"assets/{arte['nome']}"
            
            # Verificação segura de arquivos dentro de assets/
            if os.path.exists(caminho_imagem):
                st.image(caminho_imagem, use_container_width=True)
            else:
                # Fallback caso a nova imagem 09 mude de extensão ou nome na pasta
                st.markdown(f"<div style='background-color: #1a1a1a; padding: 120px 10px; text-align: center; border-radius: 8px; color: #555; font-size:0.85rem;'>🖼️ {arte['nome']}<br>(Não encontrada em assets/)</div>", unsafe_allow_html=True)
            
            # Botões dinâmicos apontando direto para os templates do Canva
            b_feed, b_story = st.columns(2)
            with b_feed:
                st.link_button("📱 FEED", arte["feed"], use_container_width=True, key=f"feed_link_{idx}")
            with b_story:
                st.link_button("📐 STORY", arte["story"], use_container_width=True, key=f"story_link_{idx}")
                
            st.markdown("<br><br>", unsafe_allow_html=True)
