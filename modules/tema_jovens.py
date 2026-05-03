# modules/tema_jovens.py
import streamlit as st

def exibir():
    # Título Alinhado com o Tema (Use o estilo Premium que definimos no CSS)
    st.markdown("<h1 class='gradient-title'>Artes para Cultos Gerais</h1>", unsafe_allow_html=True)
    st.markdown("<p class='sub-title'>Templates editáveis para Cultos de Domingo, Celebração, Adoração e Doutrina.</p>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    # Organização em Colunas para os Packs (Perfeito para visualizar no celular)
    col1, col2 = st.columns(2)
    
    # --- PACK #01 (Adicione sua imagem em assets) ---
    with col1:
        st.markdown("<div class='premium-card'>", unsafe_allow_html=True)
        # Substitua "assets/artes_domingo.png" pelo caminho real da sua imagem
        st.image("assets/artes_domingo.png", caption="Culto de Celebração", use_container_width=True) 
        st.markdown("**Pack #01 - Culto de Adoração**")
        st.write("20 Templates 1:1 (Instagram)")
        # Substitua pelo seu link real do template do Canva
        st.link_button("Editar Pack Adoração", "https://www.canva.com/brand/join?token=...", use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)
    
    # --- PACK #02 (Placeholder para você preencher) ---
    with col2:
        st.markdown("<div class='premium-card'>", unsafe_allow_html=True)
        # st.image("assets/artes_familia.png", use_container_width=True) # Descomente e use quando tiver imagem
        st.markdown("**Pack #02 - Próximo Pack**")
        st.write("15 Templates 1:1 (Instagram)")
        # st.link_button("Editar Pack Família", "https://www.canva.com/...", use_container_width=True)
        st.write("Disponível em breve!")
        st.markdown("</div>", unsafe_allow_html=True)
        
    # Mensagem final de edificação (Opcional, usando ARA como preferido)
    st.markdown("---")
    st.write("Atenção: Novos packs são adicionados semanalmente!")
