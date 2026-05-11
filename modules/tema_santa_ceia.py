# modules/tema_santa_ceia.py
import streamlit as st

def exibir():
    st.markdown("<h1 class='gradient-title'>🍷 Santa Ceia</h1>", unsafe_allow_html=True)
    st.markdown("<p class='sub-title'>Templates para Santa Ceia, Anúncios e Telão.</p>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("<div class='premium-card'>", unsafe_allow_html=True)
        st.image("assets/artes_santa_ceia.png", caption="Santa Ceia", use_container_width=True)
        st.markdown("**Pack Santa Ceia**")
        st.write("18 Templates Especiais")
        st.link_button("Editar Pack Santa Ceia", "https://www.canva.com/...", use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.markdown("<div class='premium-card'>", unsafe_allow_html=True)
        st.markdown("**Pack #02 - Ceia do Senhor**")
        st.write("Disponível em breve!")
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("---")
    st.info("🔄 Novos packs são adicionados semanalmente!")
