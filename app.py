# app.py
import streamlit as st

# Configuração da Página
st.set_page_config(page_title="Comunicando Igrejas", layout="wide", page_icon="📱")

# Carregando o CSS Premium (Fundo Preto)
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Importando os módulos
from modules import (
    vitrine, suporte, tema_geral, tema_familia, 
    tema_jovens, tema_mulheres, tema_homens, 
    tema_infantil, tema_santa_ceia, tema_comemorativo
)

# Gerenciamento de Login
if 'auth' not in st.session_state:
    st.session_state.auth = False

# --- FLUXO PRINCIPAL ---
if not st.session_state.auth:
    # 1. Exibe a Vitrine (A proposta de R$ 27 e o botão verde)
    vitrine.exibir()
    
    # 2. SEÇÃO DE ACESSO (Logo abaixo do botão de compra)
    st.markdown("---")
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown("""
            <div style='text-align: center; padding: 20px; border: 1px solid #333; border-radius: 15px; background-color: #0c0c0c;'>
                <h3 style='color: #FF2D95;'>Já possui acesso?</h3>
                <p>Entre com seus dados abaixo para acessar os templates.</p>
            </div>
        """, unsafe_allow_html=True)
        
        email = st.text_input("E-mail", placeholder="Seu e-mail de compra")
        senha = st.text_input("Senha", type="password", placeholder="Sua senha")
        
        if st.button("🔓 ENTRAR NA ÁREA DE MEMBROS", use_container_width=True):
            # Lógica de validação (Substitua pelas credenciais reais)
            if email == "admin@igreja.com" and senha == "123":
                st.session_state.auth = True
                st.rerun()
            else:
                st.error("Dados incorretos. Caso ainda não tenha o pack, clique no botão verde acima para comprar!")

else:
    # --- ÁREA EXCLUSIVA (Pós-Login) ---
    st.sidebar.markdown(f"<h2 style='color: #FF2D95;'>Olá, Varão!</h2>", unsafe_allow_html=True)
    
    opcao = st.sidebar.radio(
        "Navegue pelos Temas:",
        ["🏛️ Cultos Gerais", "👨‍👩‍👧‍👦 Família", "🔥 Jovens", "🌸 Mulheres", "🧔 Homens", "🧸 Infantil", "🍷 Santa Ceia", "🎉 Datas Comemorativas", "💬 Suporte"]
    )
    
    if st.sidebar.button("Sair"):
        st.session_state.auth = False
        st.rerun()

    # Roteador de Páginas
    if opcao == "🏛️ Cultos Gerais": tema_geral.exibir()
    elif opcao == "👨‍👩‍👧‍👦 Família": tema_familia.exibir()
    elif opcao == "🔥 Jovens": tema_jovens.exibir()
    elif opcao == "🌸 Mulheres": tema_mulheres.exibir()
    elif opcao == "🧔 Homens": tema_homens.exibir()
    elif opcao == "🧸 Infantil": tema_infantil.exibir()
    elif opcao == "🍷 Santa Ceia": tema_santa_ceia.exibir()
    elif opcao == "🎉 Datas Comemorativas": tema_comemorativo.exibir()
    elif opcao == "💬 Suporte": suporte.exibir()
