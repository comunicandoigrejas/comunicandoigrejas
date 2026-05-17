import streamlit as st
import os

def exibir():
    st.markdown("<h1 class='gradient-title'>⛪ Cultos Gerais</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>Escolha o formato ideal (Feed ou Story) para baixar e editar o seu template no Canva.</p>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    # Lista estruturada das artes
    artes = [
        {"img_base": "Cultos Gerais 01", "feed": "https://canva.link/q1iy99fiuhdij9v", "story": "https://canva.link/39a7aig9rylbfx3"},
        {"img_base": "Cultos Gerais 02", "feed": "https://canva.link/13bboathtx0kcbw", "story": "https://canva.link/shzp2bd8087nxhc"},
        {"img_base": "Cultos Gerais 03", "feed": "https://canva.link/8dp6aqomdei1p93", "story": "https://canva.link/43cyvpd0io65bmd"},
        {"img_base": "Cultos Gerais 04", "feed": "https://canva.link/iilqcqz88khx5ct", "story": "https://canva.link/m26hso5xwnzb2ot"},
        {"img_base": "Cultos Gerais 05", "feed": "https://canva.link/40seh7gwmul8fq5", "story": "https://canva.link/ordyq2ibhkk7mnw"},
        {"img_base": "Cultos Gerais 06", "feed": "https://canva.link/m81a1vp0ax97as1", "story": "https://canva.link/82yli7fl2qghus9"},
        {"img_base": "Cultos Gerais 07", "feed": "https://canva.link/8fya2w3xw2pc7s7", "story": "https://canva.link/412ueqr89q5w16u"},
        {"img_base": "Cultos Gerais 08", "feed": "https://canva.link/m2prw20152k1z3w", "story": "https://canva.link/tepbqpuxlvog6fw"}
    ]

    # Exibição em 3 colunas (imagens menores e lado a lado)
    cols = st.columns(3)

    for i, arte in enumerate(artes):
        with cols[i % 3]:
            # REMOVIDO: A div class='premium-card' foi retirada para eliminar a caixa rosa neon
            
            # Busca silenciosa da imagem nas pastas e extensões
            extensoes = ['.jpg', '.jpeg', '.png', '.PNG', '.JPG']
            imagem_encontrada = None
            
            for ext in extensoes:
                caminho_assets = f"assets/{arte['img_base']}{ext}"
                caminho_raiz = f"{arte['img_base']}{ext}"
                
                if os.path.exists(caminho_assets):
                    imagem_encontrada = caminho_assets
                    break
                elif os.path.exists(caminho_raiz):
                    imagem_encontrada = caminho_raiz
                    break
            
            # Se achar a imagem, coloca direto na coluna
            if imagem_encontrada:
                st.image(imagem_encontrada, use_container_width=True)
            else:
                st.markdown("<div style='text-align: center; padding: 20px; color: #555;'>🖼️ Carregando imagem...</div>", unsafe_allow_html=True)

            # Sub-colunas para os botões ficarem lado a lado logo abaixo da foto
            btn_col1, btn_col2 = st.columns(2)
            
            with btn_col1:
                st.link_button("📱 FEED", arte['feed'], use_container_width=True, key=f"feed_{i}")
                
            with btn_col2:
                st.link_button("📐 STORY", arte['story'], use_container_width=True, key=f"story_{i}")
            
            # Adiciona um pequeno espaço de separação para a linha de baixo não ficar colada
            st.markdown("<br>", unsafe_allow_html=True)

    # Botão de voltar para os temas
    st.markdown("---")
    if st.button("⬅️ Voltar aos Temas", use_container_width=True, key="voltar_cultos"):
        st.session_state.pagina_atual = None
        st.rerun()
