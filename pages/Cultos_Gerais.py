import streamlit as st
import os

def exibir():
    st.markdown("<h1 class='gradient-title'>⛪ Cultos Gerais</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>Escolha o formato ideal (Feed ou Story) para baixar e editar o seu template no Canva.</p>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    # Lista estruturada com os nomes base das imagens e os links correspondentes
    artes = [
        {"titulo":, "img_base": "Cultos Gerais 01", "feed": "https://canva.link/q1iy99fiuhdij9v", "story": "https://canva.link/39a7aig9rylbfx3"},
        {"titulo": "Cultos Gerais 02", "img_base": "Cultos Gerais 02", "feed": "https://canva.link/13bboathtx0kcbw", "story": "https://canva.link/shzp2bd8087nxhc"},
        {"titulo": "Cultos Gerais 03", "img_base": "Cultos Gerais 03", "feed": "https://canva.link/8dp6aqomdei1p93", "story": "https://canva.link/43cyvpd0io65bmd"},
        {"titulo": "Cultos Gerais 04", "img_base": "Cultos Gerais 04", "feed": "https://canva.link/iilqcqz88khx5ct", "story": "https://canva.link/m26hso5xwnzb2ot"},
        {"titulo": "Cultos Gerais 05", "img_base": "Cultos Gerais 05", "feed": "https://canva.link/40seh7gwmul8fq5", "story": "https://canva.link/ordyq2ibhkk7mnw"},
        {"titulo": "Cultos Gerais 06", "img_base": "Cultos Gerais 06", "feed": "https://canva.link/m81a1vp0ax97as1", "story": "https://canva.link/82yli7fl2qghus9"},
        {"titulo": "Cultos Gerais 07", "img_base": "Cultos Gerais 07", "feed": "https://canva.link/8fya2w3xw2pc7s7", "story": "https://canva.link/412ueqr89q5w16u"},
        {"titulo": "Cultos Gerais 08", "img_base": "Cultos Gerais 08", "feed": "https://canva.link/m2prw20152k1z3w", "story": "https://canva.link/tepbqpuxlvog6fw"}
    ]

    # Alterado para 3 colunas para deixar os cards menores e lado a lado
    cols = st.columns(3)

    for i, arte in enumerate(artes):
        # Distribui as artes entre as três colunas (0, 1 e 2)
        with cols[i % 3]:
            st.markdown("<div class='premium-card'>", unsafe_allow_html=True)
            
            # --- SISTEMA DE VERIFICAÇÃO DE EXTENSÕES ---
            # Testa caminhos na pasta 'assets' e na raiz com múltiplas extensões comuns
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
            
            # Exibe a imagem se encontrada, caso contrário mostra o aviso amigável
            if imagem_encontrada:
                st.image(imagem_encontrada, use_container_width=True)
            else:
                st.warning(f"⚠️ Imagem '{arte['img_base']}' não localizada.")

            st.markdown(f"### {arte['titulo']}")
            
            # Sub-colunas para os botões de Feed e Story ficarem perfeitamente alinhados
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
