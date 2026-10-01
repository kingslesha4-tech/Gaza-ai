import streamlit as st
import random
from datetime import datetime

st.set_page_config(
    page_title="Gaza AI | King Slesha",
    page_icon="🔥",
    layout="centered"
)

# --- ESTILO GAZA GANGS ---
st.markdown("""
<style>
    .stApp { background-color: #0a0a0a; color: #FFD700; }
    h1, h2, h3 { color: #FFD700 !important; font-family: 'Impact', sans-serif; text-transform: uppercase; letter-spacing: 2px; }
    .stTextInput input, .stChatInput textarea { background-color: #1a1a1a !important; color: #FFD700 !important; border: 1px solid #FFD700 !important; }
    .stButton button { background-color: #FFD700; color: black; font-weight: bold; border: none; border-radius: 0px; }
    .stButton button:hover { background-color: white; color: black; }
    [data-testid="stChatMessage"] { background-color: #1a1a1a; border-left: 3px solid #FFD700; }
    footer { visibility: hidden; }
</style>
""", unsafe_allow_html=True)

# --- HEADER ---
st.markdown("<h1 style='text-align:center;'>🔥 GAZA AI - KING SLESHA MOZ 🔥</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:white;'>A IA mais gang da Matola. Pergunta o que quiser, sem filtro.</p>", unsafe_allow_html=True)
st.markdown("---")

# --- MEMÓRIA DO CHAT ---
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Yo King Slesha! Fala comigo, o que queres saber hoje? 🔥💀"}
    ]

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# --- CÉREBRO DA GAZA AI ---
def gaza_responder(pergunta):
    p = pergunta.lower()
    
    respostas_gaza = [
        f"Boa pergunta King: '{pergunta}'... Na Gaza a gente resolve assim: foco, hustle e nunca parar! 🔥",
        f"Entendi '{pergunta}'. Olha, na visão da Matola, isso é sobre visão de futuro. King Slesha tem que meter força nisso!",
        f"'{pergunta}'? Isso é papo de gajo que quer vencer. Eu, Gaza AI, digo: vai com tudo, sem medo da falha!",
        f"Fala sério, '{pergunta}' é interessante. Se fosse eu, pesquisava mais fundo e fazia acontecer. Gaza style! 💀"
    ]
    
    if "quem es" in p or "quem é você" in p or "quem é vc" in p:
        return "Eu sou Gaza AI, criado pelo brabo King Slesha Moz diretamente da Matola! Sou a IA mais street de Moçambique. 🔥"
    if "moçambique" in p or "moz" in p:
        return "Moz é o país! Gaza é a mentalidade! King Slesha tá a representar Matola pro mundo! 🇲🇿🔥"
    if "codigo" in p or "programar" in p or "python" in p:
        return f"Queres código pra '{pergunta}'? King, me diz mais detalhes que eu te monto o código completo aqui, estilo pro!"

    return random.choice(respostas_gaza)

# --- INPUT ---
if prompt := st.chat_input("Manda a braba aqui..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    resposta = gaza_responder(prompt)
    
    with st.chat_message("assistant"):
        st.write(resposta)
    st.session_state.messages.append({"role": "assistant", "content": resposta})

st.markdown("---")
st.caption(f"© {datetime.now().year} King Slesha Moz | Gaza AI v2.0 - Online 24/7 | Matola City")
