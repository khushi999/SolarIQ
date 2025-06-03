import numpy as np
import pandas as pd
import joblib

# load the cleaned dataset
df = pd.read_csv("data/processed/clean_scaled.csv")

# set the window size, i.e, 30 days
WINDOW_SIZE = 30

# convert to numpy array
values = df["generation_scaled"].values

x, y = [], []

for i in range(len(values) - WINDOW_SIZE):
    x.append(values[i:i + WINDOW_SIZE])
    y.append(values[i + WINDOW_SIZE])
    
x = np.array(x)
y = np.array(y)

print(f"Shape of X: {x.shape}")  # (num_samples, window_size)
print(f"Shape of y: {y.shape}")  # (num_samples,)

# Save to disk for training later
np.save("data/processed/X.npy", x)
np.save("data/processed/y.npy", y)