import pandas as pd
import numpy as np

# Load the cleaned data
df = pd.read_csv('data/processed/clean_nasa.csv')

SEQUENCE_LENGTH = 7  # (7 days to predict next)

# Extract the irradiance column (as a NumPy array)
features = df[['solar_irradiance_scaled', 'temperature_scaled', 'humidity_scaled']].values

# Create empty lists for input sequences and targets
x, y = [], []

# Loop through the irradiance values to create sequences
for i in range(len(features) - SEQUENCE_LENGTH):    # This loop goes from i=0 to len(features)-7, so you don't go out of bounds. 
    
    x_seq = features[i:i+SEQUENCE_LENGTH]
    y_target = features[i + SEQUENCE_LENGTH][0]   # this is the target the model should learn to predict (8th value in the array)
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
