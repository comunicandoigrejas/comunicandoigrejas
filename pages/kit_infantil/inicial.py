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

    # Lista estruturada com suporte a capas (Imagens em assets/)
    materiais_infantis = [
        {
            "titulo": "🔤 Atividades com Alfabeto", 
            "desc": "Material didático e lúdico com letras do alfabeto contextualizadas para o aprendizado.", 
            "link": "https://drive.google.com/drive/folders/1gokpOP_PkZUWxv-bGMhxXRdrRAMKJOnB?usp=drive_link",
            "capa": "Alfabeto.png" # ← Imagem adicionada conforme solicitado!
        },
        {
            "titulo": "🔢 Atividades com Números", 
            "desc": "Exercícios dinâmicos e atividades numéricas estruturadas para fixação e aprendizado infantil.", 
            "link": "https://drive.google.com/drive/folders/1KNfSYAuk2ZWOPL-91liNAPqxKgGi9F3F?usp=drive_link",
            "capa": None # Pronto para colocar o nome do arquivo quando você tiver
        },
        {
            "titulo": "📖 Bíblia Infantil", 
            "desc": "Histórias e visuais adaptados com linguagem simples e envolvente para o entendimento dos pequeninos.", 
            "link": "https://drive.google.com/drive/folders/1iFZlMEpedSIucCBmqkjEp_9zRM2zKFhe?usp=drive_link",
            "capa": None
        },
        {
            "titulo": "🎨 Bíblia para Colorir", 
            "desc": "Páginas com cenários e relatos bíblicos marcantes prontos para imprimir e as crianças colorirem.", 
            "link": "https://drive.google.com/drive/folders/1j2S-O4cHxPDqU3QTxpDnnZmKJjj1govv?usp=drive_link",
            "capa": None
        },
        {
            "titulo": "🖼️ Desenhos Bíblicos para Colorir", 
            "desc": "Compilado de ilustrações de personagens da fé separados para atividades na salinha infantil.", 
            "link": "https://drive.google.com/drive/folders/1mxWgSdMJLnWHMwLK4cdmo3_fc66edsxZ?usp=drive_link",
            "capa": None
        },
        {
            "titulo": "✝️ Parábolas de Jesus", 
            "desc": "Estudos e visuais focados nos ensinamentos práticos e histórias contadas por Cristo de forma ilustrada.", 
            "link": "https://drive.google.com/drive/folders/1I-Lal2q5x6EiynN76t8KRLbESUaW8Ae4?usp=drive_link",
            "capa": None
        },
    ]

    # Grid organizada em 3 colunas de exibição
    col1, col2, col3 = st.columns(3)

    for idx, item in enumerate(materiais_infantis):
        coluna_alvo = col1 if idx % 3 == 0 else (col2 if idx % 3 == 1 else col3)
        
        with coluna_alvo:
            caminho_capa = f"assets/{item['capa']}" if item.get('capa') else ""
            
            # 1. Se a imagem estiver configurada e existir na pasta assets, exibe ela primeiro
            if caminho_capa and os.path.exists(caminho_capa):
                st.image(caminho_capa, use_container_width=True)
            else:
                # 2. Caso contrário, exibe o bloco padrão escuro com o ícone/título para manter o alinhamento
                st.markdown(f"""
                    <div style='background-color: #0c0c0c; height: 180px; display: flex; 
                    align-items: center; justify-content: center; border-radius: 8px; 
                    color: #777; font-size:1.2rem; border: 1px solid #222; 
                    font-weight: bold; text-align: center; padding: 15px; margin-bottom: 5px;'>
                    {item['titulo']}
                    </div>
                """, unsafe_allow_html=True)
            
            # Botão oficial de download/direcionamento
            st.link_button("📥 ACESSAR MATERIAL", item['link'], use_container_width=True)
            st.markdown("<br>", unsafe_allow_html=True)