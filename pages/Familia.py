import streamlit as st

st.set_page_config(page_title="Família", layout="wide", page_icon="👨‍👩‍👧‍👦")

with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def exibir():
    st.markdown("<h1 class='gradient-title'>👨‍👩‍👧‍👦 Família</h1>", unsafe_allow_html=True)
    st.markdown("<p class='sub-title'>Templates para Cultos da Família, Dia dos Pais, Dia das Mães e Relacionamentos.</p>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("<div class='premium-card'>", unsafe_allow_html=True)
        st.image("assets/artes_familia.png", caption="Culto da Família", use_container_width=True)
        st.markdown("**Pack Família**")
        st.write("20 Templates para Instagram")
        st.link_button("Editar Pack Família", "https://www.canva.com/...", use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.markdown("<div class='premium-card'>", unsafe_allow_html=True)
        st.markdown("**Pack #02 - Relacionamentos**")
        st.write("Disponível em breve!")
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("---")
    st.info("🔄 Novos packs são adicionados semanalmente!")

exibir()
