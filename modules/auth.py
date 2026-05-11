import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd

# modules/auth.py - Trecho atualizado da função validar_login

def validar_login(email_digitado, senha_digitada):
    conn = st.connection("gsheets", type=GSheetsConnection)
    try:
        df = conn.read()
        usuario = df[(df['Email'] == email_digitado) & (df['Senha'] == str(senha_digitada))]
        
        if not usuario.empty:
            if usuario.iloc[0]['Status'] == 'Ativo':
                # Guardamos o Nome e o Plano na sessão
                return {
                    "sucesso": True, 
                    "nome": usuario.iloc[0]['Nome'],
                    "plano": usuario.iloc[0]['Plano'] # Pega o plano da planilha
                }
            else:
                st.error("Varão, seu acesso está inativo.")
                return {"sucesso": False}
        else:
            st.error("E-mail ou senha incorretos.")
            return {"sucesso": False}
    except:
        return {"sucesso": False}

# Na tela_login, quando o botão for clicado:
# resultado = validar_login(email, senha)
# if resultado["sucesso"]:
#     st.session_state.logado = True
#     st.session_state.nome_usuario = resultado["nome"]
#     st.session_state.plano = resultado["plano"] # Aqui a mágica acontece

def tela_login():
    # Estilização com as cores: Azul, Roxo e Verde
    st.markdown("""
        <style>
            .login-container {
                padding: 40px;
                background-color: #0e1117;
                border: 2px solid #7B2CBF;
                border-radius: 20px;
                box-shadow: 0 0 20px rgba(123, 44, 191, 0.3);
            }
        </style>
    """, unsafe_allow_html=True)

    with st.container():
        st.markdown("<h2 style='text-align: center; color: #00FF00;'>Portal do Aluno</h2>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center;'>Identifique-se para acessar suas artes</p>", unsafe_allow_html=True)
        
        email = st.text_input("E-mail cadastrado")
        senha = st.text_input("Sua senha secreta", type="password")
        
        if st.button("ENTRAR NO SISTEMA", use_container_width=True):
            sucesso, nome = validar_login(email, senha)
            if sucesso:
                st.session_state.logado = True
                st.session_state.nome_usuario = nome
                st.success(f"Bem-vindo, {nome}! Acesso liberado.")
                st.rerun() # Atualiza para entrar no Dashboard
