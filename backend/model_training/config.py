# config.py

# Model architecture
INPUT_SIZE = 3
HIDDEN_SIZE = 64
NUM_LAYERS = 2

# Training
BATCH_SIZE = 32
EPOCHS = 50
LEARNING_RATE = 0.001

# Paths
MODEL_SAVE_PATH = "models/solar_lstm.pth"
X_VAL_PATH = "data/processed/x_val.npy"
Y_VAL_PATH = "data/processed/y_val.npy"
INFERENCE_PLOT_PATH = "assets/inference_plot.png"

# Early stopping
EARLY_STOPPING_PATIENCE = 7
