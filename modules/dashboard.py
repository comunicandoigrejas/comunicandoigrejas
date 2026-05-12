# modules/dashboard.py
import streamlit as st

def exibir():
    nome_usuario = st.session_state.get('nome_usuario', 'Membro')
    plano_usuario = st.session_state.get('plano', 'START').upper()

    # CSS
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
                box-shadow: 0 10px 25px rgba(255, 45, 149, 0.25);
            }
            .icon-box { font-size: 45px; margin-bottom: 10px; }
            .card-title { color: #ffffff; font-size: 1.3rem; font-weight: 700; margin-bottom: 5px; }
            .card-subtitle { color: #aaaaaa; font-size: 0.9rem; }
        </style>
    """, unsafe_allow_html=True)

    # Botão Voltar
    if st.button("← Voltar para a Página Inicial", use_container_width=False):
        st.session_state.logado = False
        st.rerun()

    # Cabeçalho
    st.markdown(f"""
        <div class="welcome-box">
            <h1 style='margin:0; color: #00FF00;'>Olá, {nome_usuario}! 👋</h1>
            <p style='color: #ddd; font-size: 1.15rem; margin-top: 8px;'>
                Plano Atual: <strong>{plano_usuario}</strong>
            </p>
        </div>
    """, unsafe_allow_html=True)

    st.subheader("📌 Escolha uma Categoria")

    # Linha 1
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown('<div class="category-card"><div class="icon-box">⛪</div><div class="card-title">Cultos Gerais</div><div class="card-subtitle">Domingo e Adoração</div></div>', unsafe_allow_html=True)
        st.button("Acessar", key="btn_geral", use_container_width=True)

    with c2:
        st.markdown('<div class="category-card"><div class="icon-box">🔥</div><div class="card-title">Jovens</div><div class="card-subtitle">Congressos e Vigílias</div></div>', unsafe_allow_html=True)
        st.button("Acessar", key="btn_jovens", use_container_width=True)

    with c3:
        st.markdown('<div class="category-card"><div class="icon-box">👨‍👩‍👧‍👦</div><div class="card-title">Família</div><div class="card-subtitle">Cultos Familiares</div></div>', unsafe_allow_html=True)
        st.button("Acessar", key="btn_familia", use_container_width=True)

    # Linha 2
    c4, c5, c6 = st.columns(3)
    with c4:
        st.markdown('<div class="category-card"><div class="icon-box">🌸</div><div class="card-title">Mulheres</div><div class="card-subtitle">Conferências Femininas</div></div>', unsafe_allow_html=True)
        st.button("Acessar", key="btn_mulheres", use_container_width=True)

    with c5:
        st.markdown('<div class="category-card"><div class="icon-box">🧔</div><div class="card-title">Homens</div><div class="card-subtitle">Varões de Valor</div></div>', unsafe_allow_html=True)
        st.button("Acessar", key="btn_homens", use_container_width=True)

    with c6:
        st.markdown('<div class="category-card"><div class="icon-box">🧸</div><div class="card-title">Infantil</div><div class="card-subtitle">Ministério Kids</div></div>', unsafe_allow_html=True)
        st.button("Acessar", key="btn_infantil", use_container_width=True)

    # Linha 3
    c7, c8, c9 = st.columns(3)
    with c7:
        st.markdown('<div class="category-card"><div class="icon-box">🍷</div><div class="card-title">Santa Ceia</div><div class="card-subtitle">Anúncios e Telão</div></div>', unsafe_allow_html=True)
        st.button("Acessar", key="btn_ceia", use_container_width=True)

    with c8:
        st.markdown('<div class="category-card"><div class="icon-box">🎉</div><div class="card-title">Datas Comemorativas</div><div class="card-subtitle">Natal, Páscoa, etc</div></div>', unsafe_allow_html=True)
        st.button("Acessar", key="btn_comemorativo", use_container_width=True)

    with c9:
        st.markdown('<div class="category-card"><div class="icon-box">💬</div><div class="card-title">Suporte</div><div class="card-subtitle">Fale conosco</div></div>', unsafe_allow_html=True)
        st.button("Acessar", key="btn_suporte", use_container_width=True)
