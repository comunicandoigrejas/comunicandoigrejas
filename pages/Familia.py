import streamlit as st
import os

def exibir():
    st.markdown("<h2 style='color: #00D2FF; font-weight: bold; margin-bottom: 5px;'>👨‍👩‍👧‍👦 Culto da Família</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color: #888888; font-size: 1.05rem;'>Selecione o modelo desejado abaixo e clique nos botões para abrir o link de edição diretamente no seu Canva.</p>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    # --- DICIONÁRIO DE LINKS (FEED E STORY MAPEADOS) ---
    TEMPLATES_FAMILIA = {
        "01": {
            "feed": "https://canva.link/pfrtk1xbvzm0p7r",
            "story": "https://canva.link/71a37o3fr02cex7"
        },
        "02": {
            "feed": "https://canva.link/ci63w1sxkl9q1cd",
            "story": "https://canva.link/s56b64yxy82s4fa"
        },
        "03": {
            "feed": "https://canva.link/c5q45ey5hya0vh6",
            "story": "https://canva.link/1h5tzgtblb5b44u"
        },
        "04": {
            "feed": "https://canva.link/7lxxfbfdm9aea5r",
            "story": "https://canva.link/d18tcb80lbqr1po"
        },
        "05": {
            "feed": "https://canva.link/218p8vv5gxqsqbg",
            "story": "https://canva.link/zuu6xix69i0e9ma"
        },
        "06": {
            "feed": "https://canva.link/kykta04w5w40kak",
            "story": "https://canva.link/wpf8aa7xywsuyvt"
        },
        "07": {
            "feed": "https://canva.link/e2el7wghnwrb0y1",
            "story": "https://canva.link/zo1hiz1w7uf9xv7"
        },
        "08": {
            "feed": "https://canva.link/k0moqgzszdfvy0q",
            "story": "https://canva.link/ot8qilq8nfnzn25"
        },
        "09": {
            "feed": "https://canva.link/0mgkheryu9by4qk",
            "story": "https://canva.link/wd42zxtruh1w68y"
        }
    }

    # --- GRID DE EXIBIÇÃO EM 3 COLUNAS ---
    # Serão 3 linhas contendo 3 cards cada, totalizando as 9 artes
    lista_chaves = sorted(list(TEMPLATES_FAMILIA.keys()))
    
    for i in range(0, len(lista_chaves), 3):
        grupo_chaves = lista_chaves[i:i+3]
        colunas = st.columns(3)
        
        for idx, chave in enumerate(grupo_chaves):
            with colunas[idx]:
                # Configura os nomes exatos das imagens conforme sua pasta assets
                nome_imagem = f"Culto Familia {chave}.png"
                caminho_completo = f"assets/{nome_imagem}"
                
                # Container estilizado simulando o card escuro do sistema
                st.markdown(f"""
                    <div style='background-color: #0c0c0c; border: 1px solid #1f1f1f; padding: 15px; border-radius: 10px; margin-bottom: 10px;'>
                        <p style='color: #00D2FF; font-weight: bold; margin-top: 0; margin-bottom: 10px; font-size: 0.95rem;'>🎨 Modelo {chave}</p>
                    </div>
                """, unsafe_allow_html=True)
                
                # Validação de carregamento seguro da imagem
                if os.path.exists(caminho_completo):
                    st.image(caminho_completo, use_container_width=True)
                elif os.path.exists(nome_imagem):
                    st.image(nome_imagem, use_container_width=True)
                else:
                    # Caso a imagem não seja encontrada na pasta, exibe um mockup elegante para não quebrar a tela
                    st.markdown(f"""
                        <div style='background-color: #151515; height: 260px; display: flex; align-items: center; justify-content: center; border-radius: 6px; margin-bottom: 15px; border: 1px dashed #333;'>
                            <span style='color: #555; font-size: 0.9rem;'>🖼️ {nome_imagem}</span>
                        </div>
                    """, unsafe_allow_html=True)
                
                # Espaçador interno antes dos botões de ação
                st.markdown("<div style='margin-top: 5px;'></div>", unsafe_allow_html=True)
                
                # Dois botões lado a lado para direcionamento ao Canva
                btn_col1, btn_col2 = st.columns(2)
                with btn_col1:
                    st.link_button("📱 Canva Story", TEMPLATES_FAMILIA[chave]["story"], use_container_width=True, key=f"story_fam_{chave}")
                with btn_col2:
                    st.link_button("🖼️ Canva Feed", TEMPLATES_FAMILIA[chave]["feed"], use_container_width=True, key=f"feed_fam_{chave}")
                
                st.markdown("<br><br>", unsafe_allow_html=True)

# Execução direta para testes individuais se necessário
if __name__ == "__main__":
    exibir()
