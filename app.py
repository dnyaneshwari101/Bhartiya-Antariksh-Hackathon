import streamlit as st
#from ui.chat_ui import run_chat_interface
#from ui.map_ui import display_map

st.set_page_config(page_title="GeoCoT-RAG Assistant", layout="wide")
st.title("🧠 GeoCoT-RAG Spatial Assistant")

# Sidebar with info
with st.sidebar:
    st.header("About")
    st.markdown("""
    Ask natural questions like:
    - "Show flood-prone areas in Kerala"
    - "Generate a map of high landslide risk zones"
    
    This tool uses Mistral + RAG + GIS logic.
    """)

# Layout: Chat + Map side by side
col1, col2 = st.columns([1, 2])
with col1:
    run_chat_interface()

with col2:
    display_map()
