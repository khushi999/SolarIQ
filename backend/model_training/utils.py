import logging
import numpy as np
from sklearn.metrics import root_mean_squared_error
import matplotlib.pyplot as plt
import os

# ------------------- LOGGER SETUP -------------------
def get_logger(name='SolarIQ'):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        os.makedirs('logs', exist_ok=True)
        file_handler = logging.FileHandler('logs/solariq.log')
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger

logger = get_logger()
# -----------------------------------------------------

def compute_rmse(y_true, y_pred):
    """Compute Root Mean Squared Error (RMSE)"""
    return root_mean_squared_error(y_true, y_pred, squared=False)

def plot_predictions(y_true, y_pred, save_path='assets/inference_plot.png'):
    """Plot predicted vs actual irradiance and save the plot"""
    plt.figure(figsize=(12, 5))
    plt.plot(y_pred, label='Predicted', linestyle='--')
    plt.plot(y_true, label='Actual', alpha=0.7)
    plt.title('Predicted vs Actual Solar Irradiance (Validation Set)')
    plt.xlabel('Time Step')
    plt.ylabel('Normalized Irradiance')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    # Ensure save directory exists
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    plt.savefig(save_path)
    plt.show()
