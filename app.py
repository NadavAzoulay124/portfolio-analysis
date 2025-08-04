import streamlit as st, pandas as pd, refinitiv.data as rd

# --- Page-wide config (appears in browser tab) --------------------
st.set_page_config(
    page_title="OBEX Analyzer",   # tab title
    page_icon="📈",               # favicon (any emoji or local file)
    layout="wide"                 # use full-width layout
)

# --- Visible banner inside the app --------------------------------
st.markdown(
    """
    <h1 style='text-align: center; font-size: 3rem; margin-bottom: 0.2em;'>
        🟢 OBEX&nbsp;<span style="color:#1f77b4;">Analyzer</span>
    </h1>
    <hr style='margin-top:0;'>
    """,
    unsafe_allow_html=True,
)