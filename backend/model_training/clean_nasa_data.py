import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler 

RAW_DATA_PATH = 'data/raw/nasa_power.csv'
df = pd.read_csv(RAW_DATA_PATH)

df['date'] = pd.to_datetime(df['date'].astype(str),format='%Y%m%d', errors='coerce')
# .astype(str) ensures values like 20230101 are parsed as text (not numbers).
# format="%Y%m%d" tells pandas exactly how to read the format (YYYYMMDD).
# errors='coerce' makes invalid dates become NaT instead of crashing.

print(df['date'].head(10))

print(df.columns)

df['temperature'] = pd.to_numeric(df['temperature'], errors='coerce')
df['humidity'] = pd.to_numeric(df['humidity'], errors='coerce')
df['solar_irradiance'] = pd.to_numeric(df['solar_irradiance'], errors='coerce')
# The errors='coerce' parameter in pandas is used to handle errors during data type conversions, 
# particularly within functions like pd.to_numeric and pd.to_datetime. When set, it replaces invalid or non-convertible values 
# with NaN (Not a Number) for numeric conversions or NaT (Not a Time) for datetime conversions, instead of raising an error.

df = df.dropna()

scaler = MinMaxScaler()
df[['temperature_scaled', 'humidity_scaled', 'solar_irradiance_scaled']] = scaler.fit_transform(df[['temperature','humidity', 'solar_irradiance']])

plt.figure(figsize=(12,5))
plt.plot(df['date'], df['solar_irradiance_scaled'])
plt.title('Solar Irradiance (Normalized) Over Time')
plt.xlabel('date')
plt.ylabel('solar_irradiance (0-1)')
plt.grid(True)
plt.tight_layout()
plt.show()


PROCESSED_DATA_PATH = 'data/processed/clean_nasa.csv'
df.to_csv(PROCESSED_DATA_PATH, index=False) 
# index = False is written so that the row index (0,1,2,3,4..) of the new columns are not added to the og df 

print(f'cleaned data saved to {PROCESSED_DATA_PATH}')
