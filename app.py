import streamlit as st
import google.generativeai as genai

# Configuração da página
st.set_page_config(page_title="Gaza AI", page_icon="🤖")
st.title("Gaza AI - King 👑")

# Pega a chave dos Secrets
try:
    api_key = st.secrets["gemini"]["api_key"]
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-1.5-flash")
except Exception as e:
    st.error(f"Erro na chave: {e}")
    st.stop()

# Histórico de chat
if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Input do usuário
if prompt := st.chat_input("Fala King, o que precisa?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Pensando..."):
            try:
                response = model.generate_content(prompt)
                resposta = response.text
                st.markdown(resposta)
                st.session_state.messages.append({"role": "assistant", "content": resposta})
            except Exception as e:
                st.error(f"Erro: {e}")
