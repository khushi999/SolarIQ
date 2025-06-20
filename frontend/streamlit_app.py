import sys
import os
# Add the parent directory to the path to find backend modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import torch
from streamlit_js_eval import streamlit_js_eval
from backend.data.fetch_nasa_power import fetch_nasa_power_data
from backend.data.location_utils import get_user_location_from_browser
from backend.model_training.model import SolarLSTM
from backend.model_training.config import INPUT_SIZE, HIDDEN_SIZE, NUM_LAYERS, MODEL_SAVE_PATH

st.set_page_config(page_title="SolarIQ", layout="wide")

# --- Header ---
st.title("🔆 SolarIQ – Solar Energy Forecasting")
st.markdown("Predict tomorrow's solar irradiance using NASA weather data and machine learning.")

# --- Sidebar for user input ---
st.sidebar.header("📍 Location Settings")

use_auto_location = st.sidebar.checkbox("Auto-detect my location", value=True)

if use_auto_location:
    # Get browser location
    browser_location = streamlit_js_eval(
        js_expressions="""
        new Promise((resolve, reject) => {
            if (navigator.geolocation) {
                navigator.geolocation.getCurrentPosition(
                    (pos) => resolve({lat: pos.coords.latitude, lon: pos.coords.longitude}),
                    (err) => resolve(null)
                );
            } else {
                resolve(null);
            }
        })
        """,
        key="get_location"
    )
    
    # Get location details using the browser location
    city, lat, lon = get_user_location_from_browser(browser_location)
    
    st.sidebar.success(f"📍 Detected Location: {city} ({lat:.2f}, {lon:.2f})")
    st.markdown(f"🌐 Forecasting results for **{city}**, located at ({lat:.2f}, {lon:.2f})")
else:
    lat = st.sidebar.number_input("Latitude", value=28.6139)
    lon = st.sidebar.number_input("Longitude", value=77.2090)

# --- Fetch Button ---
if st.button("Fetch Weather Data"):
    with st.spinner("Fetching data from NASA POWER API..."):
        end_date = datetime.today().strftime("%Y%m%d")
        start_date = (datetime.today() - timedelta(days=365)).strftime("%Y%m%d")
        df = fetch_nasa_power_data(lat, lon, start_date, end_date)
        
        if df is not None:
            df = df[
                (df['solar_irradiance'] != -999) &
                (df['temperature'] != -999) &
                (df['humidity'] != -999)
            ]

            if not df.empty:
                st.session_state['df'] = df
                st.success("✅ Data fetched successfully!")
                st.dataframe(df.tail(7))
            else:
                st.error("No valid data points found. Please try a different location or date range.")
        else:
            st.error("Failed to fetch data. Please try again.")

# --- Display if data exists ---
if 'df' in st.session_state:
    df = st.session_state['df']

    # --- Historical Plot ---
    st.subheader("☀️ Historical Solar Irradiance")
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(df['solar_irradiance'].values, label='Irradiance', color='orange')
    ax.set_ylabel("kWh/m²/day")
    ax.set_xlabel("Days")
    ax.grid(True)
    st.pyplot(fig)

    # --- Prediction ---
    st.subheader("🔮 Tomorrow's Solar Forecast")
    last_7_days = df.tail(7)[['solar_irradiance', 'temperature', 'humidity']].values

    if last_7_days.shape == (7, 3):
        sequence = torch.tensor(last_7_days, dtype=torch.float32).unsqueeze(0)
        model = SolarLSTM(input_size=INPUT_SIZE, hidden_size=HIDDEN_SIZE, num_layers=NUM_LAYERS)
        model.load_state_dict(torch.load(MODEL_SAVE_PATH))
        model.eval()

        with torch.no_grad():
            prediction = model(sequence).item()
            st.session_state['prediction'] = prediction

        st.success(f"Predicted Solar Irradiance for Tomorrow: **{prediction:.3f} kWh/m²/day**")
    else:
        st.warning("Insufficient data for prediction. Need 7 valid recent days.")

    # --- Savings Calculator ---
    st.subheader("💰 Solar Savings Calculator")
    with st.form("savings_form"):
        system_size = st.number_input("Solar system size (in kW)", min_value=0.1, value=3.0)
        efficiency = st.slider("System efficiency (%)", min_value=10, max_value=100, value=80)
        electricity_rate = st.number_input("Electricity rate ($/kWh)", min_value=1.0, value=6.0)
        submitted = st.form_submit_button("Estimate Savings")

    if submitted:
        try:
            if 'prediction' not in st.session_state:
                st.warning("Please fetch prediction first.")
            else:
                predicted_irradiance = float(st.session_state['prediction'])
                daily_energy_kwh = predicted_irradiance * system_size * (efficiency / 100)
                estimated_savings = daily_energy_kwh * electricity_rate

                st.success(
                    f"🔋 Estimated Solar Energy: **{daily_energy_kwh:.2f} kWh/day**\n"
                    f"💸 Estimated Daily Savings: **${estimated_savings:.2f}**"
                )
        except Exception as e:
            st.error(f"Error: {e}")
