import streamlit as st
from modules import inicio, dashboard, artes, cursos # Importe seus módulos aqui

# ... (Seu código de configuração de página e CSS aqui) ...

# 1. Verificação do estado de login
if 'auth' not in st.session_state:
    st.session_state.auth = False

# 2. Roteador Principal
if not st.session_state.auth:
    # --- TELA PARA QUEM NÃO ESTÁ LOGADO ---
    inicio.exibir() # Chama a página inspirada nas fotos que você enviou
    
    st.sidebar.markdown("---")
    with st.sidebar.expander("Área do Assinante"):
        email = st.text_input("E-mail")
        senha = st.text_input("Senha", type="password")
        if st.button("Entrar na Benção"):
            if email == "admin" and senha == "123": # Simulação de login
                st.session_state.auth = True
                st.rerun()
            else:
                st.error("Credenciais incorretas, varão.")

else:
    # --- ÁREA INTERNA (PÓS-LOGIN) ---
    # O 'else' deve estar exatamente na mesma coluna do 'if not st.session_state.auth'
    with st.sidebar:
        st.image("assets/image_fcbdfe.png") # Exemplo de uso da sua imagem na barra lateral
        opcao = st.sidebar.radio(
            "Menu Principal", 
            ["Dashboard", "Artes Canva", "Cursos", "Ebooks", "Suporte"]
        )
        if st.button("Sair"):
            st.session_state.auth = False
            st.rerun()

    # Chamada das páginas internas
    if opcao == "Dashboard":
        dashboard.exibir()
    elif opcao == "Artes Canva":
        artes.exibir()
    elif opcao == "Cursos":
        cursos.exibir()
    # Adicione os outros elif conforme criar os módulos
