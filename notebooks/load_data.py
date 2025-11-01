import pandas as pd

# Load raw dataset
df = pd.read_excel('data/raw/flood_risk_dataset_india.xlsx')

# Preview first few rows
print(df.head())

# Summary info
print(df.info())

# Check for missing values
print(df.isnull().sum())

# Example: drop rows with missing target label
df_clean = df.dropna(subset=['Flood Occurred'])

# Save processed data for modeling
df_clean.to_csv('data/processed/flood_risk_clean.csv', index=False)

