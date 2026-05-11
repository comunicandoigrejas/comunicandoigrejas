# modules/tema_homens.py
import streamlit as st

def exibir():
    st.markdown("<h1 class='gradient-title'>🧔 Homens</h1>", unsafe_allow_html=True)
    st.markdown("<p class='sub-title'>Templates para Cultos de Homens, Café com Varões e Conferências Masculinas.</p>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("<div class='premium-card'>", unsafe_allow_html=True)
        st.image("assets/artes_homens.png", caption="Culto de Homens", use_container_width=True)
        st.markdown("**Pack Varões de Valor**")
        st.write("20 Templates para Instagram")
        st.link_button("Editar Pack Homens", "https://www.canva.com/...", use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.markdown("<div class='premium-card'>", unsafe_allow_html=True)
        st.markdown("**Pack #02 - Homens de Oração**")
        st.write("Disponível em breve!")
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("---")
    st.info("🔄 Novos packs são adicionados semanalmente!")
