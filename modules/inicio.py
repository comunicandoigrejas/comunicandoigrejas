import streamlit as st

def exibir_landing_page():
    # --- SEÇÃO 1: HERO (Foto 1) ---
    st.markdown("<h1 class='gradient-title'>Mais de 2.000 Artes Profissionais para Igrejas.</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;'>Atualizações Semanais!</h3>", unsafe_allow_html=True)
    
    # Placeholder para o vídeo/imagem central
    st.image("assets/image_fcbdfe.png", use_container_width=True) # Referência à imagem enviada
    
    st.markdown("<div class='price-tag'>R$ 27</div>", unsafe_allow_html=True)
    if st.button("🚀 QUERO ACESSAR AGORA MESMO", use_container_width=True):
        st.write("Redirecionando...")

    # --- SEÇÃO 2: O QUE VOCÊ TERÁ ACESSO (Foto 1 - Lista) ---
    with st.container():
        st.markdown("""
        <div class='premium-card'>
            <h4>E o que você terá acesso?</h4>
            <ul>
                <li>✅ <b>Artes Profissionais:</b> Mais de 2.000 artes prontas.</li>
                <li>✅ <b>Atualizações Semanais:</b> Novos conteúdos toda semana.</li>
                <li>✅ <b>Vídeo Aulas Exclusivas:</b> Aprenda a dominar o Canva.</li>
                <li>✅ <b>Suporte Prioritário:</b> Contato direto via WhatsApp.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    # --- SEÇÃO 3: GALERIA (Foto 2) ---
    st.markdown("### Essas são apenas algumas das artes que te esperam!")
    col1, col2, col3 = st.columns(3)
    # Aqui você usará as artes em 1:1 conforme o combinado
    with col1: st.image("https://via.placeholder.com/400x600") 
    with col2: st.image("https://via.placeholder.com/400x600")
    with col3: st.image("https://via.placeholder.com/400x600")

    # --- SEÇÃO 4: BÔNUS (Foto 3) ---
    st.markdown("<h2 style='text-align: center;'>Agindo agora você recebe BÔNUS incríveis!</h2>", unsafe_allow_html=True)
    
    for i, bonus in enumerate(["Sites CANVA", "Curso ADS", "Kit Ministério Infantil"]):
        st.markdown(f"""
        <div class='premium-card'>
            <span style='color: #FF2D95; font-weight: bold;'>Bônus #{i+1}</span>
            <h4>{bonus} para Igrejas</h4>
            <p>Descrição curta do bônus para gerar valor ao irmão.</p>
        </div>
        """, unsafe_allow_html=True)

    # --- SEÇÃO 5: PLANOS E FAQ (Foto 4) ---
    st.markdown("<h2 style='text-align: center;'>Escolha o Melhor Plano pra Você!</h2>", unsafe_allow_html=True)
    plan1, plan2, plan3 = st.columns(3)
    with plan1:
        st.markdown("<div class='premium-card' style='text-align: center;'><b>START</b><br>R$ 27</div>", unsafe_allow_html=True)
    with plan2:
        st.markdown("<div class='premium-card' style='text-align: center; border-color: #FF2D95;'><b>PREMIUM</b><br>R$ 57</div>", unsafe_allow_html=True)
    with plan3:
        st.markdown("<div class='premium-card' style='text-align: center;'><b>EXCLUSIVE</b><br>R$ 97</div>", unsafe_allow_html=True)

    # FAQ com Expanders do Streamlit
    st.markdown("### PERGUNTAS FREQUENTES")
    with st.expander("Como recebo meu acesso?"):
        st.write("O acesso é enviado imediatamente após a confirmação do pagamento via Hotmart.")
