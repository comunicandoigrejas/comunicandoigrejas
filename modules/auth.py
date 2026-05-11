import streamlit as st
import pandas as pd

def validar_login(email_digitado, senha_digitada):
    # 1. COLOQUE O ID DA SUA PLANILHA AQUI
    # O ID é aquele código entre o /d/ e o /edit no link da sua planilha
    # Na sua imagem 37cab8.png, o ID aparece na barra de endereços.
    ID_PLANILHA = "https://docs.google.com/spreadsheets/d/1dqf4LdW8U5fMAA2p0qPUgQnaAchvqM7Gt8o1--Rn1vg/edit" 
    
    # Este link transforma a sua planilha num ficheiro de texto simples (CSV)
    url = f"https://docs.google.com/spreadsheets/d/{ID_PLANILHA}/export?format=csv&gid=0"

    try:
        # Lê a planilha ignorando o cache para garantir que lê o que acabou de escrever
        df = pd.read_csv(url)
        
        # Limpa os nomes das colunas (tira espaços invisíveis)
        df.columns = [c.strip() for c in df.columns]
        
        # Converte tudo para texto e limpa espaços nos dados
        df = df.astype(str).apply(lambda x: x.str.strip())
        
        email_busca = str(email_digitado).strip().lower()
        senha_busca = str(senha_digitada).strip()

        # Procura o usuário
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
        st.error(f"Erro na ligação: {e}")
        return {"sucesso": False}

def tela_login():
    st.markdown("<h2 style='text-align: center; color: #00FF00;'>Portal do Aluno</h2>", unsafe_allow_html=True)
    
    with st.form("form_acesso_direto"):
        email = st.text_input("E-mail")
        senha = st.text_input("Senha", type="password")
        submeter = st.form_submit_button("ENTRAR NA ÁREA DE MEMBROS", use_container_width=True)
        
        if submeter:
            res = validar_login(email, senha)
            if res["sucesso"]:
                st.session_state.logado = True
                st.session_state.nome_usuario = res["nome"]
                st.session_state.plano = res["plano"]
                st.success(f"Bem-vindo, {res['nome']}!")
                st.rerun()
            else:
                st.error("Dados incorretos. Verifique se o e-mail e a senha estão iguais à planilha.")
