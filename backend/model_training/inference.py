import torch
import numpy as np
import logging
import argparse
import pandas as pd
from model import SolarLSTM
from utils import compute_rmse, compute_mae, plot_predictions
from config import (
    INPUT_SIZE,
    HIDDEN_SIZE,
    NUM_LAYERS,
    MODEL_SAVE_PATH,
    X_VAL_PATH,
    Y_VAL_PATH,
    INFERENCE_PLOT_PATH
)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def run_inference(export_csv=False, disable_plot=False):
    logging.info("Loading validation data...")
    x_val = np.load(X_VAL_PATH)
    y_val = np.load(Y_VAL_PATH)

    logging.info("Initializing model...")
    model = SolarLSTM(input_size=INPUT_SIZE, hidden_size=HIDDEN_SIZE, num_layers=NUM_LAYERS)
    model.load_state_dict(torch.load(MODEL_SAVE_PATH))
    model.eval()

    x_val_tensor = torch.tensor(x_val, dtype=torch.float32)

    logging.info("Running inference...")
    with torch.no_grad():
        predictions = model(x_val_tensor).squeeze().numpy()

    # Evaluation
    rmse = compute_rmse(y_val, predictions)
    mae = compute_mae(y_val, predictions)
    logging.info(f"Validation RMSE: {rmse:.4f}")
    logging.info(f"Validation MAE: {mae:.4f}")

    # Plotting
    if not disable_plot:
        plot_predictions(y_val, predictions, save_path=INFERENCE_PLOT_PATH)

    # Export predictions to CSV
    if export_csv:
        df = pd.DataFrame({
            'Actual': y_val,
            'Predicted': predictions
        })
        df.to_csv('assets/predictions.csv', index=False)
        logging.info("Predictions exported to assets/predictions.csv")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run inference on validation set.")
    parser.add_argument("--export_csv", action="store_true", help="Export predictions to CSV")
    parser.add_argument("--disable_plot", action="store_true", help="Disable plot display and saving")
    args = parser.parse_args()

    run_inference(export_csv=args.export_csv, disable_plot=args.disable_plot)
