from datasets import load_dataset
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
dataset = load_dataset("openclimatefix/uk_pv", split="train")
df = pd.DataFrame(dataset)

# Parse datetime and sort
df['datetime'] = pd.to_datetime(df['datetime'])
df = df.sort_values('datetime')

# Plot the raw solar generation
plt.figure(figsize=(12, 5))
plt.plot(df['datetime'], df['solar_generation_kw'])
plt.title('UK Solar Generation Over Time')
plt.xlabel('Date')
plt.ylabel('Solar Generation (kW)')
plt.grid(True)
plt.tight_layout()
plt.show()

# Save raw dataset
df.to_csv("data/raw/uk_pv.csv", index=False)
