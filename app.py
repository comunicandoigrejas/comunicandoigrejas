import streamlit as st
import os

# --- CONFIGURAÇÃO DA PÁGINA (TELA AMPLA E SEM SIDEBAR) ---
st.set_page_config(
    page_title="Comunicando Igrejas",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- GARANTE QUE AS VARIÁVEIS EXISTEM NO INÍCIO ---
if 'pagina_atual' not in st.session_state:
    st.session_state.pagina_atual = None

if 'logado' not in st.session_state:
    st.session_state.logado = False

if 'nome_usuario' not in st.session_state:
    st.session_state.nome_usuario = None

if 'plano' not in st.session_state:
    st.session_state.plano = None

# Import do sistema de login real
from modules.auth import tela_login

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

    # --- CSS PERSONALIZADO ---
    st.markdown("""
        <style>
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
        
        /* Botão luminoso topo */
        div.element-container:has(#btn_topo_container) + div div.stButton > button {
            background: linear-gradient(90deg, #FF2D95 0%, #00D2FF 100%) !important;
            color: #ffffff !important;
            font-weight: bold !important;
            font-size: 1.4rem !important;
            border: none !important;
            padding: 18px 30px !important;
            border-radius: 50px !important;
            box-shadow: 0 0 15px #FF2D95, 0 0 30px #00D2FF !important;
            animation: glowPulsar 1.8s infinite alternate !important;
            width: 100% !important;
        }
        
        @keyframes glowPulsar {
            0% { box-shadow: 0 0 10px #FF2D95, 0 0 20px #00D2FF; }
            100% { box-shadow: 0 0 25px #FF2D95, 0 0 50px #00D2FF; }
        }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # --- CHAMADA PRINCIPAL ---
    st.markdown("""
        <div style='text-align: center; margin-bottom: 10px;'>
            <p style='color: #a0a0a0; font-size: 1.3rem; margin-bottom: 0; text-decoration: line-through;'>De R$ 197 por Apenas</p>
            <h1 style='color: #ffffff; font-size: 4.8rem; font-weight: 900; margin-top: -5px; margin-bottom: 0px;'>R$ 29,90</h1>
            <p style='color: #00D2FF; font-size: 1.3rem; font-weight: bold; margin-top: 5px; margin-bottom: 30px;'>Comece hoje e nunca mais dependa de designers!</p>
        </div>
    """, unsafe_allow_html=True)
    
    col_esq, col_centro, col_dir = st.columns([1, 2, 1])
    with col_centro:
        st.markdown('<div id="btn_topo_container"></div>', unsafe_allow_html=True)
        if st.button("🚀 QUERO MEU ACESSO AGORA MESMO", key="btn_luminoso_topo", use_container_width=True):
            st.components.v1.html("""<script>window.parent.document.getElementById("tabela-precos").scrollIntoView({behavior: "smooth"});</script>""", height=0)

    st.markdown("<br><br><br>", unsafe_allow_html=True)

    # --- BENEFÍCIOS ---
    st.markdown("""
        <div class='caixa-beneficios'>
            <h2 style='text-align: center; color: #ffffff; font-weight: bold; margin-top: 0; margin-bottom: 30px;'>📋 E o que você terá acesso?</h2>
            <div class='item-beneficio'>
                <div class='titulo-beneficio'>⚡ Artes Profissionais:</div>
                <div class='desc-beneficio'>Centenas de artes prontas para editar no Canva.</div>
            </div>
            <div class='item-beneficio'>
                <div class='titulo-beneficio'>🔄 Atualizações Semanais:</div>
                <div class='desc-beneficio'>Novas artes toda semana.</div>
            </div>
            <div class='item-beneficio'>
                <div class='titulo-beneficio'>🎥 Vídeo Aulas Exclusivas:</div>
                <div class='desc-beneficio'>Aprenda a usar o Canva focado em igrejas.</div>
            </div>
            <div class='item-beneficio'>
                <div class='titulo-beneficio'>🎁 Bônus Exclusivos:</div>
                <div class='desc-beneficio'>Efeitos, textos 3D, imagens e muito mais.</div>
            </div>
            <div class='item-beneficio'>
                <div class='titulo-beneficio'>💬 Suporte Prioritário:</div>
                <div class='desc-beneficio'>Suporte direto via WhatsApp.</div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)

    # --- AMOSTRAS DE ARTES ---
    st.markdown("<h2 style='text-align: center; color: #00D2FF; font-weight: bold;'>🎨 Algumas das artes que te esperam</h2>", unsafe_allow_html=True)
    amostras_cols = st.columns(4)
    imagens_amostra = ["1.png", "2.png", "3.png", "4.png"]

    for idx, img_nome in enumerate(imagens_amostra):
        with amostras_cols[idx]:
            caminho_img = f"assets/{img_nome}"
            if os.path.exists(caminho_img):
                st.image(caminho_img, use_container_width=True)
            else:
                st.markdown(f"<div style='background-color: #111; padding: 80px 10px; text-align: center; border-radius: 8px; color: #444;'>🖼️ {img_nome}</div>", unsafe_allow_html=True)

    st.markdown("<br><br><br><br>", unsafe_allow_html=True)

    # --- TABELA DE PLANOS ---
    st.markdown('<div id="tabela-precos"></div>', unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center; color: #FF2D95; font-weight: bold;'>💎 Escolha o Plano Ideal para sua Igreja</h2>", unsafe_allow_html=True)

    vendas_col1, vendas_col2 = st.columns(2)

    with vendas_col1:
        st.markdown("""
            <div style='background-color: #0c0c0c; border: 1px solid #1f1f1f; border-radius: 15px; padding: 30px; text-align: center; min-height: 580px;'>
                <h3 class='titulo-plano' style='color: #00D2FF;'>🚀 Plano BÁSICO</h3>
                <p style='font-size: 1rem; color: #bbbbbb;'>Acesso anual às artes essenciais.</p>
                <hr style='border-color: #1f1f1f;'>
                <ul class='texto-grande-pacote' style='text-align: left; padding-left: 20px;'>
                    <li>⏳ Validade de <b>1 ano</b></li>
                    <li>✅ Cultos Gerais, Família, Homens, Mulheres, Infantil, Jovens, Santa Ceia, Campanhas</li>
                    <li>❌ Sem atualizações semanais</li>
                </ul>
                <hr style='border-color: #1f1f1f;'>
                <p style='color: #888888;'>Acesso por 1 ano por apenas</p>
                <h2 style='color: #ffffff; font-size: 2.5rem;'>R$ 29,90</h2>
            </div>
        """, unsafe_allow_html=True)
        st.link_button("🛍️ QUERO O PLANO BÁSICO", "https://pay.hotmart.com/Y106003109C", use_container_width=True)

    with vendas_col2:
        st.markdown("""
            <div style='background-color: #0c0c0c; border: 1px solid #FF2D95; border-radius: 15px; padding: 30px; text-align: center; min-height: 580px; box-shadow: 0 0 15px rgba(255, 45, 149, 0.15);'>
                <h3 class='titulo-plano' style='color: #FF2D95;'>👑 Plano PREMIUM</h3>
                <p style='font-size: 1rem; color: #bbbbbb;'>Acesso vitalício + atualizações.</p>
                <hr style='border-color: #1f1f1f;'>
                <ul class='texto-grande-pacote' style='text-align: left; padding-left: 20px;'>
                    <li>🔥 <b>Acesso VITALÍCIO</b></li>
                    <li>🔄 Atualizações Mensais</li>
                    <li>✅ Todos os templates + materiais secretaria</li>
                </ul>
                <hr style='border-color: #1f1f1f;'>
                <p style='color: #888888;'>Acesso Vitalício por apenas</p>
                <h2 style='color: #FF2D95; font-size: 2.5rem;'>R$ 59,90</h2>
            </div>
        """, unsafe_allow_html=True)
        st.link_button("👑 QUERO O PACOTE COMPLETO", "https://pay.hotmart.com/Y98906000N?off=7dey0pfj", use_container_width=True)

    st.markdown("<br><br><br>", unsafe_allow_html=True)

    # --- ÁREA DE LOGIN ---
    st.markdown("<div style='background-color: #0c0c0c; border: 1px solid #1f1f1f; border-radius: 15px; padding: 25px; margin-top: 20px;'>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; color: #ffffff; margin-top:0;'>🔑 Já comprou? Faça login para acessar seus templates</h3>", unsafe_allow_html=True)
    
    tela_login()   # ← Sistema real com planilha Google
    
    st.markdown("</div>", unsafe_allow_html=True)


# --- CONTROLADOR PRINCIPAL ---
if st.session_state.logado:
    try:
        from pages import Dashboard
        Dashboard.exibir()
    except Exception as e:
        st.error(f"Erro ao carregar o painel interno: {e}")
        st.info("💡 Verifique se a pasta **pages/templates_canva** existe **sem espaço** no final do nome.")
else:
    exibir_painel_inicial()