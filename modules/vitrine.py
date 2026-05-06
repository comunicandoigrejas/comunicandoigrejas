# modules/vitrine.py
import streamlit as st
import os

def exibir():
    # Função auxiliar para carregar imagens com segurança
    def carregar_imagem(nome_arquivo):
        caminho = f"assets/{nome_arquivo}"
        if os.path.exists(caminho):
            st.image(caminho, use_container_width=True)
        else:
            st.error(f"Arquivo não encontrado: {caminho}")

    # --- SEÇÃO 1: HERO (Banner Principal) ---
    st.markdown("<h1 class='gradient-title'>Mais de 2.000 Artes <br> Profissionais para Igrejas.</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; color: #FF2D95;'>Atualizações Semanais!</h3>", unsafe_allow_html=True)
    
    # Imagem 01 (Hero/Banner)
    carregar_imagem("hero_mockup.png")
    
    # --- SEÇÃO DE PREÇO DESTACADA (Borda roxa e fundo escuro) ---
    st.markdown(f"""
        <div style='text-align: center; margin: 30px 0; padding: 25px; border: 2px dashed #7B2CBF; border-radius: 15px; background-color: #0a0a0a;'>
            <span style='text-decoration: line-through; color: #888; font-size: 1.1rem;'>De R$ 197 por apenas</span>
            <div style='font-size: 4.5rem; font-weight: 800; color: #FF2D95; text-shadow: 0 0 15px rgba(255, 45, 149, 0.5);'>
                R$ 39,90
            </div>
            <p style='color: #fff; font-size: 1.1rem;'>Comece hoje e nunca mais dependa de designers!</p>
        </div>
    """, unsafe_allow_html=True)

    # --- BOTÃO DE COMPRA VERDE CENTRALIZADO ---
    col_btn1, col_btn2, col_btn3 = st.columns([1, 2, 1])
    with col_btn2:
        st.link_button(
            "🚀 QUERO ACESSAR AGORA MESMO", 
            "https://pay.hotmart.com/Y98906000N",
            use_container_width=True
        )

    # --- SEÇÃO 2: BENEFÍCIOS (O que você terá acesso) ---
    st.markdown("<br><br>", unsafe_allow_html=True)
    with st.container():
        st.markdown("""
            <div class='premium-card'>
                <h3 style='text-align: center; color: #fff;'>E o que você terá acesso?</h3>
                <ul style='list-style: none; padding: 0; color: #ddd;'>
                    <li style='margin-bottom: 10px;'>✅ <b>Artes Profissionais:</b> Mais de 2.000 artes prontas para usar no Canva.</li>
                    <li style='margin-bottom: 10px;'>✅ <b>Atualizações Semanais:</b> Novos conteúdos toda semana para sua igreja.</li>
                    <li style='margin-bottom: 10px;'>✅ <b>Vídeo Aulas Exclusivas:</b> Aprenda a dominar o Canva passo a passo.</li>
                    <li style='margin-bottom: 10px;'>✅ <b>Bônus Exclusivos:</b> Pacotes de fontes, texturas e elementos 3D.</li>
                    <li style='margin-bottom: 10px;'>✅ <b>Suporte Prioritário:</b> Contato direto e eficiente via WhatsApp.</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)

    # --- SEÇÃO 3: GALERIA DE AMOSTRAS (Imagem 02) ---
    st.markdown("<br><h2 style='text-align: center;'>Confira uma prévia do que você vai receber:</h2>", unsafe_allow_html=True)
    
    # Criando 4 colunas para que as imagens fiquem pequenas e lado a lado
    col_a, col_b, col_c, col_d = st.columns(4)
    
    with col_a:
        carregar_imagem("01.png")
    with col_b:
        carregar_imagem("02.png")
    with col_c:
        carregar_imagem("03.png")
    with col_d:
        carregar_imagem("04.png")

    # --- SEÇÃO 5: TABELA DE PLANOS (Imagem 04) ---
    st.markdown("<h2 style='text-align: center; margin-top: 50px;'>Escolha o Melhor Plano pra Você!</h2>", unsafe_allow_html=True)
    carregar_imagem("04.png")
    
    # Botões rápidos para os planos
    p1, p2, p3 = st.columns(3)
    with p1: st.button("ASSINAR START", key="plan_start", use_container_width=True)
    with p2: st.button("ASSINAR PREMIUM", key="plan_premium", use_container_width=True)
    with p3: st.button("ASSINAR EXCLUSIVE", key="plan_exclusive", use_container_width=True)

    # --- PERGUNTAS FREQUENTES ---
    st.markdown("<h3 style='text-align: center; margin-top: 60px;'>PERGUNTAS FREQUENTES</h3>", unsafe_allow_html=True)
    with st.expander("Como recebo meu acesso?"):
        st.write("O acesso é enviado imediatamente após a confirmação do pagamento via Hotmart.")
    with st.expander("Tem atualizações?"):
        st.write("Sim! Nossa plataforma é atualizada semanalmente com novas artes gospel.")
    with st.expander("Consigo editar pelo celular?"):
        st.write("Sim, todos os templates são 100% compatíveis com o aplicativo do Canva para celular.")

    # --- RODAPÉ ---
    st.markdown("---")
    col_f1, col_f2 = st.columns([2, 1])
    with col_f1:
        st.markdown("<b>FICOU COM DÚVIDA?</b><br>Entre em contato através do nosso WhatsApp.", unsafe_allow_html=True)
    with col_f2:
        st.link_button("💬 ATENDIMENTO WHATSAPP", "https://wa.me/551937704733")
