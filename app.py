import streamlit as st
from modules import dashboard, artes, cursos, ebooks, suporte

# Configuração Base
st.set_page_config(page_title="Comunicando Igrejas", layout="wide")

# Carrega o CSS Neon
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Gerenciamento de Login (Simples para exemplo)
if 'auth' not in st.session_state:
    st.session_state.auth = False

def tela_login():
    st.markdown("<h1 class='gradient-text' style='text-align: center;'>Portal Comunicando Igrejas</h1>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1,1,1])
    with col2:
        email = st.text_input("E-mail")
        senha = st.text_input("Senha", type="password")
        if st.button("Entrar na Benção", use_container_width=True):
            if email == "admin" and senha == "123": # Aqui você conectará com seu banco futuramente
                st.session_state.auth = True
                st.rerun()
            else:
                st.error("Credenciais incorretas.")

# --- ROTEADOR DE PÁGINAS ---
if not st.session_state.auth:
   if not st.session_state.auth:
    # Se NÃO estiver logado, mostra a Página Inicial (Landing Page)
    inicio.exibir() 
    
    # Opcional: Coloque o formulário de login no final ou em um botão flutuante
    with st.expander("Já é membro? Faça login aqui"):
        # Seus campos de email e senha...
        if st.button("Entrar na Benção"):
            # Lógica de login
            st.session_state.auth = True
            st.rerun()
else:
    # Se ESTIVER logado, mostra o Menu Lateral e as outras páginas
    opcao = st.sidebar.radio("Navegação", ["Dashboard", "Artes Canva", "Cursos"])
    
    if opcao == "Dashboard":
        dashboard.exibir()
    elif opcao == "Artes Canva":
        artes.exibir()
else:
    # Menu Lateral Premium
    with st.sidebar:
        st.image("https://via.placeholder.com/150") # Sua Logo
        st.markdown("---")
        escolha = st.radio(
            "Navegação", 
            ["Início", "Artes Canva", "Cursos", "Ebooks", "Suporte"]
        )
        if st.button("Sair"):
            st.session_state.auth = False
            st.rerun()

    # Chama a página específica
    if escolha == "Início":
        dashboard.exibir()
    elif escolha == "Artes Canva":
        artes.exibir()
    elif escolha == "Cursos":
        cursos.exibir()
    elif escolha == "Ebooks":
        ebooks.exibir()
    elif escolha == "Suporte":
        suporte.exibir()
