import torch
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error
from model import SolarLSTM

# Load x_val and y_val arrays from npy files

x_val = np.load('data/processed/x_val.npy')
y_val = np.load('data/processed/y_val.npy')

# Load the trained model
#    - Initialize model and load model weights from 'solar_lstm.pth'
model = SolarLSTM(input_size=3, hidden_size=64, num_layers=2)
model.load_state_dict(torch.load('model/solar_lstm.pth'))
model.eval()

# Convert x_val to torch tensor
x_val_tensor = torch.tensor(x_val, dtype=torch.float32)

# Disable gradient computation (torch.no_grad())
#    - forward pass through the model on x_val
#    - Output shape: predicted values of shape (num_samples,)
with torch.no_grad():
    predictions = model(x_val_tensor).squeeze().numpy()


# Compute RMSE between predictions and actual y_val
rmse = mean_squared_error(y_val, predictions, squared=False)
print(f"Validation RMSE: {rmse:.4f}")

# graph 
plt.figure(figsize=(12,5))
plt.plot(predictions, label='Predicted', linestyle='--')
plt.plot(y_val, label='Actual', alpha=0.7)
plt.title('Predicted vs Actual Solar Irradiance (Validation Set)')
plt.xlabel('Time Step')
plt.ylabel('Normalized Irradiance')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('assets/inference_plot.png')  # save plot for README
plt.show()