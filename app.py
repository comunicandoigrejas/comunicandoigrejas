import streamlit as st

def exibir_painel_vendas():
    st.markdown("---")
    st.markdown("<h2 style='text-align: center; color: #FF2D95;'>💎 Conheça os Nossos Planos</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #888888;'>Tenha acesso às melhores artes profissionais para a sua igreja.</p>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    # Criação das colunas para os dois planos lado a lado
    vendas_col1, vendas_col2 = st.columns(2)

    with vendas_col1:
        st.markdown("""
            <div style='background-color: #0c0c0c; border: 1px solid #1f1f1f; border-radius: 15px; padding: 25px; text-align: center;'>
                <h3 style='color: #00D2FF;'>🚀 Plano START</h3>
                <p style='font-size: 0.9rem; color: #bbbbbb;'>Ideal para igrejas que estão a começar a organizar as suas redes sociais.</p>
                <hr style='border-color: #1f1f1f;'>
                <ul style='text-align: left; font-size: 0.95rem; color: #dddddd; line-height: 1.8;'>
                    <li>✅ Acesso a <b>Cultos Gerais</b></li>
                    <li>✅ Acesso a <b>Datas Comemorativas</b></li>
                    <li>✅ Acesso a <b>Família e Homens</b></li>
                    <li>✅ Acesso a <b>Infantil</b></li>
                    <li>❌ Conteúdos Premium Bloqueados</li>
                </ul>
                <hr style='border-color: #1f1f1f;'>
                <p style='color: #888888; margin-bottom: 0;'>Acesso Vitalício por apenas</p>
                <h2 style='color: #ffffff; margin-top: 5px;'>R$ 27,00</h2>
            </div>
        """, unsafe_allow_html=True)

    with vendas_col2:
        st.markdown("""
            <div style='background-color: #0c0c0c; border: 1px solid #FF2D95; border-radius: 15px; padding: 25px; text-align: center; box-shadow: 0 0 15px rgba(255, 45, 149, 0.2);'>
                <h3 style='color: #FF2D95;'>👑 Plano PREMIUM</h3>
                <p style='font-size: 0.9rem; color: #bbbbbb;'>O pacote completo com atualizações e artes exclusivas de departamentos.</p>
                <hr style='border-color: #1f1f1f;'>
                <ul style='text-align: left; font-size: 0.95rem; color: #dddddd; line-height: 1.8;'>
                    <li>✅ <b>Todos os benefícios</b> do plano Start</li>
                    <li>🔥 Acesso exclusivo ao módulo de <b>Jovens</b></li>
                    <li>🌸 Acesso exclusivo ao módulo de <b>Mulheres</b></li>
                    <li>🍷 Acesso exclusivo ao módulo de <b>Santa Ceia</b></li>
                    <li>✨ Suporte e atualizações de novos templates</li>
                </ul>
                <hr style='border-color: #1f1f1f;'>
                <p style='color: #888888; margin-bottom: 0;'>Acesso Vitalício por apenas</p>
                <h2 style='color: #FF2D95; margin-top: 5px;'>Consulte as Condições</h2>
            </div>
        """, unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

# --- DENTRO DA FUNÇÃO PRINCIPAL DE RENDERIZAÇÃO DA PÁGINA (Ex: no app.py ou Dashboard.py) ---
# Altere a lógica final onde as páginas são exibidas para incluir esta verificação:

# Se o utilizador NÃO selecionou nenhuma página ainda, mostra o painel informativo
if not st.session_state.get('pagina_atual'):
    exibir_painel_vendas()
