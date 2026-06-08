import streamlit as st

def exibir():
    st.markdown("<h2 style='text-align: center; color: white; font-weight: bold;'>📖 ESBOÇOS E SERMÕES PRONTOS</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #888; font-size: 0.95rem;'>Inspirações, esboços homiléticos e estudos bíblicos estruturados na versão ARA (Almeida Revista e Atualizada).</p>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    sermoes_lista = [
        {"tema": "🔥 O Despertar da Fé Verdadeira", "ref": "Romanos 10:17 (ARA)", "desc": "Esboço completo focado em santificação e o ouvir da Palavra de Deus.", "link": "https://sua-url-aqui.com"},
        {"tema": "🛡️ Guardando a Fé no Século Presente", "ref": "2 Timóteo 4:7 (ARA)", "desc": "Estudo aprofundado sobre perseverança cristã e a carreira do cristão.", "link": "https://sua-url-aqui.com"},
        {"tema": "🌊 As Águas Profundas do Espírito", "ref": "Ezequiel 47 (ARA)", "desc": "Mensagem avivada sobre comunhão contínua e intimidade na oração.", "link": "https://sua-url-aqui.com"},
    ]

    cols = st.columns(3)
    for idx, sermao in enumerate(sermoes_lista):
        with cols[idx % 3]:
            st.markdown(f"""
                <div style='background-color: #0c0c0c; border: 1px solid #222; border-radius: 8px; padding: 20px; min-height: 160px; margin-bottom: 10px;'>
                    <h4 style='color: #ffffff; margin-top:0;'>{sermao['tema']}</h4>
                    <small style='color: #2da042; font-weight: bold;'>📖 {sermao['ref']}</small>
                    <p style='color: #888; font-size: 0.85rem; margin-top: 8px;'>{sermao['desc']}</p>
                </div>
            """, unsafe_allow_html=True)
            st.link_button("📖 ABRIR ESBOÇO", sermao['link'], use_container_width=True)