import streamlit as st

# Configuração da página
st.set_page_config(page_title="Comunicando Igrejas", layout="wide", page_icon="📱")

# Carregar CSS Personalizado
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# --- SISTEMA DE ESTADO ---
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# --- FUNÇÕES DE NAVEGAÇÃO ---
def login():
    st.session_state.logged_in = True

def logout():
    st.session_state.logged_in = False

# --- 1. PÁGINA INICIAL (PRÉ-LOGIN) ---
if not st.session_state.logged_in:
    # Seção Hero
    st.markdown("<h1 style='text-align: center;' class='gradient-text'>Tenha acesso a uma plataforma completa para transformar a comunicação da sua igreja</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;'>Artes prontas, cursos, materiais e ferramentas — tudo em um só lugar</h3>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        if st.button("🔥 QUERO ACESSAR AGORA (Hotmart)", use_container_width=True):
            st.write("Redirecionando para Hotmart...") # Adicione o link real aqui
        
        st.divider()
        
        # Área de Login Simples
        st.subheader("Já é membro? Faça seu login")
        email = st.text_input("Email")
        password = st.text_input("Senha", type="password")
        if st.button("Entrar na Plataforma"):
            if email == "admin" and password == "123": # Lógica de teste
                login()
                st.rerun()
            else:
                st.error("Credenciais inválidas, irmão.")

# --- 2. ÁREA INTERNA (PÓS-LOGIN) ---
else:
    st.sidebar.image("https://via.placeholder.com/150", caption="Comunicando Igrejas") # Use sua logo
    menu = st.sidebar.radio("Navegação", ["Dashboard", "Artes Canva", "Cursos", "Ebooks", "Suporte"])
    
    if st.sidebar.button("Sair"):
        logout()
        st.rerun()

    if menu == "Dashboard":
        st.markdown(f"## Bem-vindo à plataforma <span class='gradient-text'>Comunicando Igrejas</span>", unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.info("🎨 **Artes Canva**\n\n+500 templates prontos.")
        with col2:
            st.success("🎓 **Cursos**\n\nTreinamentos para sua equipe.")
        with col3:
            st.warning("📚 **Ebooks**\n\nGuias práticos de gestão.")

    elif menu == "Artes Canva":
        st.header("🎨 Templates Editáveis")
        cat = st.tabs(["Cultos", "Eventos", "Jovens", "Mulheres"])
        
        with cat[0]:
            col1, col2 = st.columns(2)
            with col1:
                st.image("https://via.placeholder.com/400x400", caption="Pack Culto de Domingo")
                st.button("Editar no Canva", key="btn1")

    elif menu == "Cursos":
        st.header("🎓 Treinamentos Profissionais")
        st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ") # Exemplo de player
        st.markdown("### Módulo 1: IA para Igrejas")
        st.write("- Aula 1: Introdução ao Design com IA")
        st.write("- Aula 2: Criando roteiros abençoados")

    elif menu == "Suporte":
        st.header("💬 Suporte ao Aluno")
        st.write("Precisa de ajuda, varão?")
        st.button("Chamar no WhatsApp")
