import streamlit as st
import os

def exibir():
    st.markdown("<h1 class='gradient-title'>⛪ Cultos Gerais</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>Escolha o formato ideal (Feed ou Story) para baixar e editar o seu template no Canva.</p>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    # Lista estruturada com os nomes das artes e os links correspondentes
    artes = [
        {"titulo": "Cultos Gerais 01", "img": "Cultos Gerais 01.jpg", "feed": "https://canva.link/q1iy99fiuhdij9v", "story": "https://canva.link/39a7aig9rylbfx3"},
        {"titulo": "Cultos Gerais 02", "img": "Cultos Gerais 02.jpg", "feed": "https://canva.link/13bboathtx0kcbw", "story": "https://canva.link/shzp2bd8087nxhc"},
        {"titulo": "Cultos Gerais 03", "img": "Cultos Gerais 03.jpg", "feed": "https://canva.link/8dp6aqomdei1p93", "story": "https://canva.link/43cyvpd0io65bmd"},
        {"titulo": "Cultos Gerais 04", "img": "Cultos Gerais 04.jpg", "feed": "https://canva.link/iilqcqz88khx5ct", "story": "https://canva.link/m26hso5xwnzb2ot"},
        {"titulo": "Cultos Gerais 05", "img": "Cultos Gerais 05.jpg", "feed": "https://canva.link/40seh7gwmul8fq5", "story": "https://canva.link/ordyq2ibhkk7mnw"},
        {"titulo": "Cultos Gerais 06", "img": "Cultos Gerais 06.jpg", "feed": "https://canva.link/m81a1vp0ax97as1", "story": "https://canva.link/82yli7fl2qghus9"},
        {"titulo": "Cultos Gerais 07", "img": "Cultos Gerais 07.jpg", "feed": "https://canva.link/8fya2w3xw2pc7s7", "story": "https://canva.link/412ueqr89q5w16u"},
        {"titulo": "Cultos Gerais 08", "img": "Cultos Gerais 08.jpg", "feed": "https://canva.link/m2prw20152k1z3w", "story": "https://canva.link/tepbqpuxlvog6fw"}
    ]

    # Criando o layout de 2 colunas para exibição lado a lado
    cols = st.columns(2)

    for i, arte in enumerate(artes):
        with cols[i % 2]:
            st.markdown("<div class='premium-card'>", unsafe_allow_html=True)
            
            # --- SISTEMA INTELIGENTE DE BUSCA DE IMAGEM ---
            caminho_raiz = arte['img']
            caminho_assets = f"assets/{arte['img']}"
            
            # Verifica primeiro se está na pasta 'assets'
            if os.path.exists(caminho_assets):
                st.image(caminho_assets, use_container_width=True)
            # Se não estiver, verifica na raiz do projeto
            elif os.path.exists(caminho_raiz):
                st.image(caminho_raiz, use_container_width=True)
            else:
                st.warning(f"⚠️ Não encontramos a imagem '{arte['img']}' nem na raiz nem na pasta 'assets'. Verifique se o nome no GitHub está correto.")

            st.markdown(f"### {arte['titulo']}")
            st.markdown("<p style='color: #888888; font-size: 0.9rem;'>Selecione o formato desejado:</p>", unsafe_allow_html=True)
            
            # Sub-colunas para os botões de Feed e Story ficarem lado a lado
            btn_col1, btn_col2 = st.columns(2)
            
            with btn_col1:
                st.link_button("📱 FEED", arte['feed'], use_container_width=True, key=f"feed_{i}")
                
            with btn_col2:
                st.link_button("📐 STORY", arte['story'], use_container_width=True, key=f"story_{i}")
            
            st.markdown("</div>", unsafe_allow_html=True)

    # Botão para voltar à seleção de temas
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("⬅️ Voltar aos Temas", use_container_width=True, key="voltar_cultos"):
        st.session_state.pagina_atual = None
        st.rerun()
