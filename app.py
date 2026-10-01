import streamlit as st
from datetime import datetime
try:
    from openai import OpenAI
    HAS_OPENAI = True
except:
    HAS_OPENAI = False

st.set_page_config(page_title="Gaza AI | King Slesha", page_icon="🔥", layout="centered")
st.markdown("""
<style>
.stApp { background-color: #0a0a0a; color: #FFD700; }
h1 { color: #FFD700 !important; text-align:center; font-family: Impact; letter-spacing:2px; }
.stChatInput textarea { background-color: #1a1a1a !important; color: #FFD700 !important; border: 1px solid #FFD700 !important; }
[data-testid="stChatMessage"] { background-color: #1a1a1a; border-left: 3px solid #FFD700; }
</style>
""", unsafe_allow_html=True)

st.markdown("<h1>🔥 GAZA AI - KING SLESHA MOZ 🔥</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:white;'>IA REAL da Matola com ChatGPT. Pergunta sem filtro, King.</p>", unsafe_allow_html=True)

if "messages" not in st.session_state:
    st.session_state.messages = [{"role":"system","content":"Você é Gaza AI, criada por King Slesha Moz da Matola, Moçambique. Você é gang, street, direta, fala português de Moçambique com gírias tipo 'King', 'brabo', 'hustle'. Você é inteligente pra caralho e ajuda com código, ideias, negócios. Responde sempre com vibe Gaza - preto e amarelo, Matola no topo."}]

for m in st.session_state.messages:
    if m["role"] != "system":
        with st.chat_message(m["role"]):
            st.write(m["content"])

if prompt := st.chat_input("Manda a braba aqui..."):
    st.session_state.messages.append({"role":"user","content":prompt})
    with st.chat_message("user"):
        st.write(prompt)
    with st.chat_message("assistant"):
        if HAS_OPENAI and "OPENAI_API_KEY" in st.secrets:
            client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
            stream = client.chat.completions.create(model="gpt-4o-mini", messages=st.session_state.messages, stream=True)
            resposta = st.write_stream(stream)
        else:
            resposta = "King, chave não encontrada! Verifica os Secrets no Streamlit!"
            st.write(resposta)
    st.session_state.messages.append({"role":"assistant","content":resposta})

st.caption(f"© {datetime.now().year} King Slesha Moz | Gaza AI v3.0 Real Brain | Matola")
