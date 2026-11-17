"""Version Streamlit de la présentation (Streamlit Community Cloud)."""
from pathlib import Path
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="IA & fabrication du réel — Dr. BADREDDINE Amina",
    page_icon="⚠️",
    layout="wide",
    initial_sidebar_state="collapsed",
)
st.markdown(
    "<style>header, footer {visibility:hidden;} .block-container {padding:0; max-width:100%;}</style>",
    unsafe_allow_html=True,
)
html = Path(__file__).with_name("index.html").read_text(encoding="utf-8")
components.html(html, height=860, scrolling=False)
