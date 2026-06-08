import streamlit as st
import os

def exibir():
    st.markdown("<h2 style='text-align: center; color: white; font-weight: bold;'>📅 MODELOS DISPONÍVEIS: AGENDA</h2>", unsafe_allow_html=True)
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

    # Lista estruturada com as 9 mídias de Agenda e seus respectivos links de Feed e Story (Formato PNG)
    artes_agenda = [
        {"nome": "Agenda 01.png", "feed": "https://canva.link/qb1xht3ia9x256y", "story": "https://canva.link/s66gy4m62r2a1ns"},
        {"nome": "Agenda 02.png", "feed": "https://canva.link/pkbm8qez2mo13c9", "story": "https://canva.link/btxn0dys0wkilef"},
        {"nome": "Agenda 03.png", "feed": "https://canva.link/ga88hsckzv1hdj6", "story": "https://canva.link/f4nte8p0qsmcew9"},
        {"nome": "Agenda 04.png", "feed": "https://canva.link/sz8g7m89r8w2g1x", "story": "https://canva.link/c58orfc19tvu74m"},
        {"nome": "Agenda 05.png", "feed": "https://canva.link/i1fyg29zwrmxvup", "story": "https://canva.link/88umywhbe7e2bj0"},
        {"nome": "Agenda 06.png", "feed": "https://canva.link/1vdqyeodp01h9he", "story": "https://canva.link/qd1m33nwzuk5wfw"},
        {"nome": "Agenda 07.png", "feed": "https://canva.link/yizlf46h18afi12", "story": "https://canva.link/lc0shvjqckxfoo2"},
        {"nome": "Agenda 08.png", "feed": "https://canva.link/k3whmhbqmarqaxe", "story": "https://canva.link/2l4295wjpoqyefa"},
        {"nome": "Agenda 09.png", "feed": "https://canva.link/moedxytqtdtwmua", "story": "https://canva.link/xuiub6cdcctpxkv"},
    ]

    # Grid organizada em 3 colunas de exibição
    col1, col2, col3 = st.columns(3)

    for idx, arte in enumerate(artes_agenda):
        # Distribuição uniforme dos cards pelas colunas
        coluna_alvo = col1 if idx % 3 == 0 else (col2 if idx % 3 == 1 else col3)
        
        with coluna_alvo:
            caminho_imagem = f"assets/{arte['nome']}"
            
            # Validação segura para exibir o arquivo .png da pasta assets/
            if os.path.exists(caminho_imagem):
                st.image(caminho_imagem, use_container_width=True)
            else:
                # Card alternativo amigável caso a imagem física não esteja na pasta assets/
                st.markdown(f"<div style='background-color: #1a1a1a; padding: 120px 10px; text-align: center; border-radius: 8px; color: #555; font-size:0.85rem;'>🖼️ {arte['nome']}<br>(Não encontrada em assets/)</div>", unsafe_allow_html=True)
            
            # Botões de redirecionamento direto para os templates do Canva
            b_feed, b_story = st.columns(2)
            with b_feed:
                st.link_button("📱 FEED", arte["feed"], use_container_width=True)
            with b_story:
                st.link_button("📐 STORY", arte["story"], use_container_width=True)
            
            st.markdown("<br>", unsafe_allow_html=True)