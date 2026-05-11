import streamlit as st

def exibir():
    # 1. Recuperar dados da sessão (definidos no login)
    nome_usuario = st.session_state.get('nome_usuario', 'Varão')
    plano_usuario = st.session_state.get('plano', 'START').upper()

    # --- ESTILO CSS PERSONALIZADO ---
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
                height: 220px;
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
            .locked-card {
                border-color: #333 !important;
                opacity: 0.7;
            }
            .icon-box { font-size: 40px; margin-bottom: 10px; }
            .card-title { color: #ffffff; font-size: 1.2rem; font-weight: bold; }
            .card-subtitle { color: #888; font-size: 0.8rem; }
            .badge-premium {
                background-color: #7B2CBF;
                color: white;
                padding: 2px 8px;
                border-radius: 5px;
                font-size: 10px;
                margin-top: 5px;
            }
        </style>
    """, unsafe_allow_html=True)

    # --- TELA DE BOAS-VINDAS ---
    st.markdown(f"""
        <div class="welcome-box">
            <h1 style='margin:0; color: #00FF00;'>Olá, {nome_usuario}! 👋</h1>
            <p style='color: #ddd; font-size: 1.1rem; margin-top: 10px;'>
                Plano Atual: <span style='color: #7B2CBF; font-weight: bold;'>{plano_usuario}</span>
            </p>
        </div>
    """, unsafe_allow_html=True)

    st.subheader("📁 Categorias de Artes")
    
    # --- FUNÇÃO AUXILIAR PARA CRIAR CARDS COM TRAVA ---
    def criar_card(titulo, subtitulo, icone, chave, premium_only=False):
        is_locked = premium_only and plano_usuario == "START"
        
        card_class = "category-card locked-card" if is_locked else "category-card"
        badge = "<div class='badge-premium'>EXCLUSIVO PREMIUM</div>" if premium_only else ""
        icon = "🔒" if is_locked else icone

        st.markdown(f"""
            <div class="{card_class}">
                <div class="icon-box">{icon}</div>
                <div class="card-title">{titulo}</div>
                <div class="card-subtitle">{subtitulo}</div>
                {badge}
            </div>
        """, unsafe_allow_html=True)

        if is_locked:
            if st.button("🔓 Liberar Agora", key=chave, use_container_width=True):
                st.toast("Redirecionando para upgrade...", icon="🚀")
                # Aqui você coloca o link de upgrade da Hotmart futuramente
        else:
            st.button(f"Acessar {titulo}", key=chave, use_container_width=True)

    # --- GRID DE CATEGORIAS ---
    col1, col2, col3 = st.columns(3)

    with col1:
        criar_card("Cultos Gerais", "Domingo, Ensino, Oração", "⛪", "cultos")
    
    with col2:
        criar_card("Jovens & Teens", "Congressos e Vigílias", "🔥", "jovens")
    
    with col3:
        criar_card("Santa Ceia", "Anúncios e Telão", "🍞", "ceia")

    st.markdown("<br>", unsafe_allow_html=True)
    col4, col5, col6 = st.columns(3)

    with col4:
        criar_card("Logotipos", "Identidade Visual", "🎨", "logos")

    with col5:
        # Exemplo de conteúdo bloqueado para START
        criar_card("Vídeo Aulas", "Domine o Design", "🎥", "aulas", premium_only=True)

    with col6:
        # Exemplo de conteúdo bloqueado para START
        criar_card("Bônus VIP", "Texturas e Elementos 3D", "🎁", "bonus", premium_only=True)
