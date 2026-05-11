# modules/tema_geral.py
import streamlit as st

def exibir():
    st.markdown("<h1 class='gradient-title'>⛪ Cultos Gerais</h1>", unsafe_allow_html=True)
    st.markdown("<p class='sub-title'>Templates editáveis para Cultos de Domingo, Adoração, Oração e Doutrina.</p>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("<div class='premium-card'>", unsafe_allow_html=True)
        st.image("assets/artes_domingo.png", caption="Culto de Celebração", use_container_width=True)
        st.markdown("**Pack #01 - Culto de Adoração**")
        st.write("20 Templates para Instagram (1:1)")
        st.link_button("Editar Pack no Canva", "https://www.canva.com/brand/join?token=...", use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.markdown("<div class='premium-card'>", unsafe_allow_html=True)
        # st.image("assets/outra_imagem.png", use_container_width=True)
        st.markdown("**Pack #02 - Culto de Libertação**")
        st.write("15 Templates para Instagram")
        st.write("Disponível em breve!")
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("---")
    st.info("🔄 Novos packs são adicionados semanalmente!")
