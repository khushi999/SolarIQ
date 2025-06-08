import torch
from torch import nn, optim
import numpy as np
import os
from model import SolarLSTM
from dataset import get_dataloaders
from load_data import load_sequences
from config import (
    HIDDEN_SIZE, NUM_LAYERS, BATCH_SIZE, LEARNING_RATE, EPOCHS,
    MODEL_SAVE_PATH, X_VAL_PATH, Y_VAL_PATH, EARLY_STOPPING_PATIENCE
)
from utils import logger

def train_model():
    # Load data
    x_train, y_train, x_val, y_val = load_sequences()
    train_loader, val_loader = get_dataloaders(x_train, y_train, x_val, y_val, batch_size=BATCH_SIZE)

    # Setup
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = SolarLSTM(input_size=3, hidden_size=HIDDEN_SIZE, num_layers=NUM_LAYERS).to(device)
    criterion = nn.MSELoss()
    optimizer = optim.Adam(model.parameters(), lr=LEARNING_RATE)

    best_val_loss = float('inf')
    patience_counter = 0

    for epoch in range(EPOCHS):
        model.train()
        train_loss = 0.0

        for batch_x, batch_y in train_loader:
            batch_x, batch_y = batch_x.to(device), batch_y.to(device)

            optimizer.zero_grad()
            outputs = model(batch_x).squeeze()
            loss = criterion(outputs, batch_y)
            loss.backward()
            optimizer.step()

            train_loss += loss.item()

        model.eval()
        val_loss = 0.0
        with torch.no_grad():
            for batch_x, batch_y in val_loader:
                batch_x, batch_y = batch_x.to(device), batch_y.to(device)
                outputs = model(batch_x).squeeze()
                loss = criterion(outputs, batch_y)
                val_loss += loss.item()

        avg_train_loss = train_loss / len(train_loader)
        avg_val_loss = val_loss / len(val_loader)

        logger.info(f"Epoch {epoch+1}/{EPOCHS} - Train Loss: {avg_train_loss:.4f}, Val Loss: {avg_val_loss:.4f}")

        # Early stopping
        if avg_val_loss < best_val_loss:
            best_val_loss = avg_val_loss
            patience_counter = 0
            os.makedirs(os.path.dirname(MODEL_SAVE_PATH), exist_ok=True)
            torch.save(model.state_dict(), MODEL_SAVE_PATH)
            np.save(X_VAL_PATH, x_val)
            np.save(Y_VAL_PATH, y_val)
        else:
            patience_counter += 1
            logger.info(f"No improvement. Patience: {patience_counter}/{EARLY_STOPPING_PATIENCE}")

        if patience_counter >= EARLY_STOPPING_PATIENCE:
            logger.info("Early stopping triggered.")
            break

if __name__ == "__main__":
    train_model()
    
    