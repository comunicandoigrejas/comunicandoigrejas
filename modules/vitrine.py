# modules/vitrine.py
import streamlit as st
import os

def exibir():
    # Função para carregar imagens com segurança
    def carregar_imagem(nome_arquivo, legenda=None):
        caminho = f"assets/{nome_arquivo}"
        if os.path.exists(caminho):
            st.image(caminho, caption=legenda, use_container_width=True)
        else:
            st.info(f"Aguardando imagem: {nome_arquivo}")

    # --- SEÇÃO 1: HERO & PREÇO ---
    st.markdown("<h1 class='gradient-title'>Mais de 2.000 Artes <br> Profissionais para Igrejas.</h1>", unsafe_allow_html=True)
    
    st.markdown(f"""
        <div style='text-align: center; margin: 20px 0; padding: 25px; border: 2px dashed #7B2CBF; border-radius: 15px; background-color: #0a0a0a;'>
            <span style='text-decoration: line-through; color: #888; font-size: 1.1rem;'>De R$ 197 por apenas</span>
            <div style='font-size: 4.5rem; font-weight: 800; color: #FF2D95; text-shadow: 0 0 15px rgba(255, 45, 149, 0.5);'>
                R$ 39,90
            </div>
            <p style='color: #fff; font-size: 1.1rem;'>ACESSO IMEDIATO!</p>
        </div>
    """, unsafe_allow_html=True)

    # Botão de Compra Principal
    col_btn1, col_btn2, col_btn3 = st.columns([1, 2, 1])
    with col_btn2:
        st.link_button("🚀 QUERO O MEU PACK AGORA", "https://pay.hotmart.com/Y98906000N", use_container_width=True)

    # --- SEÇÃO 2: AMOSTRAS (Menores e Centralizadas) ---
    st.markdown("<br><h2 style='text-align: center;'>Uma prévia do que te espera:</h2>", unsafe_allow_html=True)
    
    # Usando colunas de respiro para deixar as imagens menores e elegantes
    respiro_esq, c1, c2, c3, c4, respiro_dir = st.columns([0.5, 2, 2, 2, 2, 0.5])
    with c1: carregar_imagem("01.png")
    with c2: carregar_imagem("02.png")
    with c3: carregar_imagem("03.png")
    with c4: carregar_imagem("04.png")

    # --- SEÇÃO 3: OS DOIS PLANOS (START & PREMIUM) ---
    st.markdown("<br><h2 style='text-align: center;'>Escolha o Plano Ideal:</h2>", unsafe_allow_html=True)
    
    col_plan1, col_plan2 = st.columns(2)

    with col_plan1:
        st.markdown(f"""
            <div class='premium-card' style='text-align: center; border-color: #7B2CBF;'>
                <h2 style='color: #7B2CBF;'>PLAN START</h2>
                <p>O essencial para sua igreja</p>
                <hr style='border-color: #333;'>
                <ul style='list-style: none; padding: 0; text-align: left; color: #bbb;'>
                    <li>✅ +500 Artes Editáveis</li>
                    <li>✅ Acesso via Canva</li>
                    <li>✅ Suporte via E-mail</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)
        st.button("ASSINAR START", key="plan_start", use_container_width=True)

    with col_plan2:
        st.markdown(f"""
            <div class='premium-card' style='text-align: center; border-color: #FF2D95; background-color: #111;'>
                <h2 style='color: #FF2D95;'>PLAN PREMIUM</h2>
                <p>O Pack Completo dos Abençoados</p>
                <hr style='border-color: #333;'>
                <ul style='list-style: none; padding: 0; text-align: left; color: #bbb;'>
                    <li>✅ +2.000 Artes Editáveis</li>
                    <li>✅ Atualizações Semanais</li>
                    <li>✅ Bônus Exclusivos</li>
                    <li>✅ Suporte VIP WhatsApp</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)
        st.button("ASSINAR PREMIUM 🔥", key="plan_premium", use_container_width=True)

    # --- RODAPÉ ---
    st.markdown("<br><hr>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #555;'>Comunicando Igrejas - Levando a mensagem com excelência.</p>", unsafe_allow_html=True)
