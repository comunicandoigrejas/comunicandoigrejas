import streamlit as st

st.set_page_config(page_title="Jovens", layout="wide", page_icon="🔥")

with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def exibir():
    st.markdown("<h1 class='gradient-title'>🔥 Jovens</h1>", unsafe_allow_html=True)
    st.markdown("<p class='sub-title'>Templates para Cultos Jovens, Congressos, Vigílias e Teens.</p>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("<div class='premium-card'>", unsafe_allow_html=True)
        st.image("assets/artes_jovens.png", caption="Culto Jovem", use_container_width=True)
        st.markdown("**Pack Jovens em Chamas**")
        st.write("25 Templates para Instagram")
        st.link_button("Editar Pack Jovens", "https://www.canva.com/...", use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.markdown("<div class='premium-card'>", unsafe_allow_html=True)
        st.markdown("**Pack Teens**")
        st.write("Disponível em breve!")
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("---")
    st.info("🔄 Novos packs são adicionados semanalmente!")

exibir()
