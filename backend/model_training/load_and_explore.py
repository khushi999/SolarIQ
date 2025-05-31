from datasets import load_dataset
import pandas as pd
import matplotlib.pyplot as plt

# Load a safe small batch from the dataset
dataset = load_dataset("openclimatefix/uk_pv", split="train[:1000]")
df = pd.DataFrame(dataset)

# Print all columns to check structure
print("DataFrame columns:")
print(df.columns)
print("\nFirst few rows:")
print(df.head())
