import numpy as np

# loading sequences from the data/processed... folder
x_sequences = np.load('data/processed/x_sequences.npy')
y_targets = np.load('data/processed/y_targets.npy')

# verifying the loaded data
print("x shape:", x_sequences.shape)
print("y shape:", y_targets.shape)

# splitting data into 80(training)/20(validation) sets
split_index =  int(0.8 * len(x_sequences))

# split data into training and validation sets
x_train = x_sequences[:split_index]
y_train = y_targets[:split_index]

x_val = x_sequences[split_index:]
y_val = y_targets[split_index:]

# confirming the splitting and verfying sizes
print("Training set size: ", x_train.shape, y_train.shape)
print("Validation set size: ", x_val.shape, y_val.shape)


# x = 358 total samples, 7 days per sample (sequence length), 3 features per day: solar_irradiance_scaled, temperature_scaled, humidity_scaled
# y = (358,), meaning each sequence is predicting a single scalar value: the next day's solar irradiance.