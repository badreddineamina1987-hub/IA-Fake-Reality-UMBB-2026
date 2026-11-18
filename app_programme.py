"""Écran programme du colloque (défilement automatique) — Streamlit."""
from pathlib import Path
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Programme — الملتقى الوطني · UMBB 19.11.2026",
    page_icon="⚠️",
    layout="wide",
    initial_sidebar_state="collapsed",
)
# Masquer l'interface Streamlit pour un affichage plein écran
st.markdown(
    """<style>
    header, footer, #MainMenu, [data-testid="stToolbar"], [data-testid="stDecoration"] {display:none !important;}
    .block-container {padding:0 !important; max-width:100% !important;}
    .stApp {background:#000;}
    iframe {display:block; width:100vw !important; height:100vh !important; border:0;}
    </style>""",
    unsafe_allow_html=True,
)
html = Path(__file__).with_name("programme.html").read_text(encoding="utf-8")
components.html(html, height=1000, scrolling=False)
