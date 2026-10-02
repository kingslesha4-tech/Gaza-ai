import streamlit as st
import time

st.set_page_config(page_title="Gaza AI Music Studio", page_icon="🎵", layout="wide")

st.markdown("""
<style>
.stApp {background:#0a0a0a; color:white}
.gold {color:#f7d774; font-weight:800}
.card {background:#151515; border:1px solid #f7d77444; border-radius:16px; padding:20px}
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='color:#f7d774'>🎵 Gaza AI Music Studio</h1><p>Model: Gaza-Music v2.1</p>", unsafe_allow_html=True)

col1, col2 = st.columns([1.2, 1])

with col1:
    st.markdown("### 📝 LYRICS INPUT")
    lyrics = st.text_area("Escreve tua letra:", height=250, placeholder="[Verse]\nCity lights...")
    instrumental = st.selectbox("Instrumental:", ["Amapiano", "Afrobeat", "Trap", "Drill", "Kizomba"])
    voice = st.selectbox("Voz:", ["Mali - Masculina Grave", "Nayara - Feminina Doce", "Zaza - AutoTune"])

with col2:
    st.markdown("### 🎚️ ESTILO")
    tempo = st.slider("Tempo BPM", 80, 160, 112)
    dur = st.slider("Duração (seg)", 30, 180, 90)

    if st.button("✨ GERAR MÚSICA", use_container_width=True):
        if not lyrics:
            st.warning("Escreve a letra primeiro KING!")
        else:
            bar = st.progress(0, text="Gerando...")
            for i in range(100):
                time.sleep(0.03)
                bar.progress(i+1)
            st.success("🔥 Música gerada! (DEMO)")
            st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")
            st.download_button("⬇️ Baixar MP3", data="demo", file_name="gaza_track.mp3")

st.info("💡 DEMO: Para música REAL com tua letra, próxima etapa é ligar API Suno")
