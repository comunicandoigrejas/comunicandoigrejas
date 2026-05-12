import streamlit as st

if not st.session_state.get("logado", False):
    st.warning("🔒 Acesso restrito. Faça login para continuar.")
    st.stop()

st.set_page_config(page_title="Datas Comemorativas", layout="wide", page_icon="🎉")

with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.sidebar.markdown(f"### 👋 Olá, **{st.session_state.get('nome_usuario', 'Membro')}**")
st.sidebar.markdown(f"**Plano:** {st.session_state.get('plano', 'START')}")
if st.sidebar.button("🏠 Voltar ao Dashboard"):
    st.switch_page("app.py")
if st.sidebar.button("🚪 Sair"):
    for key in list(st.session_state.keys()):
        del st.session_state[key]
    st.switch_page("app.py")

def exibir():
    st.markdown("<h1 class='gradient-title'>🎉 Datas Comemorativas</h1>", unsafe_allow_html=True)
    st.markdown("<p class='sub-title'>Templates para Natal, Páscoa, Ano Novo, Dia das Mães e Pais.</p>", unsafe_allow_html=True)
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
        st.markdown("**Pack Ano Novo**")
        st.write("Disponível em breve!")
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("---")
    st.info("🔄 Novos packs são adicionados semanalmente!")

exibir()
