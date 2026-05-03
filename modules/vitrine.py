# modules/vitrine.py
import streamlit as st

def exibir():
    # --- SEÇÃO 1: HERO (Foto 1) ---
    st.markdown("<h1 class='gradient-title'>Mais de 2.000 Artes <br> Profissionais para Igrejas.</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; color: #FF2D95;'>Atualizações Semanais!</h3>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>Transforme suas divulgações em minutos com o <b>maior acervo de artes gospel</b> editáveis do Brasil.</p>", unsafe_allow_html=True)
    
    # Mockup Central (Vídeo ou Imagem Principal)
    st.image("assets/hero_mockup.png", use_container_width=True) # Certifique-se de ter essa imagem
    
    st.markdown("""
        <div style='text-align: center; margin: 20px 0;'>
            <span style='text-decoration: line-through; color: #888;'>De R$ 197 por apenas</span>
            <div style='font-size: 3rem; font-weight: bold; color: #fff;'>R$ 27</div>
            <p style='font-size: 0.9rem;'>Comece hoje e nunca mais dependa de designers!</p>
        </div>
    """, unsafe_allow_html=True)
    
    if st.button("🚀 QUERO ACESSAR AGORA MESMO", use_container_width=True):
        st.link_button("Ir para o Pagamento", "SUA_URL_DA_HOTMART_AQUI")

    # --- SEÇÃO 2: O QUE VOCÊ TERÁ ACESSO (Foto 1 - Lista) ---
    st.markdown("""
        <div class='premium-card'>
            <h3 style='text-align: center;'>E o que você terá acesso?</h3>
            <ul style='list-style: none; padding: 0;'>
                <li>✅ <b>Artes Profissionais:</b> Mais de 2.000 artes profissionais prontas para editar no Canva.</li>
                <li>✅ <b>Atualizações Semanais:</b> Novas artes e materiais toda semana! Sempre se renovando.</li>
                <li>✅ <b>Vídeo Aulas Exclusivas:</b> Aprenda a dominar o Canva e outras ferramentas com aulas diretas.</li>
                <li>✅ <b>Bônus Exclusivos para Membros:</b> Pacote completo de recursos: fontes, texturas, elementos 3D.</li>
                <li>✅ <b>Suporte Prioritário:</b> Precisa de ajuda? Fale com a gente! Suporte rápido via WhatsApp.</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)

    # --- SEÇÃO 3: GALERIA (Foto 2) ---
    st.markdown("<h2 style='text-align: center;'>Essas são apenas algumas das artes que te esperam!</h2>", unsafe_allow_html=True)
    # Criando uma grade de imagens (3 colunas x 2 linhas de exemplo)
    col1, col2, col3 = st.columns(3)
    with col1: st.image("assets/exemplo1.png", use_container_width=True)
    with col2: st.image("assets/exemplo2.png", use_container_width=True)
    with col3: st.image("assets/exemplo3.png", use_container_width=True)
    
    col4, col5, col6 = st.columns(3)
    with col4: st.image("assets/exemplo4.png", use_container_width=True)
    with col5: st.image("assets/exemplo5.png", use_container_width=True)
    with col6: st.image("assets/exemplo6.png", use_container_width=True)

    # --- SEÇÃO 4: BÔNUS (Foto 3) ---
    st.markdown("""
        <div style='background: linear-gradient(90deg, #7B2CBF, #FF2D95); padding: 10px; border-radius: 5px; text-align: center; margin: 40px 0;'>
            <h3 style='color: white; margin: 0;'>Agindo agora você também irá receber um pacote de bônus incríveis!</h3>
        </div>
    """, unsafe_allow_html=True)

    bonuses = [
        ("Bônus #1", "Sites CANVA para Igrejas", "Um pacote de sites para igrejas que você poderá editar de forma simples."),
        ("Bônus #2", "Curso ADS para Igrejas", "Aprenda a anunciar os eventos da sua igreja pelo Meta Ads."),
        ("Bônus #3", "Kit Ministério Infantil", "Material exclusivo com atividades bíblicas, desenhos para colorir e recursos.")
    ]

    for tag, title, desc in bonuses:
        st.markdown(f"""
            <div class='premium-card'>
                <span style='color: #FF2D95; font-weight: bold;'>{tag}</span>
                <h4>{title}</h4>
                <p>{desc}</p>
            </div>
        """, unsafe_allow_html=True)

    # --- SEÇÃO 5: PLANOS (Foto 4) ---
    st.markdown("<h2 style='text-align: center;'>Escolha o Melhor Plano pra Você!</h2>", unsafe_allow_html=True)
    p1, p2, p3 = st.columns(3)
    
    with p1:
        st.markdown("<div class='premium-card' style='text-align: center;'><b>PLANO START</b><br><span style='font-size: 1.5rem;'>R$ 27</span><br><small>3 Meses de Acesso</small></div>", unsafe_allow_html=True)
        st.button("QUERO O START", key="btn_p1", use_container_width=True)
        
    with p2:
        st.markdown("<div class='premium-card' style='text-align: center; border-color: #FF2D95;'><b>PLANO PREMIUM</b><br><span style='font-size: 1.5rem; color: #FF2D95;'>R$ 57</span><br><small>1 Ano de Acesso</small></div>", unsafe_allow_html=True)
        st.button("QUERO O PREMIUM", key="btn_p2", use_container_width=True)
        
    with p3:
        st.markdown("<div class='premium-card' style='text-align: center;'><b>PLANO EXCLUSIVE</b><br><span style='font-size: 1.5rem;'>R$ 97</span><br><small>Acesso Vitalício</small></div>", unsafe_allow_html=True)
        st.button("QUERO O EXCLUSIVE", key="btn_p3", use_container_width=True)

    # --- SEÇÃO 6: FAQ ---
    st.markdown("<h3 style='text-align: center; margin-top: 50px;'>PERGUNTAS FREQUENTES</h3>", unsafe_allow_html=True)
    with st.expander("COMO RECEBO MEU ACESSO?"):
        st.write("Imediatamente após a confirmação do pagamento via Hotmart.")
    with st.expander("POR QUANTO TEMPO VOU TER ACESSO?"):
        st.write("Depende do plano escolhido: 3 meses, 1 ano ou vitalício.")
    with st.expander("CONSIGO EDITAR PELO CELULAR?"):
        st.write("Sim! Todos os templates são 100% compatíveis com o app do Canva no celular.")

    # --- RODAPÉ ---
    st.markdown("---")
    col_f1, col_f2 = st.columns([2, 1])
    with col_f1:
        st.markdown("<b>FICOU COM DÚVIDA?</b><br>Entre em contato conosco através do WhatsApp.", unsafe_allow_html=True)
    with col_f2:
        st.link_button("💬 ATENDIMENTO WHATSAPP", "https://wa.me/SEU_NUMERO")
