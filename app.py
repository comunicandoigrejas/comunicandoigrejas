import streamlit as st
import os

def exibir_painel_inicial():
    # --- 1. IMAGEM DE CAPA (HERO MOCKUP) ---
    # Busca automática do arquivo nas extensões e pastas do projeto
    img_topo = "hero_mockup.png"
    caminho_assets = f"assets/{img_topo}"
    
    if os.path.exists(caminho_assets):
        st.image(caminho_assets, use_container_width=True)
    elif os.path.exists(img_topo):
        st.image(img_topo, use_container_width=True)
    else:
        # Espaço reservado caso o arquivo ainda não tenha subido para o GitHub
        st.markdown("<div style='text-align: center; padding: 30px; color: #555;'>🖼️ Capa: hero_mockup.png</div>", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # --- 2. ÁREA DE LOGIN INTERNA ---
    st.markdown("<div style='background-color: #0c0c0c; border: 1px solid #1f1f1f; border-radius: 15px; padding: 20px; margin-bottom: 30px;'>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; color: #ffffff; margin-top:0;'>🔑 Já é membro? Faça seu Login</h3>", unsafe_allow_html=True)
    
    # Campos horizontais e modernos para o utilizador entrar
    log_col1, log_col2, log_col3 = st.columns([2, 2, 1])
    with log_col1:
        email_login = st.text_input("E-mail", placeholder="seuemail@exemplo.com", label_visibility="collapsed", key="init_email")
    with log_col2:
        senha_login = st.text_input("Senha", type="password", placeholder="Sua senha", label_visibility="collapsed", key="init_senha")
    with log_col3:
        if st.button("🔓 ENTRAR", use_container_width=True, key="init_btn_entrar"):
            # Aqui liga-se à sua lógica de verificação (ex: auth.py)
            st.success("Acesso autorizado!") 
            st.rerun()
            
    st.markdown("</div>", unsafe_allow_html=True)

    # --- 3. EXIBIÇÃO DOS PLANOS E BOTÕES DE COMPRA ---
    st.markdown("<h2 style='text-align: center; color: #FF2D95; font-weight: bold;'>💎 Conheça os Nossos Planos</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #888888;'>Tenha acesso imediato às melhores artes profissionais para abençoar as redes sociais da sua igreja.</p>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    vendas_col1, vendas_col2 = st.columns(2)

    with vendas_col1:
        st.markdown("""
            <div style='background-color: #0c0c0c; border: 1px solid #1f1f1f; border-radius: 15px; padding: 25px; text-align: center; height: 380px;'>
                <h3 style='color: #00D2FF; margin-top:0;'>🚀 Plano START</h3>
                <p style='font-size: 0.9rem; color: #bbbbbb;'>Ideal para organizar as postagens semanais da sua igreja.</p>
                <hr style='border-color: #1f1f1f;'>
                <ul style='text-align: left; font-size: 0.9rem; color: #dddddd; line-height: 1.6; padding-left: 20px;'>
                    <li>✅ Acesso a <b>Cultos Gerais</b></li>
                    <li>✅ Acesso a <b>Datas Comemorativas</b></li>
                    <li>✅ Acesso a <b>Família e Homens</b></li>
                    <li>✅ Acesso a <b>Infantil</b></li>
                    <li>❌ Conteúdos de Departamentos Bloqueados</li>
                </ul>
                <hr style='border-color: #1f1f1f;'>
                <p style='color: #888888; margin-bottom: 0; font-size: 0.85rem;'>Acesso Vitalício por apenas</p>
                <h2 style='color: #ffffff; margin-top: 5px; margin-bottom: 15px;'>R$ 29,90</h2>
            </div>
        """, unsafe_allow_html=True)
        # Substitua a URL abaixo pelo link de checkout do seu meio de pagamento (ex: Kiwify, Hotmart)
        st.link_button("🛍️ QUERO O PLANO START", "URL_DE_PAGAMENTO_START_AQUI", use_container_width=True, key="buy_start")

    with vendas_col2:
        st.markdown("""
            <div style='background-color: #0c0c0c; border: 1px solid #FF2D95; border-radius: 15px; padding: 25px; text-align: center; height: 380px; box-shadow: 0 0 15px rgba(255, 45, 149, 0.15);'>
                <h3 style='color: #FF2D95; margin-top:0;'>👑 Plano PREMIUM</h3>
                <p style='font-size: 0.9rem; color: #bbbbbb;'>O pacote completo com atualizações e artes exclusivas de ministérios.</p>
                <hr style='border-color: #1f1f1f;'>
                <ul style='text-align: left; font-size: 0.9rem; color: #dddddd; line-height: 1.6; padding-left: 20px;'>
                    <li>✅ <b>Todos os benefícios</b> do plano Start</li>
                    <li>🔥 Acesso exclusivo ao módulo de <b>Jovens</b></li>
                    <li>🌸 Acesso exclusivo ao módulo de <b>Mulheres</b></li>
                    <li>🍷 Acesso exclusivo ao módulo de <b>Santa Ceia</b></li>
                    <li>✨ Suporte premium e atualizações contínuas</li>
                </ul>
                <hr style='border-color: #1f1f1f;'>
                <p style='color: #888888; margin-bottom: 0; font-size: 0.85rem;'>Acesso Vitalício por apenas</p>
                <h2 style='color: #FF2D95; margin-top: 5px; margin-bottom: 15px;'>R$ 59,90</h2>
            </div>
        """, unsafe_allow_html=True)
        # Substitua a URL abaixo pelo link de checkout do plano completo
        st.link_button("👑 QUERO O PACOTE COMPLETO", "URL_DE_PAGAMENTO_PREMIUM_AQUI", use_container_width=True, key="buy_premium")
        
    st.markdown("<br>", unsafe_allow_html=True)

# --- CONTROLO DE EXIBIÇÃO NO SEU DASHBOARD ---
# Lembre-se de usar esta condicional para que o painel só apareça se nenhuma categoria estiver aberta:
if not st.session_state.get('pagina_atual'):
    exibir_painel_inicial()
