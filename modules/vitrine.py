import streamlit as st
import os

def exibir():
    # Tudo o que está aqui dentro tem 4 espaços de recuo
    def carregar_imagem(nome_arquivo):
        # Tudo o que está dentro desta subfunção tem 8 espaços de recuo
        caminho = f"assets/{nome_arquivo}"
        if os.path.exists(caminho):
            st.image(caminho, use_container_width=True)
        else:
            st.info(f"Aguardando imagem: {nome_arquivo}")

    # 1. BANNER PRINCIPAL
    carregar_imagem("hero_mockup.png")

   # --- 2. NOVA SEÇÃO: O QUE VOCÊ TERÁ ACESSO? (Versão Estreita e Corrigida) ---
    respiro_esq, centro, respiro_dir = st.columns([0.6, 1.8, 0.6])

    with centro:
        st.html("""
            <div style='background-color: #000; border: 1px solid #333; border-radius: 15px; padding: 25px; margin: 20px 0; font-family: sans-serif;'>
                <h2 style='text-align: center; color: white; margin-bottom: 25px;'>E o que você terá acesso?</h2>
                
                <div style='margin-bottom: 15px;'>
                    <p style='color: #FF2D95; font-weight: bold; margin-bottom: 0; font-size: 18px;'>✅ Artes Profissionais:</p>
                    <p style='color: #ddd; font-size: 16px; margin-top: 5px; line-height: 1.4;'>Mais de 2.000 artes profissionais prontas para editar no Canva. De forma rápida e simples!</p>
                </div>

                <div style='margin-bottom: 15px;'>
                    <p style='color: #FF2D95; font-weight: bold; margin-bottom: 0; font-size: 18px;'>✅ Atualizações Semanais:</p>
                    <p style='color: #ddd; font-size: 16px; margin-top: 5px; line-height: 1.4;'>Novas artes e materiais toda semana! Sua comunicação sempre atualizada.</p>
                </div>

                <div style='margin-bottom: 15px;'>
                    <p style='color: #FF2D95; font-weight: bold; margin-bottom: 0; font-size: 18px;'>✅ Vídeo Aulas Exclusivas:</p>
                    <p style='color: #ddd; font-size: 16px; margin-top: 5px; line-height: 1.4;'>Aprenda a dominar o Canva com aulas pensadas para igrejas e ministérios.</p>
                </div>

                <div style='margin-bottom: 15px;'>
                    <p style='color: #FF2D95; font-weight: bold; margin-bottom: 0; font-size: 18px;'>✅ Bônus Exclusivos:</p>
                    <p style='color: #ddd; font-size: 16px; margin-top: 5px; line-height: 1.4;'>Efeitos visuais, textos em 3D, texturas, vídeos e imagens de fundo.</p>
                </div>

                <div style='margin-bottom: 5px;'>
                    <p style='color: #FF2D95; font-weight: bold; margin-bottom: 0; font-size: 18px;'>✅ Suporte Prioritário:</p>
                    <p style='color: #ddd; font-size: 16px; margin-top: 5px; line-height: 1.4;'>Dúvidas? Fale com a gente! Suporte rápido e eficiente pelo WhatsApp.</p>
                </div>
            </div>
        """)

   # 3. CHAMADA DE PREÇO COM RETÂNGULO VERDE FLUORESCENTE
    st.markdown("""
        <div style='
            border: 3px solid #00FF00; 
            padding: 20px; 
            border-radius: 15px; 
            text-align: center; 
            margin: 25px 0;
            box-shadow: 0 0 15px #00FF00;
            background-color: rgba(0, 255, 0, 0.05);
        '>
            <h1 style='margin: 0; color: white; font-size: 2.5rem;'>
                A partir de <span style='color: #00FF00;'>R$ 27,00</span>
            </h1>
        </div>
    """, unsafe_allow_html=True)

    # 5. MODELOS
    st.markdown("<br><h2 style='text-align: center;'>Veja a qualidade das nossas artes:</h2>", unsafe_allow_html=True)
    c1, c2, c3, c4 = st.columns(4)
    with c1: carregar_imagem("1.png")
    with c2: carregar_imagem("2.png")
    with c3: carregar_imagem("3.png")
    with c4: carregar_imagem("4.png")
  # --- SEÇÃO DE PLANOS ---
    st.markdown("<br><h2 style='text-align: center;'>Planos Disponíveis</h2>", unsafe_allow_html=True)
    
    col_plan1, col_plan2 = st.columns(2)

    # Conteúdo do Plano START
    html_start = """
    <div class='premium-card' style='text-align: center; border-color: #7B2CBF; min-height: 800px; padding: 20px;'>
        <div style='background-color: white; color: black; padding: 10px; border-radius: 5px; font-weight: bold; font-size: 2rem;'>
            PLANO: START<br>
            <span style='font-size: 1rem;'>(3 Meses de Acesso)</span>
        </div>
        <div style='font-size: 2.8rem; font-weight: 800; color: #fff; margin-top: 15px;'>R$ 27</div>
        <p style='color: #888; font-size: 0.95rem;'>OU 5x R$ 6,17</p>
        <hr style='border-color: #333;'>
        <ul style='list-style: none; padding: 0; text-align: left; color: #ddd; font-size: 2rem;'>
            <li>✅ +2.000 Artes Editáveis no Canva</li>
            <li>✅ 4 Formatos (Feed, Storie, Cartaz e Telão)</li>
            <li>✅ Atualizações Semanais</li>
            <li>✅ Curso Site pelo Canva</li>
            <li>✅ Templates de Site Prontos</li>
            <li>✅ Curso Anúncios (FB/IG)</li>
            <li>✅ Kit Ministério Infantil & Secretaria</li>
            <li>✅ Sermões de Pregação</li>
            <li>✅ 12 Bônus Exclusivos</li>
            <li>✅ Comunidade Vip & Suporte</li>
        </ul>
    </div>
    """

    # Conteúdo do Plano PREMIUM
    html_premium = """
    <div class='premium-card' style='text-align: center; border-color: #FF2D95; background-color: #0e0e0e; min-height: 800px; position: relative; padding: 20px;'>
        <div style='position: absolute; top: 10px; right: 10px; background-color: #28a745; color: white; padding: 5px 10px; border-radius: 5px; font-size: 0.7rem;'>+ VENDIDO</div>
        <div style='background: linear-gradient(90deg, #7B2CBF, #FF2D95); color: white; padding: 10px; border-radius: 5px; font-weight: bold; font-size: 2rem;'>
            PLANO: PREMIUM 🔥<br>
            <span style='font-size: 1rem;'>(ACESSO VITALÍCIO)</span>
        </div>
        <div style='font-size: 2.8rem; font-weight: 800; color: #fff; margin-top: 15px;'>R$ 57</div>
        <p style='color: #888; font-size: 0.95rem;'>OU 11x R$ 6,25</p>
        <hr style='border-color: #333;'>
        <ul style='list-style: none; padding: 0; text-align: left; color: #ddd; font-size: 2rem;'>
            <li>🚀 <b>DIFERENCIAL: NUNCA EXPIRA!</b></li>
            <li>✅ <b>Tudo do Plano Start</b></li>
            <li>✅ Atualizações Vitalícias</li>
            <li>✅ Suporte Prioritário Vitalício</li>
            <li>✅ Acesso a futuros lançamentos</li>
            <li>✅ Sem taxas de renovação</li>
        </ul>
    </div>
    """

    with col_plan1:
        st.markdown(html_start, unsafe_allow_html=True)
        st.link_button("GARANTIR ACESSO START", "https://pay.hotmart.com/Y98906000N", use_container_width=True)

    with col_plan2:
        st.markdown(html_premium, unsafe_allow_html=True)
        st.link_button("GARANTIR ACESSO VITALÍCIO", "https://pay.hotmart.com/Y98906000N", use_container_width=True)

# --- RODAPÉ COM CONTATOS ---
    st.markdown("<br><hr>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;'>Ficou com alguma dúvida? Fale conosco!</h3>", unsafe_allow_html=True)
    
    # Criando colunas para centralizar os botões
    col_vazia1, col_whats, col_insta, col_vazia2 = st.columns([1, 2, 2, 1])

    with col_whats:
        # Substitua o número abaixo pelo seu WhatsApp (com DDD)
        link_whatsapp = "https://wa.me/551937704733" 
        st.link_button("🟢 WHATSAPP", link_whatsapp, use_container_width=True)

    with col_insta:
        # Substitua pelo link do seu perfil
        link_instagram = "https://www.instagram.com/comunicandoigrejas"
        st.link_button("📸 INSTAGRAM", link_instagram, use_container_width=True)

    st.markdown("""
        <div style='text-align: center; color: #888; margin-top: 20px; font-size: 0.9rem;'>
            <p>Comunicando Igrejas © 2026 - Todos os direitos reservados</p>
        </div>
    """, unsafe_allow_html=True)
