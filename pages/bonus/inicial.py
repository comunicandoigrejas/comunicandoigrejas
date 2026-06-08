import streamlit as st
import os

def exibir():
    st.markdown("<h2 style='text-align: center; color: white; font-weight: bold;'>🎁 ÁREA DE BÔNUS EXCLUSIVOS</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #888; font-size: 0.95rem;'>Aproveite os materiais extras selecionados para potencializar a comunicação da sua igreja.</p>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    # Lista de bônus (Exemplo estruturado para você preencher os links de download)
    materiais_bonus = [
        {"titulo": "🔥 Pacote de Elementos 3D", "desc": "Imagens em alta definição sem fundo para usar em cartazes.", "link": "https://sua-url-aqui.com"},
        {"titulo": "🎨 Texturas & Backgrounds Bokeh", "desc": "Fundos iluminados para dar profundidade aos seus designs.", "link": "https://sua-url-aqui.com"},
        {"titulo": "✍️ Lista de Fontes que Combinam", "desc": "Guia prático com as melhores combinações de fontes no Canva.", "link": "https://sua-url-aqui.com"},
    ]

    cols = st.columns(3)
    for idx, item in enumerate(materiais_bonus):
        with cols[idx % 3]:
            st.markdown(f"""
                <div style='background-color: #0c0c0c; border: 1px solid #222; border-radius: 8px; padding: 20px; min-height: 160px; margin-bottom: 10px;'>
                    <h4 style='color: #ffffff; margin-top:0;'>{item['titulo']}</h4>
                    <p style='color: #888; font-size: 0.85rem;'>{item['desc']}</p>
                </div>
            """, unsafe_allow_html=True)
            st.link_button("📥 BAIXAR MATERIAL", item['link'], use_container_width=True)