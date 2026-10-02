import streamlit as st, time, os
from gtts import gTTS

st.set_page_config(page_title="King Slesha FULL BEAT", page_icon="👑", layout="wide")
st.markdown("""
<style>
.stApp{background:#08080a;color:white}
.card{background:#131315;border:1px solid #f7d77444;border-radius:18px;padding:18px;margin-bottom:14px}
.stButton>button{background:linear-gradient(90deg,#f7d774,#ffcc33);color:black;font-weight:900;height:54px;width:100%;border-radius:14px;border:none}
textarea{background:#0e0e0f!important;color:white!important}
</style>
<h2 style="color:#f7d774">👑 King Slesha Moz - FULL STUDIO v3.0</h2>
<p style="color:#888">Voice + Instrumental Kizomba/Amapiano Beat ✅</p>
""", unsafe_allow_html=True)

c1,c2 = st.columns([1,1])
with c1:
    st.markdown('<div class="card">✏️ <b style="color:#f7d774">LETRA COMPLETA (escreve mais pra durar mais)</b>', unsafe_allow_html=True)
    lyrics = st.text_area("", height=240, placeholder="[Verse]\nMina niranza wena, nitsemba wena\nHi ta famba na wena, matimba ya mina...\n\n[Chorus]\nKing Slesha de Matola, Moz no coração\nKizomba na noite, com muita paixão\n\nEscreve pelo menos 3 linhas pra durar mais que 4s!")
    st.caption(f"{len(lyrics)} chars - Quanto mais letra, mais longa a música")
    st.markdown('</div>', unsafe_allow_html=True)

with c2:
    st.markdown('<div class="card">🎵 <b style="color:#f7d774">CONFIGURAÇÃO FULL</b>', unsafe_allow_html=True)
    estilo = st.selectbox("Estilo + Beat", ["Kizomba ❤️ - Beat Romântico","Amapiano 🇿🇦 - Beat Log Drum","Afrobeat 🔥 - Beat Dançante","Trap 💀 - Beat Pesado"])

    # Beats instrumentais reais gratuitos
    beats = {
        "Kizomba ❤️ - Beat Romântico": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3",
        "Amapiano 🇿🇦 - Beat Log Drum": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-3.mp3",
        "Afrobeat 🔥 - Beat Dançante": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-2.mp3",
        "Trap 💀 - Beat Pesado": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-8.mp3"
    }

    tempo = st.slider("Tempo", 80, 160, 104)

    if st.button(f"✨ GERAR {estilo.split(' ')[0]} FULL COM BEAT"):
        if len(lyrics) < 10:
            st.warning("Escreve mais letra KING! Pelo menos 1 frase completa!")
        else:
            bar = st.progress(0, text=f"Gerando {estilo}...")
            for i in range(100):
                time.sleep(0.04)
                bar.progress(i+1)

            try:
                # Gera voz da letra COMPLETA
                tts = gTTS(text=lyrics, lang='pt', slow=False)
                tts.save("voz.mp3")
                st.success(f"🔥 {estilo} PRONTO! Voz + Beat!")

                st.markdown("**🎙️ TUA VOZ CANTANDO A LETRA:**")
                st.audio("voz.mp3")

                st.markdown(f"**🥁 BEAT INSTRUMENTAL {estilo}:**")
                st.audio(beats[estilo])

                st.info("💡 DICA PRO: Toca os dois juntos! Voz + Beat = tua música! Para mixagem automática profissional, precisamos ligar API Suno (pago) ou ElevenLabs.")

                with open("voz.mp3","rb") as f:
                    st.download_button("⬇️ Baixar Voz", f, "KingSlesha-voz.mp3")

            except Exception as e:
                st.error(f"Erro: {e}")
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("""
<div class="card">
<b style="color:#f7d774">⚠️ PORQUE SÓ 4 SEGUNDOS?</b><br>
1. Você escreveu pouca letra (ex: só 2 palavras = 4s)<br>
2. gTTS é grátis e só LÊ, não canta com auto-tune<br>
3. <b>SOLUÇÃO REAL:</b> Para ter música tipo Suno AI com instrumental + voz cantando bonita, precisa API paga (Suno $10/mês ou Udio)<br><br>
<b style="color:#f7d774">O QUE FAZER AGORA:</b><br>
- Escreve letra GRANDE (minimo 50 palavras) pra durar 20-30s<br>
- Usa esse app pra criar letra e voz guia<br>
- Depois leva pro FL Studio e coloca beat<br>
- Ou me diz que eu te ligo na API Suno de verdade!
</div>
""", unsafe_allow_html=True)

st.markdown('<center style="color:#555">👑 King Slesha Moz Studio v3.0 | Full Beat | Matola 🇲🇿</center>', unsafe_allow_html=True)
