import streamlit as st
import os

def exibir():
    st.markdown("<h2 style='text-align: center; color: white; font-weight: bold;'>🎉 MODELOS DISPONÍVEIS: DATAS COMEMORATIVAS</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #888; font-size: 0.95rem;'>Escolha o formato desejado para abrir o modelo editável diretamente no seu Canva.</p>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    # CSS unificado para os botões brancos elegantes
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

    # Lista estruturada seguindo o padrão oficial
    artes_comemorativas = [
        {"nome": "artes_natal.png", "titulo": "Pack Natal e Páscoa", "qtd": "30 Templates Especiais", "link": "https://www.canva.com/..."},
    ]

    # Grid de 3 colunas limpo
    col1, col2, col3 = st.columns(3)

    for idx, arte in enumerate(artes_comemorativas):
        coluna_alvo = col1 if idx % 3 == 0 else (col2 if idx % 3 == 1 else col3)
        
        with coluna_alvo:
            caminho_imagem = f"assets/{arte['nome']}"
            
            if os.path.exists(caminho_imagem):
                st.image(caminho_imagem, use_container_width=True)
            else:
                st.markdown(f"<div style='background-color: #1a1a1a; padding: 120px 10px; text-align: center; border-radius: 8px; color: #555; font-size:0.85rem;'>🖼️ {arte['nome']}<br>(Não encontrada em assets/)</div>", unsafe_allow_html=True)
            
            st.markdown(f"<p style='margin-bottom:2px; font-weight:bold; color:white;'>{arte['titulo']}</p>", unsafe_allow_html=True)
            st.markdown(f"<p style='color:#888; font-size:0.85rem; margin-bottom:8px;'>{arte['qtd']}</p>", unsafe_allow_html=True)
            
            st.link_button("🎨 EDITAR NO CANVA", arte["link"], use_container_width=True)
