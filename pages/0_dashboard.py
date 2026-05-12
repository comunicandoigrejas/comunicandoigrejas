import streamlit as st

st.set_page_config(page_title="Dashboard", layout="wide", page_icon="🏠")

with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

nome = st.session_state.get('nome_usuario', 'Irmão')
plano = st.session_state.get('plano', 'START')

st.title(f"🏠 Dashboard")
st.success(f"Olá, {nome} | Plano: **{plano}**")

st.markdown("### Use o menu lateral para acessar os temas:")
st.info("👈 Cultos Gerais, Jovens, Família, etc.")

if st.button("← Voltar para Vitrine"):
    st.session_state.logado = False
    st.rerun()
