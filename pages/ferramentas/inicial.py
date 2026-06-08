import streamlit as st

def exibir():
    st.markdown("<h2 style='text-align: center; color: white; font-weight: bold;'>🛠️ UTILITÁRIOS E FERRAMENTAS</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #888; font-size: 0.95rem;'>Links e utilitários recomendados para facilitar o dia a dia do seu departamento de mídia.</p>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    ferramentas = [
        {"nome": "✂️ Remove.bg", "desc": "Remova o fundo de qualquer foto ou imagem em apenas um clique de forma automática.", "link": "https://www.remove.bg/pt-br"},
        {"nome": "🎨 Paletas de Cores", "desc": "Encontre combinações perfeitas de cores para a identidade visual do seu evento.", "link": "https://coolors.co"},
        {"nome": "🔤 Dafont", "desc": "O maior acervo de fontes gratuitas para baixar e instalar no computador ou Canva Pro.", "link": "https://www.dafont.com/pt/"},
    ]

    cols = st.columns(3)
    for idx, ferr in enumerate(ferramentas):
        with cols[idx % 3]:
            st.markdown(f"""
                <div style='background-color: #0c0c0c; border: 1px solid #222; border-radius: 8px; padding: 20px; min-height: 160px; margin-bottom: 10px;'>
                    <h4 style='color: #00D2FF; margin-top:0;'>{ferr['nome']}</h4>
                    <p style='color: #888; font-size: 0.85rem;'>{ferr['desc']}</p>
                </div>
            """, unsafe_allow_html=True)
            st.link_button("🌐 ACESSAR SITE", ferr['link'], use_container_width=True)