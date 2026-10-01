import streamlit as st
from google import genai

st.set_page_config(page_title="Gaza AI", page_icon="👑")
st.title("Gaza AI - King 👑")

try:
    api_key = st.secrets["gemini"]["api_key"]
    client = genai.Client(api_key=api_key)
except Exception as e:
    st.error(f"Erro na chave: {e}")
    st.stop()

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if prompt := st.chat_input("Fala King, o que precisa?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Pensando..."):
            try:
                response = client.models.generate_content(
                    model="gemini-2.0-flash",
                    contents=prompt
                )
                resposta = response.text
                st.markdown(resposta)
                st.session_state.messages.append({"role": "assistant", "content": resposta})
            except Exception as e:
                st.error(f"Erro: {e}")
