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
    carregar_imagem("banner_principal.png")

    # 2. NOVA SEÇÃO: O QUE VOCÊ TERÁ ACESSO?
    st.markdown("""
        <div style='background-color: #000; border: 1px solid #333; border-radius: 15px; padding: 10px; margin: 20px 0;'>
            <h1 style='text-align: center; color: white;'>E o que você terá acesso?</h2>
            <p style='color: #FF2D95; font-weight: bold; margin-bottom: 0;'>✅ Artes Profissionais:</p>
            <p style='color: #ddd; font-size: 18px; margin-top: 5px;'>Você terá acesso a mais de 2.000 artes profissionais prontas para editar no Canva. 
            Em poucos cliques, crie artes incríveis de forma rápida, simples e sem nenhuma complicação!</p>
            <p style='color: #FF2D95; font-weight: bold; margin-bottom: 0;'>✅ Atualizações Semanais:</p>
            <p style='color: #ddd; font-size: 18px; margin-top: 5px;'>Novas artes e materiais toda semana! A plataforma está sempre se renovando para que sua 
            comunicação continue atual, relevante e poderosa.</p>
            <p style='color: #FF2D95; font-weight: bold; margin-bottom: 0;'>✅ Vídeo Aulas Exclusivas:</p>
            <p style='color: #ddd; font-size: 18px; margin-top: 5px;'>Aprenda a dominar o Canva e outras ferramentas com aulas simples e diretas, pensadas 
            especialmente para igrejas e ministérios. Mesmo sem experiência, você vai conseguir criar artes de alto nível!</p>
            <p style='color: #FF2D95; font-weight: bold; margin-bottom: 0;'>✅ Bônus Exclusivos:</p>
            <p style='color: #ddd; font-size: 18px; margin-top: 5px;'>Receba um pacote completo de recursos extras! Inclui efeitos visuais, textos em 3D, texturas, vídeos, 
            imagens de fundo e muito mais para deixar suas artes ainda mais impactantes e profissionais.</p>
            <p style='color: #FF2D95; font-weight: bold; margin-bottom: 0;'>✅ Suporte Prioritário:</p>
            <p style='color: #ddd; font-size: 18px; margin-top: 5px;'>Precisa de ajuda? Fale com a gente! Os membros da plataforma têm acesso ao nosso time 
            com suporte rápido e eficiente pelo WhatsApp.</p>
        </div>
    """, unsafe_allow_html=True)

    # 3. CHAMADA DE PREÇO
    st.markdown("<h1 style='text-align: center;'>A partir de R$ 27,00</h1>", unsafe_allow_html=True)

    # 4. PLANOS
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("<div style='border:1px solid #7B2CBF; padding:20px; border-radius:10px; text-align:center;'><h3>START</h3><p>R$ 27</p></div>", unsafe_allow_html=True)
        st.link_button("GARANTIR ACESSO START", "https://pay.hotmart.com/Y98906000N", use_container_width=True)
    with col2:
        st.markdown("<div style='border:1px solid #FF2D95; padding:20px; border-radius:10px; text-align:center;'><h3>PREMIUM 🔥</h3><p>R$ 57</p></div>", unsafe_allow_html=True)
        st.link_button("GARANTIR ACESSO VITALÍCIO", "https://pay.hotmart.com/Y98906000N", use_container_width=True)

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
