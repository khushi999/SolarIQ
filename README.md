---
title: "SolarIQ"
emoji: "☀️"
colorFrom: "yellow"
colorTo: "orange"
sdk: streamlit
sdk_version: "1.32.0"
app_file: app.py
pinned: false
---

### 🌞 SolarIQ — ML-Powered Solar Forecasting App

🌐 [Live Demo](https://solar-iq.streamlit.app/)



> Forecast daily solar energy generation for your location using weather data from NASA and machine learning.

---

### About the Project

**SolarIQ** is a climate tech product that uses global weather data and time series modeling to:

* Predict next-day solar power output
* Estimate cost savings based on system size and electricity rates *(coming soon)*
* Provide an easy-to-use interface for homeowners, solar agents, students, and researchers

Originally based on Open Climate Fix's UK dataset, the project **pivoted to NASA POWER API** to allow **location-based, real-time forecasts** globally.

---

### How It Works

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

### Sample Output

A snapshot of normalized solar irradiance from NASA POWER API for the past year:

![Solar Irradiance Plot](assets/solar_irradiance_plot.png)

---

### Sequence Generation (Sliding Window)
To prepare data for the LSTM model, SolarIQ uses a sliding window approach:

We take sequences of 7 days of past solar irradiance to predict the irradiance of the next (8th) day.
```
Example:
Input (X):  [Day 1, Day 2, ..., Day 7]
Target (y): Day 8
This method allows the model to learn from historical trends and patterns.
```
![Sequence Diagram](assets/sequence_diagram.png)
Generated 358 such sequences from the cleaned NASA POWER dataset.

---

## Modeling
   - Trains a multi-feature LSTM model using PyTorch
   - Uses past 7 days of solar irradiance, temperature, and humidity
   - Predicts the 8th day's irradiance

---

## Model Performance Visualization

The following graph shows the **predicted vs actual normalized solar irradiance** on the validation dataset:

![Predicted vs Actual Irradiance](assets/inference_plot.png)

This plot illustrates how well the trained LSTM model is able to capture patterns in solar irradiance based on features such as temperature, humidity, and past irradiance values.

---

### RMSE (Root Mean Squared Error)

- **Validation RMSE**: `0.1252`
- **Validation MAE**: `0.0996`
<!-- - **Predictions Exported To**: [`assets/predictions.csv`](assets/predictions.csv) -->

The RMSE score measures the average prediction error between actual and predicted irradiance values. A lower RMSE indicates better performance — and 0.1252 suggests our model is fairly accurate on unseen data.

---

### Project Structure

```
SolarIQ/
├── backend/
│   ├── data/
│   │   ├── fetch_nasa_power.py
│   │   └── location_utils.py
│   └── model_training/
│       ├── clean_nasa_data.py
│       └── create_sequences.py
│       └── dataset.py
│       └── load_data.py
│       └── model.py
│       └── train_loop.py
│       └── utils.py
│       └── config.py
├── data/
│   ├── raw/              # Unprocessed NASA data
│   └── processed/        # Cleaned & scaled CSVs
├── frontend/
│   └── streamlit_app.py  # UI for user interaction
├── assets/
│   └── solar_irradiance_plot.png
│   └── inference_plot.png
│   └── predictions.csv
├── requirements.txt
├── LICENSE
└── README.md
```

---

### Tech Stack

* Python, Pandas, NumPy, scikit-learn
* NASA POWER API, ipinfo.io (for geolocation)
* PyTorch (LSTM model)
* Streamlit (frontend)
* GitHub, VS Code

---
<!-- 
### Future Features

* Real-time solar forecast from any global location
* Dollar savings calculator based on $/kWh
* PDF or CSV energy reports
* Live weather + satellite image integration

--- -->

### Built by

**Khushi Jain** — Climate tech enthusiast

---
