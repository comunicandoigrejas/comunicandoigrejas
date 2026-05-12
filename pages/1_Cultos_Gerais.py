import streamlit as st

st.set_page_config(page_title="Cultos Gerais", layout="wide", page_icon="⛪")

# Carrega o CSS (importante para manter o estilo)
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def exibir():
    st.markdown("<h1 class='gradient-title'>⛪ Cultos Gerais</h1>", unsafe_allow_html=True)
    st.markdown("<p class='sub-title'>Templates editáveis para Cultos de Domingo, Adoração, Oração e Doutrina.</p>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("<div class='premium-card'>", unsafe_allow_html=True)
        st.image("assets/artes_domingo.png", caption="Culto de Celebração", use_container_width=True)
        st.markdown("**Pack #01 - Culto de Adoração**")
        st.write("20 Templates 1:1 (Instagram)")
        st.link_button("Editar no Canva", "https://www.canva.com/...", use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.markdown("<div class='premium-card'>", unsafe_allow_html=True)
        st.markdown("**Pack #02 - Próximo Pack**")
        st.write("15 Templates")
        st.write("Disponível em breve!")
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("---")
    st.info("🔄 Novos packs são adicionados semanalmente!")

exibir()
