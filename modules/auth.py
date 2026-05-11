import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd

def validar_login(email_digitado, senha_digitada):
    """
    Função que liga na planilha e verifica os dados do irmão.
    """
    # Estabelece a conexão com o Google Sheets configurado nos Secrets
    conn = st.connection("gsheets", type=GSheetsConnection)
    
    try:
        # Lê os dados da planilha
        df = conn.read()
        
        # Procura o usuário combinando E-mail e Senha
        usuario = df[(df['Email'] == email_digitado) & (df['Senha'] == str(senha_digitada))]
        
        if not usuario.empty:
            # Verifica se o irmão está com o status 'Ativo'
            if usuario.iloc[0]['Status'] == 'Ativo':
                return {
                    "sucesso": True, 
                    "nome": usuario.iloc[0]['Nome'],
                    "plano": usuario.iloc[0]['Plano'] # Pega o plano (START/PREMIUM) da planilha
                }
            else:
                st.error("Varão, seu acesso está inativo. Entre em contato com o suporte.")
                return {"sucesso": False}
        else:
            st.error("E-mail ou senha incorretos. Verifique os dados, abençoado.")
            return {"sucesso": False}
    except Exception as e:
        st.error("Erro ao conectar com a base de dados. Verifique sua internet.")
        return {"sucesso": False}

def tela_login():
    """
    Cria a interface visual do portal de acesso.
    """
    # Estilização com as cores que você pediu: Azul, Roxo e Verde
    st.markdown("""
        <style>
            .login-card {
                padding: 30px;
                background-color: #0e1117;
                border: 2px solid #7B2CBF;
                border-radius: 20px;
                box-shadow: 0 0 15px rgba(123, 44, 191, 0.3);
            }
        </style>
    """, unsafe_allow_html=True)

    # Centralizando o formulário na tela
    col_esq, col_centro, col_dir = st.columns([1, 2, 1])

    with col_centro:
        st.markdown("<div class='login-card'>", unsafe_allow_html=True)
        st.markdown("<h2 style='text-align: center; color: #00FF00;'>Portal do Aluno</h2>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; color: #ddd;'>Identifique-se para acessar suas artes</p>", unsafe_allow_html=True)
        
        email = st.text_input("Seu E-mail")
        senha = st.text_input("Sua Senha", type="password")
        
        if st.button("ENTRAR NO SISTEMA", use_container_width=True):
            resultado = validar_login(email, senha)
            
            if resultado.get("sucesso"):
                # AQUI ESTÁ A "ANOTAÇÃO" NA PASTA DIGITAL (SESSION STATE)
                st.session_state.logado = True
                st.session_state.nome_usuario = resultado["nome"]
                st.session_state.plano = resultado["plano"] # O Dashboard lerá esta linha!
                
                st.success(f"Seja bem-vindo, {resultado['nome']}!")
                st.rerun() # Reinicia o app já logado no Dashboard
        
        st.markdown("</div>", unsafe_allow_html=True)
        
        # Link para suporte caso o varão esqueça a senha
        st.markdown("<p style='text-align: center; font-size: 0.8rem; margin-top: 15px;'><a href='#' style='color: #888;'>Esqueceu sua senha? Fale com o suporte.</a></p>", unsafe_allow_html=True)
