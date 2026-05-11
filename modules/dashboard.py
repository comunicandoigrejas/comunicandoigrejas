import streamlit as st

def exibir():
    # --- ESTILO CSS PERSONALIZADO (Cores: Azul, Roxo, Verde) ---
    st.markdown("""
        <style>
            .welcome-box {
                background: linear-gradient(135deg, #1A1A2E 0%, #16213E 100%);
                padding: 30px;
                border-radius: 20px;
                border-left: 8px solid #7B2CBF;
                margin-bottom: 30px;
            }
            .category-card {
                background: rgba(255, 255, 255, 0.05);
                border: 1px solid rgba(255, 255, 255, 0.1);
                padding: 20px;
                border-radius: 15px;
                text-align: center;
                transition: 0.3s;
                height: 200px;
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
            }
            .category-card:hover {
                border-color: #00FF00;
                transform: translateY(-5px);
                background: rgba(0, 255, 0, 0.02);
            }
            .icon-box {
                font-size: 40px;
                margin-bottom: 10px;
            }
            .card-title {
                color: #ffffff;
                font-size: 1.2rem;
                font-weight: bold;
            }
            .card-subtitle {
                color: #888;
                font-size: 0.8rem;
            }
        </style>
    """, unsafe_allow_html=True)

    # --- TELA DE BOAS-VINDAS ---
    st.markdown(f"""
        <div class="welcome-box">
            <h1 style='margin:0; color: #00FF00;'>Olá, Varão! 👋</h1>
            <p style='color: #ddd; font-size: 1.2rem;'>Bem-vindo à área exclusiva do <b>Comunicando Igrejas</b>. 
            Suas ferramentas para um ministério relevante estão aqui!</p>
        </div>
    """, unsafe_allow_html=True)

    st.subheader("📁 Categorias de Artes")
    st.write("Escolha uma categoria para acessar os templates no Canva:")

    # --- GRID DE CATEGORIAS (Primeiras Categorias) ---
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
            <div class="category-card">
                <div class="icon-box">⛪</div>
                <div class="card-title">Cultos Gerais</div>
                <div class="card-subtitle">Domingo, Ensino, Oração</div>
            </div>
        """, unsafe_allow_html=True)
        if st.button("Acessar Cultos", key="cultos", use_container_width=True):
            st.session_state.pagina_interna = "cultos" # Para navegação futura

    with col2:
        st.markdown("""
            <div class="category-card" style="border-left: 4px solid #7B2CBF;">
                <div class="icon-box">🔥</div>
                <div class="card-title">Jovens & Teens</div>
                <div class="card-subtitle">Congressos, Vigílias, Lives</div>
            </div>
        """, unsafe_allow_html=True)
        st.button("Acessar Jovens", key="jovens", use_container_width=True)

    with col3:
        st.markdown("""
            <div class="category-card" style="border-left: 4px solid #48CAE4;">
                <div class="icon-box">🍞</div>
                <div class="card-title">Santa Ceia</div>
                <div class="card-subtitle">Anúncios e Fundo de Telão</div>
            </div>
        """, unsafe_allow_html=True)
        st.button("Acessar Santa Ceia", key="ceia", use_container_width=True)

    st.markdown("<br>", unsafe_allow_html=True)

    col4, col5, col6 = st.columns(3)

    with col4:
        st.markdown("""
            <div class="category-card">
                <div class="icon-box">🎨</div>
                <div class="card-title">Logotipos</div>
                <div class="card-subtitle">Identidade para Ministérios</div>
            </div>
        """, unsafe_allow_html=True)
        st.button("Acessar Logos", key="logos", use_container_width=True)

    with col5:
        st.markdown("""
            <div class="category-card">
                <div class="icon-box">📱</div>
                <div class="card-title">Cartão Digital</div>
                <div class="card-subtitle">Links para Bio e Contatos</div>
            </div>
        """, unsafe_allow_html=True)
        st.button("Acessar Cartões", key="cartoes", use_container_width=True)

    with col6:
        st.markdown("""
            <div class="category-card">
                <div class="icon-box">🎁</div>
                <div class="card-title">Bônus VIP</div>
                <div class="card-subtitle">Texturas, 3D e Elementos</div>
            </div>
        """, unsafe_allow_html=True)
        st.button("Acessar Bônus", key="bonus", use_container_width=True)
