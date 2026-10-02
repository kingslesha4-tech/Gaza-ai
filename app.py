import streamlit as st

st.set_page_config(page_title="King Slesha Moz Studio", page_icon="👑", layout="wide")

# CSS IGUAL DA FOTO - PRETO E OURO
st.markdown("""
<style>
.stApp {background-color:#070708; color:white}
h1, h2, h3 {color:#f7d774}
.card {
    background: #111113;
    border: 1px solid #f7d77440;
    border-radius: 20px;
    padding: 20px;
    box-shadow: 0 0 20px #f7d77415;
}
.gold-btn {
    background: linear-gradient(90deg,#f7d774,#ffcc33);
    color:black; font-weight:900; border-radius:14px; padding:12px;
    border:none; width:100%; font-size:18px;
}
.style-btn {
    background:#1a1a1a; border:1px solid #f7d77488; color:white;
    padding:10px; border-radius:12px; width:100%; text-align:left;
}
.style-btn.active {
    background:#f7d774; color:black; font-weight:800;
}
</style>
""", unsafe_allow_html=True)

# TOPO IGUAL DA FOTO
st.markdown("""
<div style="display:flex; justify-content:space-between; align-items:center; background:#111113; border:1px solid #f7d77440; border-radius:16px; padding:14px 20px;">
    <div style="display:flex; align-items:center; gap:12px">
        <div style="font-size:28px">〰️</div>
        <div><b style="color:#f7d774; font-size:20px">King Slesha Moz<br>Music Studio</b></div>
    </div>
    <div style="display:flex; gap:20px; color:#aaa">
        <span style="color:#f7d774; border-bottom:2px solid #f7d774"><b>Create</b></span>
        <span>Library</span><span>Projects</span><span>Sounds</span>
    </div>
    <div>🔔 ⚙️ <b style="background:#f7d774; color:black; border-radius:50%; padding:6px 12px">A</b> Alex</div>
</div>
<div style="text-align:right; margin-top:8px"><span style="background:#f7d774; color:black; border-radius:20px; padding:4px 12px; font-size:12px">Model: KingSlesha-Music v2.1</span></div>
""", unsafe_allow_html=True)

st.markdown("<h1>Create New Track</h1><p style='color:#aaa'>Generate original music with AI — lyrics, style, and voice in seconds</p>", unsafe_allow_html=True)

col1, col2 = st.columns([1.1, 0.9])

with col1:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("🟡 **LYRICS INPUT**")
    lyrics = st.text_area("Write your lyrics here...", height=280,
    placeholder="[Verse]\nCity lights flicker, late night thunder,\nRhythms echo, we rise up stronger,\nDancing through the silence...\n[Chorus]\nKing Slesha Moz...")

    c1, c2 = st.columns([1,1])
    with c1:
        st.button("✨ AI Enhance")
    with c2:
        st.caption(f"{len(lyrics)} / 1000 characters")
    st.caption("ℹ️ Tip: Use tags like [Chorus], [Verse], [Bridge] for better structure")
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("<center>🟡 INSTRUMENTAL STYLE</center>", unsafe_allow_html=True)

    # Botões estilo da foto
    r1c1, r1c2 = st.columns(2)
    with r1c1:
        instrumental = st.radio("Style", ["Amapiano", "Trap", "Kizomba"], label_visibility="collapsed")
        st.markdown(f"<div class='style-btn active'>〰️ {instrumental}</div>", unsafe_allow_html=True)
    with r1c2:
        st.selectbox(" ", ["Afrobeat", "Drill"], label_visibility="collapsed")

    # Seletores reais do Streamlit
    instrumental_choice = st.selectbox("Escolhe instrumental:", ["Amapiano", "Afrobeat", "Trap", "Drill", "Kizomba"])
    voice = st.selectbox("VOICE SELECTOR", ["Mali — Male, Warm & Smooth", "Nayara — Feminina Doce", "King Slesha — Original Moz"])

    col_t, col_d = st.columns(2)
    with col_t:
        st.metric("Tempo", "112 BPM")
        st.slider("Tempo", 80, 160, 112, label_visibility="collapsed")
    with col_d:
        st.metric("Duration", "2:30")
        st.slider("Dur", 30, 180, 150, label_visibility="collapsed")

    if st.button("✨ GENERATE", use_container_width=True):
        if not lyrics:
            st.warning("Escreve letra primeiro KING!")
        else:
            with st.spinner(f"King Slesha a gerar {instrumental_choice}..."):
                import time
                time.sleep(2)
            st.success(f"🔥 Hit {instrumental_choice} gerado!")
            st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")

    st.markdown('</div>', unsafe_allow_html=True)

# PLAYER EM BAIXO IGUAL FOTO
st.markdown("""
<div class="card" style="margin-top:20px; display:flex; justify-content:space-between; align-items:center">
    <div>🎵 <b>Untitled Track • Ready to Generate</b><br><small style="color:#888">No audio yet — generate to preview</small></div>
    <div>⏮️ ▶️ ⏭️</div>
    <div>🔊 ⬇️ 📤...</div>
</div>
<div style="text-align:center; color:#555; margin-top:10px">👑 King Slesha Moz Studio | Matola, Maputo 🇲🇿</div>
""", unsafe_allow_html=True)
