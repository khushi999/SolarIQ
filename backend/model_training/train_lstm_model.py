# Project Structure Update for LSTM Training
# We will split the model training pipeline into modular files

# New directory structure under backend/model_training/
#
# backend/
# ├── model_training/
# │   ├── load_data.py         → For loading x/y sequences and splitting into train/val
# │   ├── dataset.py           → For defining PyTorch Dataset and DataLoaders
# │   ├── model.py             → For defining the LSTM model architecture
# │   ├── train.py             → For training logic, loss, optimizer, and validation
# │   └── train_lstm_model.py  → Main entry file to call all above modules


# from load_data import load_sequences
# from dataset import get_dataloaders

# # Step 1: Load sequences
# x_train, y_train, x_val, y_val = load_sequences()
# print("Train shape:", x_train.shape, y_train.shape)
# print("Val shape:", x_val.shape, y_val.shape)

# # Step 2: Get DataLoaders
# train_loader, val_loader = get_dataloaders(x_train, y_train, x_val, y_val)
# print("Loaded DataLoaders.")