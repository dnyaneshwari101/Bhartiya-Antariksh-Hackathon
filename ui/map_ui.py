import streamlit as st
import folium
from streamlit_folium import st_folium

def display_map():
    st.subheader("🗺️ Generated Map")

    # Placeholder: Replace this with GIS result map later
    m = folium.Map(location=[10.85, 76.27], zoom_start=7)  # Centered on Kerala

    folium.Marker([10.85, 76.27], tooltip="Kerala Center").add_to(m)

    # Show map
    st_folium(m, width=700, height=500)
