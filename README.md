### 🌞 SolarIQ — ML-Powered Solar Forecasting App

> Forecast daily solar energy generation for your location using weather data from NASA and machine learning.

---

### 📌 About the Project

**SolarIQ** is a climate tech product that uses global weather data and time series modeling to:

* Predict next-day solar power output
* Estimate cost savings based on system size and electricity rates *(coming soon)*
* Provide an easy-to-use interface for homeowners, solar agents, students, and researchers

Originally based on Open Climate Fix's UK dataset, the project **pivoted to NASA POWER API** to allow **location-based, real-time forecasts** globally.

---

### 🔍 How It Works

1. **Location Detection**
   - Detects user location using IP (via ipinfo.io)

2. **Data**
   - Fetches solar irradiance, temperature, and humidity using [NASA POWER API](https://power.larc.nasa.gov/)

3. **Processing**
   - Cleans and scales the data
   - Creates 7-day rolling input sequences for prediction

4. **Modeling**
   - (Coming soon) Train an LSTM-based time series model

5. **UI**
   - (Coming soon) Streamlit interface where users input location/system size and get a forecast & savings estimate

---

### 📊 Sample Output

A snapshot of normalized solar irradiance from NASA POWER API for the past year:

![Solar Irradiance Plot](assets/solar_irradiance_plot.png)

---

### 📁 Project Structure

SolarIQ/
├── backend/
│   ├── data/
│   │   ├── fetch_nasa_power.py
│   │   └── location_utils.py
│   └── model_training/
│       ├── clean_nasa_data.py
│       └── create_sequences.py
├── data/
│   ├── raw/              # Unprocessed NASA data
│   └── processed/        # Cleaned & scaled CSVs
├── frontend/
│   └── streamlit_app.py  # WIP UI for user interaction
├── assets/
│   └── solar_irradiance_plot.png
├── requirements.txt
└── README.md

---

### 🛠️ Tech Stack

* Python, Pandas, NumPy, scikit-learn
* NASA POWER API, ipinfo.io (for geolocation)
* PyTorch (planned for LSTM)
* Streamlit (frontend - WIP)
* GitHub, VS Code

---

### 💡 Future Features

* Real-time solar forecast from any global location
* Dollar savings calculator based on $/kWh
* PDF or CSV energy reports
* Live weather + satellite image integration

---

### 🙋‍♀️ Built by

**Khushi Jain** — Computer Science grad & climate tech enthusiast ☀️

---
