# modules/vitrine.py
import streamlit as st
import os

def exibir():
    # Função para carregar imagens com segurança
    def carregar_imagem(nome_arquivo, legenda=None, width=None):
        caminho = f"assets/{nome_arquivo}"
        if os.path.exists(caminho):
            st.image(caminho, caption=legenda, use_container_width=True)
        else:
            # Mensagem discreta caso a imagem ainda não tenha sido subida
            st.info(f"Aguardando o banner principal: {nome_arquivo}")

    # --- SEÇÃO 1: HERO (IMAGEM PRINCIPAL NO TOPO) ---
    # Esta é a imagem que faltou, ocupando a largura total para impacto inicial
    carregar_imagem("hero_mockup.png")

    st.markdown("<h1 class='gradient-title'>Mais de 2.000 Artes <br> Profissionais para Igrejas.</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; color: #FF2D95;'>Atualizações Semanais e Suporte VIP</h3>", unsafe_allow_html=True)
    
    # --- SEÇÃO DE PREÇO ---
    st.markdown(f"""
        <div style='text-align: center; margin: 20px 0; padding: 25px; border: 2px dashed #7B2CBF; border-radius: 15px; background-color: #0a0a0a;'>
            <span style='text-decoration: line-through; color: #888; font-size: 1.1rem;'>De R$ 197 por apenas</span>
            <div style='font-size: 4.5rem; font-weight: 800; color: #FF2D95; text-shadow: 0 0 15px rgba(255, 45, 149, 0.5);'>
                R$ 39,90
            </div>
            <p style='color: #fff; font-size: 1.1rem;'>OFERTA EXCLUSIVA - COMUNICANDO IGREJAS</p>
        </div>
    """, unsafe_allow_html=True)

    # Botão de Compra
    col_btn1, col_btn2, col_btn3 = st.columns([1, 2, 1])
    with col_btn2:
        st.link_button("🚀 COMPRAR AGORA", "https://pay.hotmart.com/Y98906000N", use_container_width=True)

    # --- SEÇÃO 2: AMOSTRAS (01 a 04) ---
    st.markdown("<br><h2 style='text-align: center;'>Artes prontas para o seu Instagram:</h2>", unsafe_allow_html=True)
    
    # Galeria menor e centralizada
    respiro_e, c1, c2, c3, c4, respiro_d = st.columns([0.5, 2, 2, 2, 2, 0.5])
    with c1: carregar_imagem("1.png")
    with c2: carregar_imagem("2.png")
    with c3: carregar_imagem("3.png")
    with c4: carregar_imagem("4.png")

    # ... (Restante do código dos planos START e PREMIUM)
