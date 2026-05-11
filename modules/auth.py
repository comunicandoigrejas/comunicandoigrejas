# auth.py
import streamlit as st
import pandas as pd

def validar_login(email_digitado, senha_digitada):
    ID_PLANILHA = "1dqf4LdW8U5fMAA2p0qPUgQnaAchvqM7Gt8o1--Rn1vg"
    url = f"https://docs.google.com/spreadsheets/d/{ID_PLANILHA}/export?format=csv&gid=0"

    try:
        df = pd.read_csv(url, storage_options={'Cache-Control': 'no-cache'})
        df.columns = [c.strip() for c in df.columns]
        df = df.astype(str).apply(lambda x: x.str.strip())

        email_busca = str(email_digitado).strip().lower()
        senha_busca = str(senha_digitada).strip()

        usuario = df[
            (df['Email'].str.lower() == email_busca) & 
            (df['Senha'] == senha_busca)
        ]

        if not usuario.empty:
            dados = usuario.iloc[0]
            if dados.get('Status', '').upper() == 'ATIVO':
                return {
                    "sucesso": True,
                    "nome": dados.get('Nome', 'Membro'),
                    "plano": dados.get('Plano', 'START').upper()
                }
        return {"sucesso": False}

    except Exception as e:
        st.error(f"Erro ao conectar com a planilha: {e}")
        return {"sucesso": False}


def tela_login():
    st.markdown("<h2 style='text-align: center; color: #FF2D95;'>🔑 Acesso à Área de Membros</h2>", unsafe_allow_html=True)
    
    with st.form("form_login"):
        email = st.text_input("E-mail", placeholder="seuemail@exemplo.com")
        senha = st.text_input("Senha", type="password", placeholder="Sua senha")
        submit = st.form_submit_button("🔓 ENTRAR NA ÁREA DE MEMBROS", use_container_width=True)

        if submit:
            if not email or not senha:
                st.warning("Por favor, preencha e-mail e senha.")
                return

            res = validar_login(email, senha)
            if res["sucesso"]:
                st.session_state.logado = True
                st.session_state.nome_usuario = res["nome"]
                st.session_state.plano = res["plano"]
                st.success(f"Bem-vindo(a), {res['nome']}! 🎉")
                st.rerun()
            else:
                st.error("❌ E-mail ou senha incorretos.")
