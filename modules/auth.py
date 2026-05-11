import streamlit as st
import pandas as pd

def validar_login(email_digitado, senha_digitada):
    # 1. O SEU LINK DE EXPORTAÇÃO (IMPORTANTE)
    # Pegue o ID da sua planilha (aquela sequência de letras e números no link)
    # Substitua o ID abaixo pelo ID da sua planilha Artes Canva
    sheet_id = "1t_D_B9T2-mF2N6W5K_P9pE-Jp5I0n2-k-u1R0V-y-88" # EXEMPLO: Coloque o seu ID aqui
    url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv&gid=0"

    try:
        # Tenta ler o arquivo CSV diretamente da web
        df = pd.read_csv(url)
        
        # Garante que as colunas existem antes de procurar
        colunas = [c.strip() for c in df.columns]
        df.columns = colunas

        # Limpa espaços e converte para texto
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
            if dados['Status'].lower() == 'ativo':
                return {
                    "sucesso": True, 
                    "nome": dados['Nome'],
                    "plano": dados['Plano'].upper()
                }
        return {"sucesso": False}

    except Exception as e:
        # Se der erro aqui, o problema é o link ou a conexão
        st.error(f"Erro ao acessar os dados da planilha: {e}")
        return {"sucesso": False}

def tela_login():
    st.markdown("<h2 style='text-align: center; color: #00FF00;'>Portal do Aluno</h2>", unsafe_allow_html=True)
    
    with st.form("login_form"):
        email = st.text_input("E-mail")
        senha = st.text_input("Senha", type="password")
        enviar = st.form_submit_button("ENTRAR NA ÁREA DE MEMBROS", use_container_width=True)
        
        if enviar:
            resultado = validar_login(email, senha)
            if resultado["sucesso"]:
                st.session_state.logado = True
                st.session_state.nome_usuario = resultado["nome"]
                st.session_state.plano = resultado["plano"]
                st.success("Acesso liberado!")
                st.rerun()
            else:
                st.error("Dados incorretos. Verifique o e-mail e a senha na planilha.")
