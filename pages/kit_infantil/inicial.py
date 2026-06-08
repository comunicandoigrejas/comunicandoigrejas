import streamlit as st

def exibir():
    st.markdown("<h2 style='text-align: center; color: white; font-weight: bold;'>🧸 KIT MINISTÉRIO INFANTIL</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #888; font-size: 0.95rem;'>Materiais de apoio, atividades educativas para colorir e visuais bíblicos para o Departamento Infantil.</p>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    kits = [
        {"titulo": "🎨 Desenhos para Colorir", "desc": "Compilado com dezenas de histórias bíblicas prontas para impressão e colorir na salinha.", "link": "https://sua-url-aqui.com"},
        {"titulo": "🎭 Roteiros de Teatro Infantil", "desc": "Peças teatrais bíblicas dinâmicas e curtas para datas especiais (Páscoa, Natal, etc).", "link": "https://sua-url-aqui.com"},
        {"titulo": "📑 Fichas de Presença Criativas", "desc": "Cartões de controle de presença estilizados e chamativos para motivar as crianças.", "link": "https://sua-url-aqui.com"},
    ]

    cols = st.columns(3)
    for idx, kit in enumerate(kits):
        with cols[idx % 3]:
            st.markdown(f"""
                <div style='background-color: #0c0c0c; border: 1px solid #222; border-radius: 8px; padding: 20px; min-height: 160px; margin-bottom: 10px;'>
                    <h4 style='color: #ffffff; margin-top:0;'>{kit['titulo']}</h4>
                    <p style='color: #888; font-size: 0.85rem;'>{kit['desc']}</p>
                </div>
            """, unsafe_allow_html=True)
            st.link_button("📥 DESCARREGAR KIT", kit['link'], use_container_width=True)