import streamlit as st

st.set_page_config(page_title="Dashboard", layout="wide", page_icon="🏠")

with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def exibir():
    nome_usuario = st.session_state.get('nome_usuario', 'Membro')
    plano_usuario = st.session_state.get('plano', 'START').upper()

    st.markdown("""
        <style>
            .welcome-box {
                background: linear-gradient(135deg, #1A1A2E 0%, #16213E 100%);
                padding: 35px;
                border-radius: 20px;
                border-left: 8px solid #FF2D95;
                margin-bottom: 30px;
            }
            .category-card {
                background: rgba(255, 255, 255, 0.06);
                border: 1px solid rgba(255, 255, 255, 0.12);
                padding: 25px 15px;
                border-radius: 16px;
                text-align: center;
                transition: all 0.3s;
                height: 235px;
                display: flex;
                flex-direction: column;
                justify-content: center;
            }
            .category-card:hover {
                border-color: #FF2D95;
                transform: translateY(-6px);
            }
            .icon-box { font-size: 45px; margin-bottom: 10px; }
            .card-title { color: #ffffff; font-size: 1.3rem; font-weight: 700; }
            .card-subtitle { color: #aaaaaa; font-size: 0.9rem; }
        </style>
    """, unsafe_allow_html=True)

    # Botão Voltar
    if st.button("← Voltar para Vitrine", use_container_width=True):
        st.session_state.logado = False
        st.rerun()

    st.markdown(f"""
        <div class="welcome-box">
            <h1 style='margin:0; color: #00FF00;'>Olá, {nome_usuario}! 👋</h1>
            <p style='color: #ddd; font-size: 1.15rem;'>Plano: <strong>{plano_usuario}</strong></p>
        </div>
    """, unsafe_allow_html=True)

    st.subheader("📌 Escolha uma Categoria")

    # Cards (Streamlit vai mostrar automaticamente no menu lateral)
    cols = st.columns(3)

    with cols[0]:
        st.markdown('<div class="category-card"><div class="icon-box">⛪</div><div class="card-title">Cultos Gerais</div></div>', unsafe_allow_html=True)
    with cols[1]:
        st.markdown('<div class="category-card"><div class="icon-box">🔥</div><div class="card-title">Jovens</div></div>', unsafe_allow_html=True)
    with cols[2]:
        st.markdown('<div class="category-card"><div class="icon-box">👨‍👩‍👧‍👦</div><div class="card-title">Família</div></div>', unsafe_allow_html=True)

    cols2 = st.columns(3)
    with cols2[0]:
        st.markdown('<div class="category-card"><div class="icon-box">🌸</div><div class="card-title">Mulheres</div></div>', unsafe_allow_html=True)
    with cols2[1]:
        st.markdown('<div class="category-card"><div class="icon-box">🧔</div><div class="card-title">Homens</div></div>', unsafe_allow_html=True)
    with cols2[2]:
        st.markdown('<div class="category-card"><div class="icon-box">🧸</div><div class="card-title">Infantil</div></div>', unsafe_allow_html=True)

    cols3 = st.columns(3)
    with cols3[0]:
        st.markdown('<div class="category-card"><div class="icon-box">🍷</div><div class="card-title">Santa Ceia</div></div>', unsafe_allow_html=True)
    with cols3[1]:
        st.markdown('<div class="category-card"><div class="icon-box">🎉</div><div class="card-title">Datas Comemorativas</div></div>', unsafe_allow_html=True)
    with cols3[2]:
        st.markdown('<div class="category-card"><div class="icon-box">💬</div><div class="card-title">Suporte</div></div>', unsafe_allow_html=True)

exibir()
