# modules/vitrine.py
import streamlit as st
import os

def exibir():
    # Função para carregar imagens com segurança
    def carregar_imagem(nome_arquivo):
        caminho = f"assets/{nome_arquivo}"
        if os.path.exists(caminho):
            st.image(caminho, use_container_width=True)
        else:
            st.info(f"Aguardando imagem: {nome_arquivo}")

    # --- BANNER PRINCIPAL ---
    carregar_imagem("hero_mockup.png")

    # --- TÍTULO E PREÇO EM DESTAQUE ---
    st.markdown("<h1 class='gradient-title'>Mais de 2.000 Artes <br> Profissionais para Igrejas.</h1>", unsafe_allow_html=True)
    
    st.markdown("""
        <div style='text-align: center; margin: 20px 0; padding: 25px; border: 2px dashed #7B2CBF; border-radius: 15px; background-color: #0a0a0a;'>
            <span style='text-decoration: line-through; color: #888; font-size: 1.1rem;'>Invista na sua comunicação</span>
            <div style='font-size: 3.5rem; font-weight: 800; color: #FF2D95; text-shadow: 0 0 15px rgba(255, 45, 149, 0.5);'>
                A partir de R$ 27,00
            </div>
            <p style='color: #fff; font-size: 1.1rem;'>ESCOLHA O MELHOR PLANO PARA VOCÊ!</p>
        </div>
    """, unsafe_allow_html=True)

    # --- GALERIA DE AMOSTRAS (01 a 04) ---
    st.markdown("<br><h2 style='text-align: center;'>Artes prontas para o seu Instagram:</h2>", unsafe_allow_html=True)
    respiro_e, c1, c2, c3, c4, respiro_d = st.columns([0.5, 2, 2, 2, 2, 0.5])
    with c1: carregar_imagem("1.png")
    with c2: carregar_imagem("2.png")
    with c3: carregar_imagem("3.png")
    with c4: carregar_imagem("4.png")

    # --- SEÇÃO DE PLANOS (Onde estava o problema) ---
    st.markdown("<br><h2 style='text-align: center;'>Planos Disponíveis</h2>", unsafe_allow_html=True)
    
    col_plan1, col_plan2 = st.columns(2)

    # --- PLANO START ---
    with col_plan1:
        st.markdown("""
            <div class='premium-card' style='text-align: center; border-color: #7B2CBF; min-height: 800px;'>
                <div style='background-color: white; color: black; padding: 10px; border-radius: 5px; font-weight: bold;'>
                    PLANO: START<br>(3 Meses de Acesso)
                </div>
                <div style='font-size: 3.5rem; font-weight: 800; color: #fff; margin-top: 15px;'>R$ 27</div>
                <p style='color: #888;'>OU 5x R$ 6,17</p>
                <hr style='border-color: #333;'>
                <ul style='list-style: none; padding: 0; text-align: left; color: #ddd; font-size: 1.8rem;'>
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
        """, unsafe_allow_html=True)
        st.link_button("GARANTIR ACESSO START", "https://pay.hotmart.com/Y98906000N", use_container_width=True)

    # --- PLANO PREMIUM ---
    with col_plan2:
        st.markdown("""
            <div class='premium-card' style='text-align: center; border-color: #FF2D95; background-color: #0e0e0e; min-height: 800px; position: relative;'>
                <div style='position: absolute; top: 10px; right: 10px; background-color: #28a745; color: white; padding: 5px 10px; border-radius: 5px; font-size: 1.8rem;'>+ VENDIDO</div>
                <div style='background: linear-gradient(90deg, #7B2CBF, #FF2D95); color: white; padding: 10px; border-radius: 5px; font-weight: bold;'>
                    PLANO: PREMIUM 🔥<br>(ACESSO VITALÍCIO)
                </div>
                <div style='font-size: 3.5rem; font-weight: 800; color: #fff; margin-top: 15px;'>R$ 57</div>
                <p style='color: #888;'>OU 11x R$ 6,25</p>
                <hr style='border-color: #333;'>
                <ul style='list-style: none; padding: 0; text-align: left; color: #ddd; font-size: 1.8rem;'>
                    <li>🚀 <b>DIFERENCIAL: NUNCA EXPIRA!</b></li>
                    <li>✅ <b>Tudo do Plano Start</b></li>
                    <li>✅ Atualizações Vitalícias</li>
                    <li>✅ Suporte Prioritário Vitalício</li>
                    <li>✅ Acesso a futuros lançamentos</li>
                    <li>✅ Sem taxas de renovação</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)
        st.link_button("GARANTIR ACESSO VITALÍCIO", "https://pay.hotmart.com/LINK_PREMIUM", use_container_width=True)

    st.markdown("<br><hr>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>Comunicando Igrejas - 2026</p>", unsafe_allow_html=True)
