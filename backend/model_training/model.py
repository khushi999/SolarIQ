import torch
import torch.nn as nn

class SolarLSTM(nn.Module):
    def __init__(self, input_size=3, hidden_size=64, num_layers=1):
        super(SolarLSTM, self).__init__()
        
        self.hidden_size = hidden_size
        self.num_layers = num_layers

        # LSTM layer
        self.lstm = nn.LSTM(
            input_size=input_size,   # 3 features (irradiance, temp, humidity)
            hidden_size=hidden_size, # LSTM units
            num_layers=num_layers,
            batch_first=True         # Input shape: (batch, seq_len, features)
        )

        # Fully connected layer for final prediction
        self.fc = nn.Linear(hidden_size, 1)  # Output: 1 value (next-day irradiance)

    def forward(self, x):
        # x: (batch_size, sequence_length, input_size)
        lstm_out, _ = self.lstm(x)  # lstm_out: (batch_size, sequence_length, hidden_size)

        # Take the last time step’s output for each sequence
        last_out = lstm_out[:, -1, :]  # (batch_size, hidden_size)

        prediction = self.fc(last_out)  # (batch_size, 1)
        return prediction.squeeze(1)    # Flatten to shape: (batch_size,)
