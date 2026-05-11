# modules/tema_infantil.py
import streamlit as st

def exibir():
    st.markdown("<h1 class='gradient-title'>🧸 Infantil</h1>", unsafe_allow_html=True)
    st.markdown("<p class='sub-title'>Templates para Escola Bíblica Infantil, Cultos Kids e Ministério Infantil.</p>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("<div class='premium-card'>", unsafe_allow_html=True)
        st.image("assets/artes_infantil.png", caption="Culto Infantil", use_container_width=True)
        st.markdown("**Pack Ministério Infantil**")
        st.write("25 Templates Coloridos")
        st.link_button("Editar Pack Infantil", "https://www.canva.com/...", use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.markdown("<div class='premium-card'>", unsafe_allow_html=True)
        st.markdown("**Pack #02 - EBD Kids**")
        st.write("Disponível em breve!")
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("---")
    st.info("🔄 Novos packs são adicionados semanalmente!")
