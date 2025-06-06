import torch
from torch import nn, optim
from model import SolarLSTM
from dataset import get_dataloaders
from load_data import load_sequences
import numpy as np

# loading processed data
x_train, y_train, x_val, y_val = load_sequences()

# get dataloaders
train_loader, val_loader = get_dataloaders(x_train, y_train, x_val, y_val, batch_size=32)

# set device (GPU/CPU)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# initialise model, loss, optimizer
model = SolarLSTM(input_size=3, hidden_size=64, num_layers=2).to(device)
criterion = nn.MSELoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

# training loop
num_epochs = 50
for epoch in range(num_epochs):
    model.train()
    train_loss = 0.0
    
    for batch_x, batch_y in train_loader:
        batch_x = batch_x.to(device)
        batch_y = batch_y.to(device)
        
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
            batch_x = batch_x.to(device)
            batch_y = batch_y.to(device)
            
            outputs = model(batch_x).squeeze()
            loss = criterion(outputs, batch_y)
            val_loss += loss.item()
    
    
    print(f"Epoch {epoch+1}/{num_epochs} - Train Loss: {train_loss/len(train_loader):.4f}, Val Loss: {val_loss/len(val_loader):.4f}")
    
    
# Save validation sets for use in inference.py
np.save('data/processed/x_val.npy', x_val)
np.save('data/processed/y_val.npy', y_val)

torch.save(model.state_dict(), 'models/solar_lstm.pth')

# What This Output Means:
# Each line printed shows the training loss and validation loss for one epoch (i.e., one pass through the full dataset). 
# Here's how to interpret the numbers:
# Training Loss is the error on the training data. It starts high (~0.19) and quickly drops and stabilizes around 0.066, 
# which is great — it means your model is learning the patterns in the training set.
# Validation Loss tells you how well the model generalizes to unseen data. It fluctuates a bit (between ~0.06 and ~0.18), which is okay for now.
# No overfitting signs yet, but fluctuations in validation loss suggest there's some variance, 
# and maybe room to optimize (e.g., tuning model size, using dropout, or early stopping).