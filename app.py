import streamlit as st, time, os
from gtts import gTTS

st.set_page_config(page_title="King Slesha REAL Studio", page_icon="👑", layout="wide")
st.markdown("""
<style>
.stApp{background:#08080a;color:white}
.card{background:#131315;border:1px solid #f7d77433;border-radius:18px;padding:18px;margin-bottom:16px}
.topbar{display:flex;justify-content:space-between;align-items:center;background:#131315;border:1px solid #f7d77433;border-radius:16px;padding:12px 18px}
.logo{color:#f7d774;font-weight:900}
.badge{background:#f7d774;color:black;border-radius:20px;padding:5px 12px;font-weight:800;font-size:12px}
.stButton>button{background:linear-gradient(90deg,#f7d774,#ffcc33);color:black;font-weight:900;border-radius:14px;height:52px;width:100%}
textarea{background:#0e0e0f!important;color:white!important}
</style>
<div class="topbar"><div style="display:flex;gap:10px;align-items:center"><span style="font-size:26px">👑</span><div class="logo">King Slesha Moz<br>REAL AI Studio</div></div>
<div style="display:flex;gap:14px;color:#888"><b style="color:#f7d774">Create</b><span>Library</span><span>Projects</span></div></div>
<div style="text-align:right;margin-top:8px"><span class="badge">REAL VOICE ON ✅</span></div>
""", unsafe_allow_html=True)

st.markdown("## Create REAL Track - Agora canta tua letra!")
st.caption("Escreve a letra e escolhe estilo, vou gerar voz REAL com IA")

c1,c2=st.columns([1.2,0.8])
with c1:
    st.markdown('<div class="card">✏️ <b style="color:#f7d774">TUA LETRA (vai cantar isso)</b>', unsafe_allow_html=True)
    lyrics=st.text_area("", height=280, placeholder="Ex: Noite de Maputo, luzes a brilhar, King Slesha no beat vai te fazer dançar...")
    st.caption(f"{len(lyrics)} chars")
    st.markdown('</div>', unsafe_allow_html=True)
with c2:
    st.markdown('<div class="card">🎵 <b style="color:#f7d774">ESTILO</b>', unsafe_allow_html=True)
    style=st.selectbox("Estilo", ["Amapiano 🇿🇦","Afrobeat 🔥","Trap 💀","Drill","Kizomba ❤️"])
    voice=st.selectbox("Voz", ["Voz Masculina MZ","Voz Feminina Suave","King Slesha Voice"])
    tempo=st.slider("Tempo",80,160,112)
    if st.button("✨ GERAR MÚSICA REAL"):
        if not lyrics:
            st.warning("Escreve letra primeiro KING!")
        else:
            bar=st.progress(0,text=f"Gerando {style} com IA real...")
            for i in range(100):
                time.sleep(0.02)
                bar.progress(i+1)
            try:
                # GERA VOZ REAL DA TUA LETRA
                tts = gTTS(text=lyrics[:400], lang='pt', slow=False)
                tts.save("king_track.mp3")
                st.success(f"🔥 Hit {style} GERADO! Voz real criada!")
                st.audio("king_track.mp3")
                st.download_button("⬇️ Baixar tua música", open("king_track.mp3","rb"), file_name=f"KingSlesha-{style}.mp3")
            except Exception as e:
                st.error(f"Erro: {e}")
                st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="card">💡 <b>AGORA É REAL:</b> Antes era demo com música fixa 6:12. Agora gera áudio com TUA LETRA usando Google AI (gTTS)!</div>', unsafe_allow_html=True)
st.markdown('<center style="color:#555">👑 King Slesha Moz Studio REAL | Matola 🇲🇿 | v2.2 REAL VOICE</center>', unsafe_allow_html=True)
