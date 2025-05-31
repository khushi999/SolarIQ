### 🌞 SolarIQ — ML-Powered Solar Forecasting App

> Forecast solar energy generation and estimate daily savings using machine learning.

---

### 📌 About the Project

SolarIQ is a climate tech product that uses real solar energy data and time series modeling to:

* Predict next-day solar power output
* Estimate cost savings based on system size and electricity rates
* Provide an easy-to-use interface for eco-conscious individuals, solar agents, or schools

---

### 🔍 How It Works

1. **Data**
   Uses real-world solar data from [Open Climate Fix’s UK PV dataset](https://huggingface.co/datasets/openclimatefix/uk_pv)

2. **Processing**

   * Cleans and resamples data to daily totals
   * Scales generation between 0 and 1
   * Creates 7-day input sequences for prediction

3. **Modeling**

   * Will use an LSTM-based time series model (coming soon!)

4. **UI**

   * Streamlit frontend (coming soon) where users input their system size and see forecast + savings

---

### 📁 Project Structure

```
SolarIQ/
├── backend/
│   └── model_training/
│       ├── load_and_explore.py
│       ├── clean_and_prepare.py
│       └── create_sequences.py
├── data/
│   ├── raw/
│   └── processed/
├── frontend/
│   └── streamlit_app.py (WIP)
├── requirements.txt
└── README.md
```

---

### 📅 Timeline

| Week   | Focus                                 |
| ------ | ------------------------------------- |
| Week 1 | Data setup, loading, and exploration  |
| Week 2 | Preprocessing and sequence generation |
| Week 3 | Model training + evaluation           |
| Week 4 | Streamlit UI                          |
| Week 5 | Testing + deployment                  |

---

### 🛠️ Tech Stack

* Python, Pandas, NumPy, scikit-learn, PyTorch
* Hugging Face Datasets
* Streamlit (for frontend)
* GitHub + VS Code

---

### 💡 Future Additions

* Weather data integration (NASA POWER / OpenWeatherMap)
* Real-time location-based solar predictions
* Energy savings calculator by $/kWh
* Report export (PDF/CSV)