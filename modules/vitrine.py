import streamlit as st

# Criamos uma função chamada 'exibir'. 
# É ela que o app.py vai chamar quando o usuário clicar no menu.
def exibir():
    st.markdown("<h1 class='gradient-text'>🎨 Artes Canva</h1>", unsafe_allow_html=True)
    st.write("Bem-vindo à área de artes, varão! Escolha seu pack:")
    
    # Aqui você coloca o conteúdo da página de artes
    col1, col2 = st.columns(2)
    with col1:
        st.image("https://via.placeholder.com/500x500") # Exemplo 1:1
        st.link_button("Editar Pack de Culto", "https://canva.com/...")
