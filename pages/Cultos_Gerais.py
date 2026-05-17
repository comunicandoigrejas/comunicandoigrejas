import streamlit as st
import os

def exibir():
    st.markdown("<h1 class='gradient-title'>⛪ Cultos Gerais</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>Escolha o formato ideal (Feed ou Story) para baixar e editar o seu template no Canva.</p>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    # Lista estruturada com os nomes base das imagens e os links correspondentes
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

    # Organizado em 3 colunas para manter os cards menores
    cols = st.columns(3)

    for i, arte in enumerate(artes):
        with cols[i % 3]:
            st.markdown("<div class='premium-card'>", unsafe_allow_html=True)
            
            # --- SISTEMA SILENCIOSO DE VERIFICAÇÃO ---
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
            
            # Exibe a imagem se encontrada. Se não encontrar, mostra um espaço reservado discreto
            if imagem_encontrada:
                st.image(imagem_encontrada, use_container_width=True)
            else:
                st.markdown("<div style='text-align: center; padding: 40px; color: #555;'>🖼️ Carregando arte...</div>", unsafe_allow_html=True)

            st.markdown("<br>", unsafe_allow_html=True)
            
            # Sub-colunas para os botões de Feed e Story ficarem alinhados logo abaixo da imagem
            btn_col1, btn_col2 = st.columns(2)
            
            with btn_col1:
                st.link_button("📱 FEED", arte['feed'], use_container_width=True, key=f"feed_{i}")
                
            with btn_col2:
                st.link_button("📐 STORY", arte['story'], use_container_width=True, key=f"story_{i}")
            
            st.markdown("</div>", unsafe_allow_html=True)

    # Botão para voltar à seleção de temas do Dashboard
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("⬅️ Voltar aos Temas", use_container_width=True, key="voltar_cultos"):
        st.session_state.pagina_atual = None
        st.rerun()
