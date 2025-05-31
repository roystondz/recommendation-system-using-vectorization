# app.py
import streamlit as st
from recommend import df, recommend_songs

# --- Page Config ---
st.set_page_config(
    page_title="TuneMatch | Music Recommender",
    page_icon="🎧",
    layout="centered"
)

# --- Title and Subtitle ---
st.markdown("<h1 style='text-align: center;'>🎶 TuneMatch: Music Recommender</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Get smart recommendations based on your favorite track.</p>", unsafe_allow_html=True)
st.markdown("<hr>", unsafe_allow_html=True)

# --- Song Selection ---
song_list = sorted(df['song'].dropna().unique())
selected_song = st.selectbox("🎵 Select a song you like:", song_list)

# --- Recommend Button ---
if st.button("🚀 Recommend Similar Songs"):
    with st.spinner("Finding similar songs..."):
        recommendations = recommend_songs(selected_song)

    # ✅ Check if None or Empty
    if recommendations is None or recommendations.empty:
        st.error("❌ No recommendations found. Try a different song.")
    else:
        st.success("✅ Top Recommended Songs:")
        st.markdown("")

        # ✅ Display recommendations (as table or styled box)
        st.table(recommendations)

# --- Footer ---
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown(
    "<p style='text-align: center; font-size: 0.9rem; color: gray;'>"
    "© 2025 TuneMatch | Built with ❤️ using Streamlit | Royston Akash Dsouza</p>",
    unsafe_allow_html=True
)
