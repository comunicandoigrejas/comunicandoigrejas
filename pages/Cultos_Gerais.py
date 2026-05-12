import streamlit as st

def exibir():
    # Estilo específico para os cards de arte
    st.markdown("""
        <style>
            .premium-card {
                background-color: #0c0c0c;
                border: 1px solid #1f1f1f;
                border-radius: 15px;
                padding: 20px;
                margin-bottom: 20px;
                text-align: center;
            }
            .premium-card:hover {
                border-color: #FF2D95;
                box-shadow: 0 0 15px rgba(255, 45, 149, 0.3);
            }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("<h1 class='gradient-title'>⛪ Cultos Gerais</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>Templates editáveis para Cultos de Domingo, Adoração e Doutrina.</p>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    # Grid de Artes
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("<div class='premium-card'>", unsafe_allow_html=True)
        # Certifique-se de que a imagem existe na pasta assets
        st.image("1.jpg", caption="Pack Culto de Domingo", use_container_width=True)
        st.markdown("### Pack #01 - Celebração")
        st.write("20 Templates 1:1 (Instagram)")
        st.link_button("🎨 Editar no Canva", "https://www.canva.com/...", use_container_width=True, key="btn_culto_1")
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.markdown("<div class='premium-card'>", unsafe_allow_html=True)
        st.image("2.jpg", caption="Pack Adoração", use_container_width=True)
        st.markdown("### Pack #02 - Adoração")
        st.write("15 Templates para Stories/Feed")
        st.link_button("🎨 Editar no Canva", "https://www.canva.com/...", use_container_width=True, key="btn_culto_2")
        st.markdown("</div>", unsafe_allow_html=True)

    # Botão para "fechar" a categoria e voltar a ver apenas os botões do Dashboard
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("⬅️ Voltar aos Temas", use_container_width=True, key="voltar_cultos"):
        st.session_state.pagina_atual = None
        st.rerun()
