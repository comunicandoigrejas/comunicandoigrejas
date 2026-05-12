# modules/tema_comemorativo.py
import streamlit as st

def exibir():
    st.markdown("<h1 class='gradient-title'>🎉 Datas Comemorativas</h1>", unsafe_allow_html=True)
    st.markdown("<p class='sub-title'>Templates para Natal, Páscoa, Ano Novo, Dia das Mães, Pais e Feriados.</p>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("<div class='premium-card'>", unsafe_allow_html=True)
        st.image("assets/artes_natal.png", caption="Natal", use_container_width=True)
        st.markdown("**Pack Natal e Páscoa**")
        st.write("30 Templates Especiais")
        st.link_button("Editar Pack Comemorativos", "https://www.canva.com/...", use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.markdown("<div class='premium-card'>", unsafe_allow_html=True)
        st.markdown("**Pack #02 - Ano Novo**")
        st.write("Disponível em breve!")
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("---")
    st.info("🔄 Novos packs são adicionados semanalmente!")
