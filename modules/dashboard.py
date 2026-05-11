# modules/dashboard.py
import streamlit as st

def exibir():
    nome_usuario = st.session_state.get('nome_usuario', 'Membro')
    plano_usuario = st.session_state.get('plano', 'START').upper()

    # CSS Personalizado do Dashboard
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
                border: 1px solid rgba(255, 255, 255, 0.1);
                padding: 25px;
                border-radius: 16px;
                text-align: center;
                transition: all 0.3s;
                height: 240px;
                display: flex;
                flex-direction: column;
                justify-content: center;
            }
            .category-card:hover {
                border-color: #FF2D95;
                transform: translateY(-8px);
                box-shadow: 0 10px 20px rgba(255, 45, 149, 0.2);
            }
            .icon-box { font-size: 48px; margin-bottom: 12px; }
            .card-title { color: #ffffff; font-size: 1.35rem; font-weight: 700; }
            .card-subtitle { color: #aaaaaa; font-size: 0.95rem; }
            .badge {
                background: linear-gradient(90deg, #FF2D95, #7B2CBF);
                color: white;
                padding: 4px 12px;
                border-radius: 20px;
                font-size: 0.8rem;
                margin-top: 8px;
                display: inline-block;
            }
        </style>
    """, unsafe_allow_html=True)

    # Boas-vindas
    st.markdown(f"""
        <div class="welcome-box">
            <h1 style='margin:0; color: #00FF00;'>Olá, {nome_usuario}! 👋</h1>
            <p style='color: #ddd; font-size: 1.2rem; margin-top: 8px;'>
                Plano Atual: <strong>{plano_usuario}</strong>
            </p>
        </div>
    """, unsafe_allow_html=True)

    st.subheader("📌 Categorias Disponíveis")

    # Grid de Cards
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
            <div class="category-card">
                <div class="icon-box">⛪</div>
                <div class="card-title">Cultos Gerais</div>
                <div class="card-subtitle">Domingo, Adoração e Ensino</div>
            </div>
        """, unsafe_allow_html=True)
        if st.button("Acessar Cultos Gerais", key="btn_geral", use_container_width=True):
            st.switch_page("app.py")  # ou vamos usar outra estratégia

    with col2:
        st.markdown("""
            <div class="category-card">
                <div class="icon-box">🔥</div>
                <div class="card-title">Jovens</div>
                <div class="card-subtitle">Congressos e Vigílias</div>
            </div>
        """, unsafe_allow_html=True)
        st.button("Acessar Jovens", key="btn_jovens", use_container_width=True)

    with col3:
        st.markdown("""
            <div class="category-card">
                <div class="icon-box">🍷</div>
                <div class="card-title">Santa Ceia</div>
                <div class="card-subtitle">Anúncios e Telão</div>
            </div>
        """, unsafe_allow_html=True)
        st.button("Acessar Santa Ceia", key="btn_ceia", use_container_width=True)

    st.markdown("<br>", unsafe_allow_html=True)
    col4, col5, col6 = st.columns(3)

    with col4:
        st.markdown("""
            <div class="category-card">
                <div class="icon-box">👨‍👩‍👧‍👦</div>
                <div class="card-title">Família</div>
                <div class="card-subtitle">Cultos Familiares</div>
            </div>
        """, unsafe_allow_html=True)
        st.button("Acessar Família", key="btn_familia", use_container_width=True)

    with col5:
        st.markdown("""
            <div class="category-card">
                <div class="icon-box">🌸</div>
                <div class="card-title">Mulheres</div>
                <div class="card-subtitle">Conferências Femininas</div>
            </div>
        """, unsafe_allow_html=True)
        st.button("Acessar Mulheres", key="btn_mulheres", use_container_width=True)

    with col6:
        st.markdown("""
            <div class="category-card">
                <div class="icon-box">🧸</div>
                <div class="card-title">Infantil</div>
                <div class="card-subtitle">Ministério Kids</div>
            </div>
        """, unsafe_allow_html=True)
        st.button("Acessar Infantil", key="btn_infantil", use_container_width=True)
