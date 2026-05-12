import streamlit as st

st.set_page_config(page_title="Dashboard", layout="wide", page_icon="🏠")

with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

nome_usuario = st.session_state.get('nome_usuario', 'Membro')
plano_usuario = st.session_state.get('plano', 'START').upper()

st.title(f"🏠 Bem-vindo, {nome_usuario}!")

st.success(f"Plano Atual: **{plano_usuario}**")

st.subheader("Escolha uma categoria no menu lateral ↑")

if st.button("← Voltar para Vitrine"):
    st.session_state.logado = False
    st.rerun()
