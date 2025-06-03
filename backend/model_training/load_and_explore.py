from datasets import load_dataset
import pandas as pd
import matplotlib.pyplot as plt

# Load first 1000 rows only (safe for RAM)
dataset = load_dataset("openclimatefix/uk_pv", split="train")
df = pd.DataFrame(dataset)

# Rename and convert datetime
df.rename(columns={"datetime_GMT": "datetime"}, inplace=True)
df["datetime"] = pd.to_datetime(df["datetime"])
df = df.sort_values("datetime")

# Plot energy generation (in Wh)
plt.figure(figsize=(12, 5))
plt.plot(df["datetime"], df["generation_Wh"])
plt.title("Solar Energy Generation (Wh) – Sample (First 1000 Rows)")
plt.xlabel("Time")
plt.ylabel("Energy (Wh)")
plt.grid(True)
plt.tight_layout()
plt.show()

# Save sample to CSV
df.to_csv("data/raw/uk_pv_full.csv", index=False)
