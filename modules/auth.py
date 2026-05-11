import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd

def validar_login(email_digitado, senha_digitada):
    conn = st.connection("gsheets", type=GSheetsConnection)
    try:
        # O ttl=0 garante que ele leia os dados novos da planilha na hora, sem usar cache antigo
        df = conn.read(ttl=0) 
        
        # Limpa espaços em branco e garante que tudo seja tratado como texto (String)
        df['Email'] = df['Email'].astype(str).str.strip()
        df['Senha'] = df['Senha'].astype(str).str.strip()
        
        email_busca = str(email_digitado).strip()
        senha_busca = str(senha_digitada).strip()

        # Faz a busca exata
        usuario = df[(df['Email'] == email_busca) & (df['Senha'] == senha_busca)]
        
        if not usuario.empty:
            if usuario.iloc[0]['Status'] == 'Ativo':
                return {
                    "sucesso": True, 
                    "nome": usuario.iloc[0]['Nome'],
                    "plano": usuario.iloc[0]['Plano']
                }
            else:
                st.error("Varão, seu acesso está inativo.")
                return {"sucesso": False}
        else:
            # Se cair aqui, é porque e-mail ou senha não bateram com a planilha
            return {"sucesso": False}
    except Exception as e:
        st.error(f"Erro de conexão: {e}")
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
