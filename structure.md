```
SolarIQ/
├── backend/
│   └── model_training/        ← Model scripts + training notebooks
├── frontend/
│   └── streamlit_app.py       ← Streamlit UI file
├── data/
│   ├── raw/                   ← Raw data (uk_pv)
│   └── processed/             ← Cleaned CSVs
├── utils/
│   └── calc_savings.py        ← Reusable logic (savings, formatting)
├── assets/                    ← Logo, images, etc.
├── requirements.txt           ← Python packages list
├── README.md
└── .gitignore
```
---

```
Project Structure Update for LSTM Training
We will split the model training pipeline into modular files

New directory structure under backend/model_training/

backend/
├── model_training/
│   ├── load_data.py         → For loading x/y sequences and splitting into train/val
│   ├── dataset.py           → For defining PyTorch Dataset and DataLoaders
│   ├── model.py             → For defining the LSTM model architecture
│   ├── train.py             → For training logic, loss, optimizer, and validation
│   └── train_lstm_model.py  → Main entry file to call all above modules
```
---

ML Concepts Covered So Far
Sequence modeling using sliding window logic
Multivariate time series: using more than 1 feature (irradiance, temp, humidity)
Why we predict only irradiance: used for energy calculations later
Train-validation split: to evaluate model generalization
PyTorch Dataset/DataLoader: for efficient batching and shuffling

---