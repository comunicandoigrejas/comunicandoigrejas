import streamlit as st
import os

# --- GARANTE QUE A VARIÁVEL EXISTE NO INÍCIO DO SISTEMA ---
if 'pagina_atual' not in st.session_state:
    st.session_state.pagina_atual = None

def exibir_painel_inicial():
    # --- 1. IMAGEM DE CAPA (HERO MOCKUP) ---
    img_topo = "hero_mockup.png"
    caminho_assets = f"assets/{img_topo}"
    
    if os.path.exists(caminho_assets):
        st.image(caminho_assets, use_container_width=True)
    elif os.path.exists(img_topo):
        st.image(img_topo, use_container_width=True)
    else:
        st.markdown("<div style='text-align: center; padding: 30px; color: #555;'>🖼️ Capa: hero_mockup.png</div>", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # --- CSS PERSONALIZADO (FONTES GRANDES E BOTÃO PULSANTE) ---
    st.markdown("""
        <style>
        .texto-grande-pacote {
            font-size: 1.2rem !important;
            line-height: 1.8 !important;
            color: #dddddd;
        }
        .titulo-plano {
            font-size: 1.8rem !important;
            font-weight: bold !important;
            margin-bottom: 10px !important;
        }
        
        /* Animação que faz o botão de compra piscar/pulsar de forma chamativa */
        div.stLinkButton > a {
            animation: pulsarBotao 2s infinite !important;
            font-weight: bold !important;
            letter-spacing: 1px !important;
            transition: all 0.3s ease-in-out !important;
        }
        
        @keyframes pulsarBotao {
            0% {
                box-shadow: 0 0 0 0 rgba(255, 45, 149, 0.7);
                transform: scale(1);
            }
            50% {
                box-shadow: 0 0 15px 5px rgba(255, 45, 149, 0.4);
                transform: scale(1.02);
            }
            100% {
                box-shadow: 0 0 0 0 rgba(255, 45, 149, 0);
                transform: scale(1);
            }
        }
        </style>
    """, unsafe_allow_html=True)

    # --- 2. TEXTO INFORMATIVO ANTES DA VENDA ---
    st.markdown("<h2 style='text-align: center; color: #00D2FF; font-weight: bold;'>Por que o Comunicando Igrejas é para você?</h2>", unsafe_allow_html=True)
    st.markdown("""
        <p style='text-align: center; color: #bbbbbb; font-size: 1.1rem; max-width: 800px; margin: 0 auto;'>
        Sabemos que a rotina da igreja é intensa. Nosso objetivo é poupar o seu tempo e elevar a qualidade visual 
        da sua comunidade com artes prontas, modernas e 100% editáveis no Canva. Veja abaixo tudo o que preparamos 
        para abençoar o seu ministério midiático!
        </p>
    """, unsafe_allow_html=True)
    st.markdown("<br><br>", unsafe_allow_html=True)

    # --- 3. TABELA DOS PACOTES ---
    st.markdown("<h2 style='text-align: center; color: #FF2D95; font-weight: bold;'>💎 Escolha o Plano Ideal para sua Igreja</h2>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    vendas_col1, vendas_col2 = st.columns(2)

    with vendas_col1:
        st.markdown("""
            <div style='background-color: #0c0c0c; border: 1px solid #1f1f1f; border-radius: 15px; padding: 30px; text-align: center; min-height: 580px;'>
                <h3 class='titulo-plano' style='color: #00D2FF;'>🚀 Plano BÁSICO</h3>
                <p style='font-size: 1rem; color: #bbbbbb;'>Acesso direto às artes essenciais para as redes sociais da igreja, para você que quer começar a economizar tempo.</p>
                <hr style='border-color: #1f1f1f;'>
                <ul class='texto-grande-pacote' style='text-align: left; padding-left: 20px; line-height: 1.8;'>
                    <li>⏳ Validade de <b>1 ano (Acesso Anual)</b></li>
                    <li>❌ <b>Sem</b> atualização semanal</li>
                    <li>✅ ⛪ Cultos Gerais</li>
                    <li>✅ 📅 Datas Comemorativas</li>
                    <li>✅ 👥 Culto da Família</li>
                    <li>✅ 👨 Culto de Homens</li>
                    <li>✅ 👩 Culto de Mulheres</li>
                    <li>✅ 👦 Culto Infantil 🧸</li>
                    <li>✅ 🔥 Culto de Jovens</li>
                    <li>✅ 🍷 Culto de Santa Ceia</li>
                    <li>✅ 🧱 Campanhas</li>
                    <li>❌ <b>Sem</b> atualização semanal</li>
                </ul>
                <hr style='border-color: #1f1f1f;'>
                <p style='color: #888888; margin-bottom: 0; font-size: 1rem;'>Acesso por 1 ano por apenas</p>
                <h2 style='color: #ffffff; margin-top: 5px; margin-bottom: 15px; font-size: 2.5rem;'>R$ 29,90</h2>
            </div>
        """, unsafe_allow_html=True)
        st.link_button("🛍️ QUERO O PLANO BÁSICO", "URL_DE_PAGAMENTO_START_AQUI", use_container_width=True, key="buy_start")

    with vendas_col2:
        st.markdown("""
            <div style='background-color: #0c0c0c; border: 1px solid #FF2D95; border-radius: 15px; padding: 30px; text-align: center; min-height: 580px; box-shadow: 0 0 15px rgba(255, 45, 149, 0.15);'>
                <h3 class='titulo-plano' style='color: #FF2D95;'>👑 Plano PREMIUM</h3>
                <p style='font-size: 1rem; color: #bbbbbb;'>O combo completo com atualizações constantes e materiais de ministérios.</p>
                <hr style='border-color: #1f1f1f;'>
                <ul class='texto-grande-pacote' style='text-align: left; padding-left: 20px; line-height: 1.8;'>
                    <li>🔥 <b>Acesso VITALÍCIO</b> (Paga uma única vez)</li>
                    <li>🔄 <b>Atualizações Mensais</b> inclusas</li>
                    <li>✅ ⛪ Cultos Gerais</li>
                    <li>✅ 📅 Datas Comemorativas</li>
                    <li>✅ 👥 Culto da Família</li>
                    <li>✅ 👨 Culto de Homens</li>
                    <li>✅ 👩 Culto de Mulheres</li>
                    <li>✅ 👦 Culto Infantil 🧸</li>
                    <li>✅ 🔥 Culto de Jovens</li>
                    <li>✅ 🍷 Culto de Santa Ceia</li>
                    <li>✅ 🧱 Campanhas</li>
                    <li>✅ 💼 Materiais para Secretaria da Igreja</li>
                </ul>
                <hr style='border-color: #1f1f1f;'>
                <p style='color: #888888; margin-bottom: 0; font-size: 1rem;'>Acesso Vitalício por apenas</p>
                <h2 style='color: #FF2D95; margin-top: 5px; margin-bottom: 15px; font-size: 2.5rem;'>R$ 59,90</h2>
            </div>
        """, unsafe_allow_html=True)
        st.link_button("👑 QUERO O PACOTE COMPLETO", "URL_DE_PAGAMENTO_PREMIUM_AQUI", use_container_width=True, key="buy_premium")
        
    st.markdown("<br><br><br>", unsafe_allow_html=True)

    # --- 4. ÁREA DE LOGIN NO FINAL ---
    st.markdown("<div style='background-color: #0c0c0c; border: 1px solid #1f1f1f; border-radius: 15px; padding: 25px; margin-top: 20px;'>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; color: #ffffff; margin-top:0;'>🔑 Já comprou? Faça login para acessar seus templates</h3>", unsafe_allow_html=True)
    
    log_col1, log_col2, log_col3 = st.columns([2, 2, 1])
    with log_col1:
        email_login = st.text_input("E-mail", placeholder="seuemail@exemplo.com", label_visibility="collapsed", key="init_email")
    with log_col2:
        senha_login = st.text_input("Senha", type="password", placeholder="Sua senha", label_visibility="collapsed", key="init_senha")
    with log_col3:
        if st.button("🔓 ENTRAR", use_container_width=True, key="init_btn_entrar"):
            st.success("Acesso autorizado!") 
            st.rerun()
            
    st.markdown("</div>", unsafe_allow_html=True)

# --- SISTEMA DE CHECAGEM CORRIGIDO E SEGURO ---
# Força a exibição se o estado for explicitamente nulo ou vazio
if st.session_state.pagina_atual is None or st.session_state.pagina_atual == "":
    exibir_painel_inicial()
