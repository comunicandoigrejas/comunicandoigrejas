import streamlit as st

def exibir():
    st.markdown("<h2 style='text-align: center; color: white; font-weight: bold;'>📁 KIT SECRETARIA DE IGREJA</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #888; font-size: 0.95rem;'>Modelos de documentos oficiais, fichas, certificados e relatórios prontos para uso administrativo.</p>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    documentos = [
        {"doc": "📝 Ficha de Membro", "desc": "Modelo pronto no Word e PDF para cadastro completo de novos convertidos e membros.", "link": "https://sua-url-aqui.com"},
        {"doc": "📜 Certificado de Batismo", "desc": "Template elegante e oficial configurado para impressão em papel diplomata.", "link": "https://sua-url-aqui.com"},
        {"doc": "📊 Relatório Financeiro", "desc": "Planilha inteligente simplificada para controle de entradas, saídas, dízimos e ofertas.", "link": "https://sua-url-aqui.com"},
    ]

    cols = st.columns(3)
    for idx, documento in enumerate(documentos):
        with cols[idx % 3]:
            st.markdown(f"""
                <div style='background-color: #0c0c0c; border: 1px solid #222; border-radius: 8px; padding: 20px; min-height: 160px; margin-bottom: 10px;'>
                    <h4 style='color: #ffffff; margin-top:0;'>{documento['doc']}</h4>
                    <p style='color: #888; font-size: 0.85rem;'>{documento['desc']}</p>
                </div>
            """, unsafe_allow_html=True)
            st.link_button("📥 BAIXAR MODELO", documento['link'], use_container_width=True)