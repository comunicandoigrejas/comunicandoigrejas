import streamlit as st
import os

def exibir():
    st.markdown("<h2 style='text-align: center; color: white; font-weight: bold;'>🧸 KIT MINISTÉRIO INFANTIL</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #888; font-size: 0.95rem;'>Materiais de apoio, atividades educativas para colorir e visuais bíblicos prontos para abençoar as crianças.</p>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    # CSS padrão para os botões e estilização dos cards do portal
    st.markdown("""
        <style>
        div.stButton > button {
            background-color: #ffffff !important;
            color: #000000 !important;
            font-weight: bold !important;
            font-size: 0.85rem !important;
            border-radius: 4px !important;
            border: none !important;
            padding: 6px 12px !important;
            transition: background-color 0.2s !important;
        }
        div.stButton > button:hover {
            background-color: #e5e5e5 !important;
            color: #000000 !important;
        }
        </style>
    """, unsafe_allow_html=True)

    # Lista estruturada com os materiais reais e links do Google Drive fornecidos
    materiais_infantis = [
        {
            "titulo": "🔤 Atividades com Alfabeto", 
            "desc": "Material didático e lúdico com letras do alfabeto contextualizadas para o aprendizado das crianças.", 
            "link": "https://drive.google.com/drive/folders/1gokpOP_PkZUWxv-bGMhxXRdrRAMKJOnB?usp=drive_link"
        },
        {
            "titulo": "🔢 Atividades com Números", 
            "desc": "Exercícios dinâmicos e atividades numéricas estruturadas para fixação e aprendizado infantil.", 
            "link": "https://drive.google.com/drive/folders/1KNfSYAuk2ZWOPL-91liNAPqxKgGi9F3F?usp=drive_link"
        },
        {
            "titulo": "📖 Bíblia Infantil", 
            "desc": "Histórias e visuais adaptados com linguagem simples e envolvente para o entendimento dos pequeninos.", 
            "link": "https://drive.google.com/drive/folders/1iFZlMEpedSIucCBmqkjEp_9zRM2zKFhe?usp=drive_link"
        },
        {
            "titulo": "🎨 Bíblia para Colorir", 
            "desc": "Páginas com cenários e relatos bíblicos marcantes prontos para imprimir e as crianças colorirem.", 
            "link": "https://drive.google.com/drive/folders/1j2S-O4cHxPDqU3QTxpDnnZmKJjj1govv?usp=drive_link"
        },
        {
            "titulo": "🖼️ Desenhos Bíblicos para Colorir", 
            "desc": "Compilado de ilustrações de personagens da fé separados para atividades na salinha ou departamento infantil.", 
            "link": "https://drive.google.com/drive/folders/1mxWgSdMJLnWHMwLK4cdmo3_fc66edsxZ?usp=drive_link"
        },
        {
            "titulo": "✝️ Parábolas de Jesus", 
            "desc": "Estudos e visuais focados nos ensinamentos práticos e histórias contadas por Cristo de forma ilustrada.", 
            "link": "https://drive.google.com/drive/folders/1I-Lal2q5x6EiynN76t8KRLbESUaW8Ae4?usp=drive_link"
        },
    ]

    # Grid organizada em 3 colunas de exibição responsivas
    col1, col2, col3 = st.columns(3)

    for idx, item in enumerate(materiais_infantis):
        # Distribuição dos blocos entre as colunas do layout
        coluna_alvo = col1 if idx % 3 == 0 else (col2 if idx % 3 == 1 else col3)
        
        with coluna_alvo:
            # Caixa do Card em HTML/CSS para manter o padrão moderno, limpo e escuro do portal
            st.markdown(f"""
                <div style='background-color: #0c0c0c; border: 1px solid #222; border-radius: 8px; padding: 20px; min-height: 165px; margin-bottom: 12px;'>
                    <h4 style='color: #ffffff; margin-top:0; font-size:1.1rem; font-weight:bold;'>{item['titulo']}</h4>
                    <p style='color: #888; font-size: 0.85rem; line-height: 1.4; margin-top: 8px;'>{item['desc']}</p>
                </div>
            """, unsafe_allow_html=True)
            
            # Botão oficial para abrir a pasta do Drive em uma nova guia
            st.link_button("📥 ACESSAR MATERIAL", item['link'], use_container_width=True)
            st.markdown("<br>", unsafe_allow_html=True)