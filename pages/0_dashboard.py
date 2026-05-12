import streamlit as st

st.set_page_config(page_title="Dashboard", layout="wide", page_icon="🏠")

with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

nome = st.session_state.get('nome_usuario', 'Membro')
plano = st.session_state.get('plano', 'START')

st.title(f"🏠 Dashboard - Olá, {nome}!")
st.success(f"Plano Atual: **{plano}**")

st.info("👈 Use o menu lateral para acessar os temas")
