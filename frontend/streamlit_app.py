import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from backend.data.fetch_nasa_power import fetch_nasa_data
from backend.data.location_utils import get_location_info

st.set_page_config(page_title="SolarIQ", layout="wide")

# --- Header ---
st.title("🔆 SolarIQ – Solar Energy Forecasting")
st.markdown("Predict tomorrow’s solar irradiance using NASA weather data and machine learning.")

# --- Sidebar for user input ---
st.sidebar.header("📍 Location Settings")

# Option 1: Auto-detect location
use_auto_location = st.sidebar.checkbox("Auto-detect my location", value=True)

if use_auto_location:
    location = get_location_info()
    lat, lon = location['latitude'], location['longitude']
    st.sidebar.success(f"Detected: {location['city']} ({lat}, {lon})")
else:
    lat = st.sidebar.number_input("Latitude", value=28.6139)
    lon = st.sidebar.number_input("Longitude", value=77.2090)

# --- Fetch NASA weather data ---
if st.button("Fetch Weather Data"):
    with st.spinner("Fetching data from NASA POWER API..."):
        df = fetch_nasa_data(lat, lon)
        if df is not None and not df.empty:
            st.success("✅ Data fetched successfully!")
            st.dataframe(df.tail(7))

            # --- Show plot ---
            st.subheader("☀️ Historical Solar Irradiance")
            fig, ax = plt.subplots(figsize=(10, 4))
            ax.plot(df['ALLSKY_SFC_SW_DWN'].values, label='Irradiance', color='orange')
            ax.set_ylabel("kWh/m²/day")
            ax.set_xlabel("Days")
            ax.grid(True)
            st.pyplot(fig)
        else:
            st.error("Failed to fetch data. Please try again.")
