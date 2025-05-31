import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
import os

# === Step 1: Load the raw sample dataset ===
RAW_DATA_PATH = "data/raw/uk_pv_sample.csv"
df = pd.read_csv(RAW_DATA_PATH)
df['datetime'] = pd.to_datetime(df['datetime'])

# === Step 2: Resample to daily energy totals ===
df_daily = df.set_index("datetime").resample("D").sum().reset_index()

# === Step 3: Filter out days with zero or negligible generation ===
df_daily = df_daily[df_daily['generation_Wh'] > 10]  # optional threshold

# === Step 4: Normalize generation_Wh for LSTM ===
scaler = MinMaxScaler()
df_daily['generation_scaled'] = scaler.fit_transform(df_daily[['generation_Wh']])

# Save scaler object if needed for later use (optional)
import joblib
joblib.dump(scaler, "data/processed/scaler.pkl")

# === Step 5: Plot cleaned & scaled generation ===
plt.figure(figsize=(12, 5))
plt.plot(df_daily['datetime'], df_daily['generation_scaled'])
plt.title("Normalized Daily Solar Generation")
plt.xlabel("Date")
plt.ylabel("Scaled Energy (0–1)")
plt.grid(True)
plt.tight_layout()
plt.show()

# === Step 6: Save cleaned data ===
PROCESSED_DATA_PATH = "data/processed/clean_scaled.csv"
df_daily.to_csv(PROCESSED_DATA_PATH, index=False)

print(f"\nCleaned and saved to: {PROCESSED_DATA_PATH}")

