import streamlit as st
import os

# --- CONFIGURAÇÃO DA PÁGINA (TELA AMPLA E SEM SIDEBAR) ---
st.set_page_config(
    page_title="Comunicando Igrejas",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- GARANTE QUE A VARIÁVEL EXISTE NO INÍCIO DO SISTEMA ---
if 'pagina_atual' not in st.session_state:
    st.session_state.pagina_atual = None

if 'logado' not in st.session_state:
    st.session_state.logado = False

def exibir_painel_inicial():
    # --- 1. IMAGEM DE CAPA (HERO MOCKUP) ---
    img_topo = "hero_mockup.png"
    caminho_assets = f"assets/{img_topo}"
    
    if os.path.exists(caminho_assets):
        st.image(caminho_assets, use_container_width=True)
    elif os.path.exists(img_topo):
        st.image(img_topo, use_container_width=True)
    else:
        st.markdown("<div style='text-align: center; padding: 10px; color: #555;'></div>", unsafe_allow_html=True)

    # --- CSS PERSONALIZADO (CENTRALIZAÇÃO, FONTES MAIORES E BOTÕES LUMINOSOS) ---
    st.markdown("""
        <style>
        /* Remove barras laterais e espaçamentos indesejados */
        [data-testid="stSidebar"], [data-testid="stSidebarCollapseButton"] {
            display: none !important;
        }
        .block-container {
            padding-left: 4rem !important;
            padding-right: 4rem !important;
            max-width: 100% !important;
        }
        
        .texto-grande-pacote {
            font-size: 1.15rem !important;
            line-height: 1.8 !important;
            color: #dddddd;
        }
        .titulo-plano {
            font-size: 1.8rem !important;
            font-weight: bold !important;
            margin-bottom: 10px !important;
        }
        
        /* Quadro Informativo de Acesso */
        .caixa-beneficios {
            background-color: #0c0c0c;
            border: 1px solid #333333;
            border-radius: 12px;
            padding: 35px;
            margin: 20px auto;
            max-width: 900px;
        }
        .item-beneficio {
            margin-bottom: 20px;
        }
        .titulo-beneficio {
            color: #FF2D95;
            font-weight: bold;
            font-size: 1.15rem;
            margin-bottom: 2px;
        }
        .desc-beneficio {
            color: #cccccc;
            font-size: 1.05rem;
            line-height: 1.5;
        }
        
        /* --- 1. BOTÃO DE ANCORA DO TOPO (DEGRADÊ LUMINOSO) --- */
        div.element-container:has(#btn_topo_container) + div div.stButton > button {
            background: linear-gradient(90deg, #FF2D95 0%, #00D2FF 100%) !important;
            color: #ffffff !important;
            font-weight: bold !important;
            font-size: 1.4rem !important;
            border: none !important;
            padding: 18px 30px !important;
            border-radius: 50px !important;
            letter-spacing: 1px !important;
            box-shadow: 0 0 15px #FF2D95, 0 0 30px #00D2FF !important;
            animation: glowPulsar 1.8s infinite alternate !important;
            transition: all 0.3s ease-in-out !important;
            width: 100% !important;
        }
        
        @keyframes glowPulsar {
            0% { shadow: 0 0 10px #FF2D95, 0 0 20px #00D2FF; transform: scale(1); }
            100% { box-shadow: 0 0 25px #FF2D95, 0 0 50px #00D2FF, 0 0 70px #FF2D95; transform: scale(1.03); }
        }

        /* --- 2. BOTÕES DE COMPRA FINAIS (EFEITO NEON VERDE PULSANTE) --- */
        div.stLinkButton > a {
            background: linear-gradient(90deg, #24C67D 0%, #00E676 100%) !important;
            color: #ffffff !important;
            font-weight: bold !important;
            font-size: 1.25rem !important;
            border: none !important;
            padding: 14px 28px !important;
            border-radius: 8px !important;
            letter-spacing: 1px !important;
            text-align: center !important;
            box-shadow: 0 0 15px rgba(0, 230, 118, 0.6) !important;
            animation: glowVerde 1.6s infinite alternate !important;
            transition: all 0.3s ease-in-out !important;
        }
        
        @keyframes glowVerde {
            0% { box-shadow: 0 0 8px rgba(0, 230, 118, 0.5); transform: scale(1); }
            100% { box-shadow: 0 0 22px rgba(0, 230, 118, 0.9), 0 0 35px rgba(36, 198, 125, 0.4); transform: scale(1.02); }
        }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # --- 2. CHAMADA PRINCIPAL CENTRALIZADA E AMPLIADA ---
    st.markdown("""
        <div style='text-align: center; margin-bottom: 10px;'>
            <p style='color: #a0a0a0; font-size: 1.3rem; margin-bottom: 0; text-decoration: line-through; letter-spacing: 1px;'>De R$ 197 por Apenas</p>
            <h1 style='color: #ffffff; font-size: 4.8rem; font-weight: 900; margin-top: -5px; margin-bottom: 0px; text-shadow: 0px 0px 20px rgba(255,255,255,0.2);'>R$ 29,90</h1>
            <p style='color: #00D2FF; font-size: 1.3rem; font-weight: bold; margin-top: 5px; margin-bottom: 30px; letter-spacing: 0.5px;'>Comece hoje e nunca mais dependa de designers!</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Grid auxiliar para forçar a centralização perfeita do botão no meio da tela
    col_esq, col_centro, col_dir = st.columns([1, 2, 1])
    with col_centro:
        st.markdown('<div id="btn_topo_container"></div>', unsafe_allow_html=True)
        if st.button("🚀 QUERO MEU ACESSO AGORA MESMO", key="btn_luminoso_topo", use_container_width=True):
            st.markdown("<script>window.scrollTo({top: document.body.scrollHeight, behavior: 'smooth'});</script>", unsafe_allow_html=True)
            st.components.v1.html("""<script>window.parent.document.getElementById("tabela-precos").scrollIntoView({behavior: "smooth"});</script>""", height=0)
    
    st.markdown("<br><br><br>", unsafe_allow_html=True)

    # --- 3. QUADRO INFORMATIVO: E O QUE VOCÊ TERÁ ACESSO? ---
    st.markdown("""
        <div class='caixa-beneficios'>
            <h2 style='text-align: center; color: #ffffff; font-weight: bold; margin-top: 0; margin-bottom: 30px;'>📋 E o que você terá acesso?</h2>
            <div class='item-beneficio'>
                <div class='titulo-beneficio'>⚡ Artes Profissionais:</div>
                <div class='desc-beneficio'>Você terá acesso a centenas de artes profissionais prontas para editar no Canva. Em poucos cliques, crie artes incríveis de forma rápida, simples e sem nenhuma complicação!</div>
            </div>
            <div class='item-beneficio'>
                <div class='titulo-beneficio'>🔄 Atualizações Semanais:</div>
                <div class='desc-beneficio'>Novas artes e materiais toda semana! A plataforma está sempre se renovando para que sua comunicação continue atual, relevante e poderosa.</div>
            </div>
            <div class='item-beneficio'>
                <div class='titulo-beneficio'>🎥 Vídeo Aulas Exclusivas:</div>
                <div class='desc-beneficio'>Aprenda a dominar o Canva e outras ferramentas com aulas simples e diretas, pensadas especialmente para igrejas e ministérios. Mesmo sem experiência, você vai conseguir criar artes de alto nível!</div>
            </div>
            <div class='item-beneficio'>
                <div class='titulo-beneficio'>🎁 Bônus Exclusivos para Membros:</div>
                <div class='desc-beneficio'>Receba um pacote completo de recursos extras! Inclui efeitos visuais, textos em 3D, texturas, vídeos, imagens de fundo e muito mais para deixar suas artes ainda mais impactantes.</div>
            </div>
            <div class='item-beneficio'>
                <div class='titulo-beneficio'>💬 Suporte Prioritário:</div>
                <div class='desc-beneficio'>Precisa de ajuda? Fale com a gente! Os membros da plataforma têm acesso ao nosso time com suporte rápido e eficiente pelo WhatsApp.</div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)

    # --- 4. EXIBIÇÃO DOS MODELOS DISPONÍVEIS (1.png a 4.png) ---
    st.markdown("<h2 style='text-align: center; color: #00D2FF; font-weight: bold;'>🎨 Algumas das artes que te esperam</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #888888; font-size: 1.1rem;'>Modelos modernos, atraentes e 100% editáveis para abençoar o design da sua comunidade</p>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    # Organiza as 4 artes de demonstração em colunas perfeitamente alinhadas
    amostras_cols = st.columns(4)
    imagens_amostra = ["1.png", "2.png", "3.png", "4.png"]

    for idx, img_nome in enumerate(imagens_amostra):
        with amostras_cols[idx]:
            caminho_img = f"assets/{img_nome}"
            if os.path.exists(caminho_img):
                st.image(caminho_img, use_container_width=True)
            elif os.path.exists(img_nome):
                st.image(img_nome, use_container_width=True)
            else:
                st.markdown(f"<div style='background-color: #111; padding: 80px 10px; text-align: center; border-radius: 8px; color: #444; font-size: 0.85rem;'>🖼️ {img_nome}</div>", unsafe_allow_html=True)

    st.markdown("<br><br><br><br>", unsafe_allow_html=True)

    # --- 5. TABELA DOS PACOTES (PONTO DE ANCORAGEM) ---
    st.markdown('<div id="tabela-precos"></div>', unsafe_allow_html=True)
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
        st.link_button("🛍️ QUERO O PLANO BÁSICO", "https://pay.hotmart.com/Y106003109C", use_container_width=True, key="buy_start")

    with vendas_col2:
        st.markdown("""
            <div style='background-color: #0c0c0c; border: 1px solid #FF2D95; border-radius: 15px; padding: 30px; text-align: center; min-height: 580px; box-shadow: 0 0 15px rgba(255, 45, 149, 0.15);'>
                <h3 class='titulo-plano' style='color: #FF2D95;'>👑 Plano PREMIUM</h3>
                <p style='font-size: 1rem; color: #bbbbbb;'>O combo completo com updates constantes e materiais de ministérios, para você que quer começar a economizar tempo.</p>
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
        st.link_button("👑 QUERO O PACOTE COMPLETO", "https://pay.hotmart.com/Y98906000N?off=7dey0pfj", use_container_width=True, key="buy_premium")
        
    st.markdown("<br><br><br>", unsafe_allow_html=True)

    # --- 6. ÁREA DE LOGIN NO FINAL ---
    st.markdown("<div style='background-color: #0c0c0c; border: 1px solid #1f1f1f; border-radius: 15px; padding: 25px; margin-top: 20px;'>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; color: #ffffff; margin-top:0;'>🔑 Já comprou? Faça login para acessar seus templates</h3>", unsafe_allow_html=True)
    
    log_col1, log_col2, log_col3 = st.columns([2, 2, 1])
    with log_col1:
        email_login = st.text_input("E-mail", placeholder="seuemail@exemplo.com", label_visibility="collapsed", key="init_email")
    with log_col2:
        senha_login = st.text_input("Senha", type="password", placeholder="Sua senha", label_visibility="collapsed", key="init_senha")
    with log_col3:
        if st.button("🔓 ENTRAR", use_container_width=True, key="init_btn_entrar"):
            if email_login != "" and senha_login != "":
                st.session_state.logado = True
                st.session_state.nome_usuario = email_login.split('@')[0].capitalize()
                st.success("Acesso autorizado!") 
                st.rerun()
            else:
                st.error("Preencha o e-mail e a senha, irmão!")
            
    st.markdown("</div>", unsafe_allow_html=True)

# --- CONTROLADOR CENTRAL INTERNO / EXTERNO ---
if st.session_state.logado:
    try:
        from pages import Dashboard
        Dashboard.exibir()
    except Exception as e:
        st.error(f"Erro ao carregar painel interno: {e}")
else:
    exibir_painel_inicial()
