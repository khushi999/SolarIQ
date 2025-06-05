import pandas as pd
import numpy as np

# Load the cleaned data
df = pd.read_csv('data/processed/clean_nasa.csv')

SEQUENCE_LENGTH = 7  # (7 days to predict next)

# Extract the irradiance column (as a NumPy array)
irradiance_values = df['solar_irradiance_scaled'].values

# Create empty lists for input sequences and targets
x, y = [], []

# Loop through the irradiance values to create sequences
for i in range(len(irradiance_values) - SEQUENCE_LENGTH):
    x_seq = irradiance_values[i:i+SEQUENCE_LENGTH]
    y_target = irradiance_values[i + SEQUENCE_LENGTH]
    x.append(x_seq)
    y.append(y_target)

# Convert x and y to NumPy arrays
x_np = np.array(x)
y_np = np.array(y)

# Print shape of x and y
print("X shape:", x_np.shape)  # (samples, SEQUENCE_LENGTH)
print("y shape:", y_np.shape)

# Save x and y as .npy files in data/processed/
np.save('data/processed/x_sequences.npy', x_np)
np.save('data/processed/y_targets.npy', y_np)

print("Saved sequences to data/processed/")
