# In PyTorch, training data needs to be wrapped inside a Dataset and then passed to a DataLoader to make training easier, 
# especially when batching and shuffling are involved.
# SolarDataset → a custom wrapper around your (x, y) NumPy arrays.
# get_dataloaders → a helper function to create batch-ready train/validation sets.

import torch
from torch.utils.data import Dataset, DataLoader

class SolarDataset(Dataset):
    def __init__(self, x, y):
        self.x = torch.tensor(x, dtype=torch.float32)
        self.y = torch.tensor(y, dtype=torch.float32)
    
    def __len__(self):                              # tells how many samples in dataset
        return len(self.x)
    
    def __getitem__(self, idx):                     # returns a single (x, y) pair when given an index
        return self.x[idx], self.y[idx]


def get_dataloaders(x_train, y_train, x_val, y_val, batch_size=32):   #batch_size=32: means 32 sequences are fed to the model at once during training
    train_dataset = SolarDataset(x_train, y_train)
    val_dataset = SolarDataset(x_val, y_val)
    
    train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)   # - train_loader: shuffle=True for randomness
    val_loader = DataLoader(val_dataset, batch_size=batch_size, shuffle=False)         # - val_loader: shuffle=False to preserve sequence
    
    return train_loader, val_loader



# Makes training faster and more efficient (less memory usage)
# Adds shuffling for training (helps generalization)
# Keeps order in validation (we want reproducible evaluation)


