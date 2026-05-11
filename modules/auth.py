import streamlit as st
import pandas as pd

def validar_login(email_digitado, senha_digitada):
    # 1. COLOQUE O ID DA SUA PLANILHA AQUI
    # O ID é aquela parte entre o /d/ e o /edit no link da sua planilha
    # Exemplo: 1t_D_B9T2-mF2N6W5K_P9pE-Jp5I0n2-k-u1R0V-y-88
    ID_PLANILHA = "https://docs.google.com/spreadsheets/d/1dqf4LdW8U5fMAA2p0qPUgQnaAchvqM7Gt8o1--Rn1vg/edit" 
    
    # Este link força o Google a entregar os dados como um arquivo CSV puro
    url = f"https://docs.google.com/spreadsheets/d/{ID_PLANILHA}/export?format=csv"

    try:
        # Lê a planilha ignorando qualquer cache antigo
        df = pd.read_csv(url)
        
        # Limpa nomes de colunas e dados (tira espaços e converte para texto)
        df.columns = [c.strip() for c in df.columns]
        df = df.astype(str).apply(lambda x: x.str.strip())
        
        email_busca = str(email_digitado).strip().lower()
        senha_busca = str(senha_digitada).strip()

        # Procura o irmão na lista
        usuario = df[
            (df['Email'].str.lower() == email_busca) & 
            (df['Senha'] == senha_busca)
        ]
        
        if not usuario.empty:
            dados = usuario.iloc[0]
            if dados['Status'].upper() == 'ATIVO':
                return {
                    "sucesso": True, 
                    "nome": dados['Nome'],
                    "plano": dados['Plano'].upper()
                }
        return {"sucesso": False}

    except Exception as e:
        st.error(f"Erro de conexão: {e}")
        return {"sucesso": False}

def tela_login():
    st.markdown("<h2 style='text-align: center; color: #00FF00;'>Portal do Aluno</h2>", unsafe_allow_html=True)
    
    # Usamos o formulário para evitar que a página recarregue antes da hora
    with st.form("form_acesso"):
        email = st.text_input("E-mail cadastrado")
        senha = st.text_input("Sua senha", type="password")
        btn = st.form_submit_button("ENTRAR NA ÁREA DE MEMBROS", use_container_width=True)
        
        if btn:
            res = validar_login(email, senha)
            if res["sucesso"]:
                st.session_state.logado = True
                st.session_state.nome_usuario = res["nome"]
                st.session_state.plano = res["plano"]
                st.success(f"Bem-vindo, {res['nome']}!")
                st.rerun()
            else:
                st.error("Dados incorretos. Verifique o e-mail e senha na sua planilha.")
