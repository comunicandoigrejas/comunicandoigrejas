# app.py
import streamlit as st

# Configuração da Página (Título na aba do navegador)
st.set_page_config(page_title="Comunicando Igrejas - Vitrine de Artes", layout="wide", page_icon="📱")

# Carregando o CSS Premium
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# 1. IMPORTANDO TODOS OS MÓDULOS (As páginas que você criou)
try:
    from modules import (
        vitrine, suporte, tema_geral, tema_familia, 
        tema_jovens, tema_mulheres, tema_homens, 
        tema_infantil, tema_santa_ceia, tema_comemorativo
    )
except ImportError as e:
    st.error(f"Erro ao importar módulos. Verifique se o arquivo __init__.py existe e se os nomes estão corretos. Erro: {e}")
    st.stop()

# 2. Gerenciamento do Estado de Login
if 'auth' not in st.session_state:
    st.session_state.auth = False

# 3. FLUXO PRINCIPAL DO APP
if not st.session_state.auth:
    # --- FLUXO PARA VISITANTES (Venda) ---
    vitrine.exibir() # Mostra a Landing Page de Vendas (inspirada nas fotos)
    
    # Seção de Login na Sidebar (para quem já comprou)
    st.sidebar.markdown("<br><br>", unsafe_allow_html=True)
    st.sidebar.markdown("---")
    with st.sidebar.expander("🔐 Já é Cliente? Faça Login"):
        email = st.text_input("E-mail")
        senha = st.text_input("Senha", type="password")
        if st.button("Acessar Área de Membros", use_container_width=True):
            # Lógica de Login (Substitua por integração real futuramente)
            if email == "admin@igreja.com" and senha == "123":
                st.session_state.auth = True
                st.rerun()
            else:
                st.error("Credenciais incorretas, varão.")

else:
    # --- FLUXO PARA CLIENTES (Pós-Venda) ---
    st.sidebar.markdown("### Menu do Membro")
    st.sidebar.success(f"Logado como: admin@igreja.com")
    
    # 4. O MENU LATERAL AGORA MOSTRA TODOS OS TEMAS
    opcao = st.sidebar.radio(
        "Selecione o Tema das Artes",
        [
            "🏛️ Cultos Gerais",
            "👨‍👩‍👧‍👦 Família",
            "🔥 Jovens",
            "🌸 Mulheres",
            "🧔 Homens",
            "🧸 Infantil",
            "🍷 Santa Ceia",
            "🎉 Datas Comemorativas",
            "💬 Suporte"
        ]
    )
    
    st.sidebar.markdown("---")
    if st.sidebar.button("Sair"):
        st.session_state.auth = False
        st.rerun()

    # --- 5. ROTEADOR INTERNO (Chama a página correta) ---
    if opcao == "🏛️ Cultos Gerais":
        tema_geral.exibir()
    elif opcao == "👨‍👩‍👧‍👦 Família":
        tema_familia.exibir()
    elif opcao == "🔥 Jovens":
        tema_jovens.exibir()
    elif opcao == "🌸 Mulheres":
        tema_mulheres.exibir()
    elif opcao == "🧔 Homens":
        tema_homens.exibir()
    elif opcao == "🧸 Infantil":
        tema_infantil.exibir()
    elif opcao == "🍷 Santa Ceia":
        tema_santa_ceia.exibir()
    elif opcao == "🎉 Datas Comemorativas":
        tema_comemorativo.exibir()
    elif opcao == "💬 Suporte":
        suporte.exibir()
