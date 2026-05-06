# modules/vitrine.py
import streamlit as st
import os

def exibir():
    def carregar_imagem(nome_arquivo):
        caminho = f"assets/{nome_arquivo}"
        if os.path.exists(caminho):
            st.image(caminho, use_container_width=True)
        else:
            st.info(f"Aguardando imagem: {nome_arquivo}")

    # --- 1. BANNER DE TOPO ---
    carregar_imagem("hero_mockup.png")

    # --- 2. NOVA SEÇÃO: O QUE VOCÊ TERÁ ACESSO? ---
    # Usando container para forçar a renderização
    with st.container():
        st.markdown("""
            <div style='background-color: #000000; border: 2px solid #333333; border-radius: 15px; padding: 30px; margin-top: 20px; margin-bottom: 20px; font-family: sans-serif;'>
                <h2 style='text-align: center; color: #ffffff; margin-bottom: 30px;'>E o que você terá acesso?</h2>
                
                <div style='margin-bottom: 20px;'>
                    <span style='color: #FF2D95; font-weight: bold; font-size: 1.2rem;'>✅ Artes Profissionais:</span><br>
                    <span style='color: #dddddd; font-size: 1rem;'>Você terá acesso a mais de 2.000 artes profissionais prontas para editar no Canva. Em poucos cliques, crie artes incríveis de forma rápida, simples e sem nenhuma complicação!</span>
                </div>

                <div style='margin-bottom: 20px;'>
                    <span style='color: #FF2D95; font-weight: bold; font-size: 1.2rem;'>✅ Atualizações Semanais:</span><br>
                    <span style='color: #dddddd; font-size: 1rem;'>Novas artes e materiais toda semana! A plataforma está sempre se renovando para que sua comunicação continue atual, relevante e poderosa.</span>
                </div>

                <div style='margin-bottom: 20px;'>
                    <span style='color: #FF2D95; font-weight: bold; font-size: 1.2rem;'>✅ Vídeo Aulas Exclusivas:</span><br>
                    <span style='color: #dddddd; font-size: 1rem;'>Aprenda a dominar o Canva e outras ferramentas com aulas simples e diretas, pensadas especialmente para igrejas e ministérios. Mesmo sem experiência, você vai conseguir criar artes de alto nível!</span>
                </div>

                <div style='margin-bottom: 20px;'>
                    <span style='color: #FF2D95; font-weight: bold; font-size: 1.2rem;'>✅ Bônus Exclusivos para Membros:</span><br>
                    <span style='color: #dddddd; font-size: 1rem;'>Receba um pacote completo de recursos extras! Inclui efeitos visuais, textos em 3D, texturas, vídeos, imagens de fundo e muito mais.</span>
                </div>

                <div style='margin-bottom: 10px;'>
                    <span style='color: #FF2D95; font-weight: bold; font-size: 1.2rem;'>✅ Suporte Prioritário:</span><br>
                    <span style='color: #dddddd; font-size: 1rem;'>Precisa de ajuda? Fale com a gente! Os membros da plataforma têm acesso ao nosso time com suporte rápido e eficiente pelo WhatsApp.</span>
                </div>
            </div>
        """, unsafe_allow_html=True)

    # --- 3. TÍTULO DE CHAMADA ---
    st.markdown("<h1 class='gradient-title'>Invista na sua Igreja</h1>", unsafe_allow_html=True)
    
    # --- 4. PREÇO DESTAQUE ---
    st.markdown(f"""
        <div style='text-align: center; margin: 20px 0; padding: 25px; border: 2px dashed #7B2CBF; border-radius: 15px; background-color: #0a0a0a;'>
            <div style='font-size: 3.5rem; font-weight: 800; color: #FF2D95; text-shadow: 0 0 15px rgba(255, 45, 149, 0.5);'>
                A partir de R$ 27,00
            </div>
        </div>
    """, unsafe_allow_html=True)
    # --- 6. MODELOS (AMOSTRAS) ---
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
