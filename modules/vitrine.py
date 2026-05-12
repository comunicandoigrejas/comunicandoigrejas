import streamlit as st
import os

def exibir():
    def carregar_imagem(nome_arquivo):
        caminho = f"assets/{nome_arquivo}"
        if os.path.exists(caminho):
            st.image(caminho, use_container_width=True)
        else:
            st.warning(f"⚠️ Imagem não encontrada: {nome_arquivo}")
            st.info("Verifique se a pasta 'assets' está no GitHub")

    # Banner principal
    carregar_imagem("hero_mockup.png")

    # ... (o resto do código permanece igual)
