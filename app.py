import streamlit as st
import time

st.set_page_config(page_title="King Slesha Moz Studio", page_icon="👑", layout="wide")

st.markdown("""
<style>
.stApp {background:#08080a; color:white}
.card {background:#131315; border:1px solid #f7d77433; border-radius:18px; padding:18px; margin-bottom:16px}
.topbar {display:flex; align-items:center; justify-content:space-between; background:#131315; border:1px solid #f7d77433; border-radius:16px; padding:12px 18px; gap:10px}
.logo {color:#f7d774; font-weight:900; line-height:1.1; font-size:18px}
.menu {display:flex; gap:14px; color:#888; font-size:14px; flex-wrap:wrap}
.menu b {color:#f7d774; border-bottom:2px solid #f7d774}
.badge {background:#f7d774; color:black; border-radius:20px; padding:5px 12px; font-size:12px; font-weight:700; float:right; margin-top:8px}
.stButton>button {background:linear-gradient(90deg,#f7d774,#ffcc33); color:black; font-weight:900; border-radius:14px; height:52px; width:100%; border:none}
textarea {background:#0e0e0f!important; color:white!important}
</style>
""", unsafe_allow_html=True)

# TOPO FIXO MOBILE
st.markdown("""
<div class="topbar">
  <div style="display:flex; align-items:center; gap:10px">
    <span style="font-size:22px">〰️</span>
    <div class="logo">King Slesha Moz<br>Music Studio</div>
  </div>
  <div class="menu"><b>Create</b><span>Library</span><span>Projects</span><span>Sounds</span></div>
  <div style="font-size:18px">🔔 ⚙️ <span style="background:#f7d774; color:black; border-radius:50%; padding:4px 10px">A</span></div>
</div>
<div style="text-align:right"><span class="badge">Model: KingSlesha-Music v2.1</span></div>
""", unsafe_allow_html=True)

st.markdown("## Create New Track")
st.markdown("<p style='color:#888'>Generate original music with AI — lyrics, style, and voice in seconds</p>", unsafe_allow_html=True)

col1, col2 = st.columns([1.2, 0.8])

with col1:
    with st.container(border=False):
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("🟡 **LYRICS INPUT**")
        lyrics = st.text_area("Write your lyrics here...", height=260, placeholder="[Verse]\nCity lights flicker, late night thunder,\nRhythms echo, we rise up stronger\n[Chorus]\nKing Slesha Moz no beat...")
        c1,c2 = st.columns([1,1])
        c1.button("✨ AI Enhance")
        c2.caption(f"{len(lyrics)}/1000")
        st.caption("Tip: Use [Chorus], [Verse], [Bridge] for better structure")
        st.markdown('</div>', unsafe_allow_html=True)

with col2:
    with st.container(border=False):
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("<center>🟡 INSTRUMENTAL STYLE</center>", unsafe_allow_html=True)
        instrumental = st.selectbox("Style", ["Amapiano 🇿🇦", "Afrobeat 🔥", "Trap 💀", "Drill", "Kizomba ❤️"], index=0)
        st.markdown("<center>🟡 VOICE SELECTOR</center>", unsafe_allow_html=True)
        voice = st.selectbox("Voice", ["Mali — Male, Warm & Smooth", "Nayara — Feminina", "King Slesha — Original Moz"])

        t1,t2 = st.columns(2)
        t1.slider("Tempo", 80, 160, 112, format="%d BPM")
        t2.slider("Duration", 30, 180, 150, format="%d s")

        if st.button("✨ GENERATE"):
            if not lyrics:
                st.warning("Escreve letra KING!")
            else:
                bar = st.progress(0, text="King Slesha a cozinhar...")
                for i in range(100):
                    time.sleep(0.015)
                    bar.progress(i+1)
                st.success(f"🔥 {instrumental} pronto, KING!")
                st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")
                st.download_button("⬇️ Baixar Hit", data=lyrics.encode(), file_name="king_slesha_hit.mp3")
        st.markdown('</div>', unsafe_allow_html=True)

st.markdown("""
<div class="card" style="display:flex; justify-content:space-between; align-items:center; padding:12px 18px">
<b>🎵 Untitled Track • Ready to Generate</b> <span>⏮️ ▶️ ⏭️ &nbsp; 🔊 ⬇️</span>
</div>
<center style="color:#555; margin-top:8px">👑 King Slesha Moz Studio | Matola 🇲🇿 | 2026</center>
""", unsafe_allow_html=True)
