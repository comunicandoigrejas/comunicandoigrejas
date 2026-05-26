import streamlit as st
import importlib

# PAGINAS disponíveis no sistema (Ajustado o título para bater com a imagem das categorias)
PAGINAS = [
    {"icone": "⛪", "titulo": "Culto em Geral",         "modulo": "pages.Cultos_Gerais"},
    {"icone": "🎉", "titulo": "Datas Comemorativas",  "modulo": "pages.Datas_Comemorativas"},
    {"icone": "👨‍👩‍👧‍👦", "titulo": "Culto da Família",     "modulo": "pages.Familia"},
    {"icone": "🧔", "titulo": "Culto de Homens",       "modulo": "pages.Homens"},
    {"icone": "🧸", "titulo": "Culto Infantil",         "modulo": "pages.Infantil"},
    {"icone": "🔥", "titulo": "Culto de Jovens",       "modulo": "pages.Jovens"},
    {"icone": "🌸", "titulo": "Culto de Mulheres",     "modulo": "pages.Mulheres"},
    {"icone": "🍷", "titulo": "Culto de Ceia",          "modulo": "pages.Santa_Ceia"},
]

def exibir():
    # Injeta estilos locais para remover a barra lateral e formatar o grid
    st.markdown("""
        <style>
        [data-testid="stSidebar"], [data-testid="stSidebarCollapseButton"] {
            display: none !important;
        }
        .block-container {
            padding-left: 3rem !important;
            padding-right: 3rem !important;
            max-width: 100% !important;
        }
        </style>
    """, unsafe_allow_html=True)

    # Tenta ler o style.css se ele existir na raiz
    try:
        with open("style.css") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    except:
        pass

    nome = st.session_state.get('nome_usuario', 'Irmão')
    plano = st.session_state.get('plano', 'PREMIUM') # Forçado PREMIUM para teste, mude para START se quiser testar bloqueio

    # Se uma página interna de artes estiver selecionada, renderiza ela e adiciona o botão de voltar
    if st.session_state.get('pagina_atual'):
        if st.button("⬅️ Voltar para o Menu de Categorias", key="btn_global_voltar"):
            st.session_state.pagina_atual = None
            st.rerun()
        st.markdown("<br>", unsafe_allow_html=True)
        
        try:
            modulo = importlib.import_module(st.session_state.pagina_atual)
            importlib.reload(modulo) 
            modulo.exibir()
        except Exception as e:
            st.error(f"Erro ao carregar a categoria: {e}")
        return

    # --- TELA PRINCIPAL DE CATEGORIAS ---
    st.markdown("<h1 style='text-align: center; font-weight: bold; color: white; letter-spacing: 2px;'>CATEGORIAS</h1>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center; color: #888;'>Olá, irmão {nome} | Abaixo estão as suas artes do plano {plano}</p>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    # Grid de botões: 4 colunas (Alinhado com a image_bf4460.jpg)
    cols = st.columns(4)
    
    for i, pagina in enumerate(PAGINAS):
        with cols[i % 4]:
            temas_premium = ["Culto de Ceia", "Culto de Mulheres", "Culto de Jovens"]
            e_premium = pagina['titulo'] in temas_premium
            
            label = f"{pagina['icone']}  {pagina['titulo']}"
            
            if e_premium and plano == "START":
                st.button(f"🔒 {pagina['titulo']}", key=f"btn_lock_{pagina['modulo']}", disabled=True, use_container_width=True)
                st.caption("<center style='color:#666;'>Disponível no Premium</center>", unsafe_allow_html=True)
            else:
                if st.button(label, key=f"btn_nav_{pagina['modulo']}", use_container_width=True):
                    st.session_state.pagina_atual = pagina['modulo']
                    st.rerun()

    st.markdown("<br><br><hr style='border-color: #1f1f1f;'>", unsafe_allow_html=True)
    if st.button("🚪 LOGOUT (SAIR DO SISTEMA)", use_container_width=True, key="btn_logout_sistema"):
        st.session_state.logado = False
        st.session_state.pagina_atual = None
        st.rerun()
