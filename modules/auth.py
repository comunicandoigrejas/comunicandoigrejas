import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd

def validar_login(email_digitado, senha_digitada):
    """Verifica os dados na planilha e retorna Nome e Plano."""
    conn = st.connection("gsheets", type=GSheetsConnection)
    try:
        df = conn.read()
        # Procura o usuário
        usuario = df[(df['Email'] == email_digitado) & (df['Senha'] == str(senha_digitada))]
        
        if not usuario.empty:
            if usuario.iloc[0]['Status'] == 'Ativo':
                return {
                    "sucesso": True, 
                    "nome": usuario.iloc[0]['Nome'],
                    "plano": usuario.iloc[0]['Plano'].upper() # Guarda START ou PREMIUM
                }
            else:
                st.error("Varão, seu acesso está inativo. Contacte o suporte.")
                return {"sucesso": False}
        else:
            return {"sucesso": False}
    except:
        st.error("Erro ao ligar à base de dados.")
        return {"sucesso": False}

def tela_login():
    """Interface visual do Portal do Aluno."""
    
    # Centralizando para não ocupar a largura toda (como na sua imagem 41d67f)
    col_esq, col_centro, col_dir = st.columns([1, 2, 1])

    with col_centro:
        st.markdown("<h2 style='text-align: center; color: #00FF00;'>Já possui acesso?</h2>", unsafe_allow_html=True)
        st.write("Entre com os seus dados abaixo para aceder aos templates.")

        # Criando o formulário de login
        with st.form("form_login"):
            email = st.text_input("E-mail")
            senha = st.text_input("Senha", type="password")
            botao = st.form_submit_button("🔓 ENTRAR NA ÁREA DE MEMBROS", use_container_width=True)
            
            if botao:
                resultado = validar_login(email, senha)
                
                if resultado and resultado.get("sucesso"):
                    # AQUI GUARDAMOS NA SESSÃO
                    st.session_state.logado = True
                    st.session_state.nome_usuario = resultado["nome"]
                    st.session_state.plano = resultado["plano"] # Importante para o Dashboard
                    
                    st.success(f"Bem-vindo, {resultado['nome']}!")
                    st.rerun()
                else:
                    st.error("Dados incorretos. Caso ainda não tenha o pack, clique no botão verde acima para comprar!")
