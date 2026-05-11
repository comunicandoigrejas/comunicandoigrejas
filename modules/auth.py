import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd

def validar_login(email_digitado, senha_digitada):
    # Link direto da sua planilha (substitua pelo seu ID real se necessário)
    # Esse formato abaixo é o mais estável para leitura direta
    sheet_id = "COLOQUE_AQUI_O_ID_DA_SUA_PLANILHA"
    url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet=Sheet1"
    
    try:
        # Lendo diretamente como CSV (muito mais rápido e sem erros de conexão gsheets)
        df = pd.read_csv(url)
        
        # Limpeza total de dados para comparação
        df = df.astype(str).apply(lambda x: x.str.strip())
        
        email_busca = str(email_digitado).strip().lower()
        senha_busca = str(senha_digitada).strip()

        # Busca o usuário
        usuario = df[
            (df['Email'].str.lower() == email_busca) & 
            (df['Senha'] == senha_busca)
        ]
        
        if not usuario.empty:
            dados = usuario.iloc[0]
            if dados['Status'] == 'Ativo':
                return {
                    "sucesso": True, 
                    "nome": dados['Nome'],
                    "plano": dados['Plano'].upper()
                }
        return {"sucesso": False}
    except Exception as e:
        st.error(f"Erro ao acessar dados: {e}")
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
