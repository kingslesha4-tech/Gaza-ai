import streamlit as st

st.set_page_config(page_title="Gaza AI - King Slesha", page_icon="🔥")

st.title("🔥 Gaza AI - King Slesha Moz")
st.write("Bem-vindo ao meu projeto AI!")

user_input = st.text_input("Pergunta algo para a Gaza AI:")

if user_input:
    st.success(f"Gaza AI responde: Recebi tua pergunta '{user_input}' - King Slesha está a trabalhar nisso! 🚀")

st.markdown("---")
st.caption("Criado por kingslesha4-tech")
