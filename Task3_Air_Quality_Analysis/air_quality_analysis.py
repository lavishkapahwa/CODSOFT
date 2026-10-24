
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# Project folder
output_folder = Path("charts")
output_folder.mkdir(exist_ok=True)

# Load the air quality dataset
file_path = next(Path(".").glob("*.csv"))

df = pd.read_csv(
    file_path,
    sep=";",
    decimal=",",
    na_values=["-200", ""]
)

# Remove empty columns and rows
df = df.dropna(axis=1, how="all")
df = df.dropna(axis=0, how="all")

print("AIR QUALITY DATA ANALYSIS")
print("=" * 40)
print("\nFirst 5 rows:")
print(df.head())

print("\nDataset shape:", df.shape)
print("\nColumn names:")
print(df.columns.tolist())

print("\nMissing values in each column:")
print(df.isnull().sum())

print("\nSummary statistics:")
print(df.describe())

# Save cleaned dataset
df.to_csv("air_quality_cleaned.csv", index=False)

# Select numeric columns
numeric_df = df.select_dtypes(include="number")

# Plot pollutant measurements over time
pollutants = [
    col for col in ["CO(GT)", "C6H6(GT)", "NOx(GT)", "NO2(GT)"]
    if col in df.columns
]

for col in pollutants:
    values = pd.to_numeric(df[col], errors="coerce")
    plt.figure(figsize=(10, 5))
    plt.plot(values, linewidth=1)
    plt.title(f"{col} Measurements Across Records")
    plt.xlabel("Record Number")
    plt.ylabel(col)
    plt.tight_layout()
    plt.savefig(output_folder / f"{col.replace('/', '_')}_trend.png")
    plt.close()

# Correlation heatmap
if len(numeric_df.columns) >= 2:
    plt.figure(figsize=(12, 8))
    sns.heatmap(
        numeric_df.corr(),
        cmap="coolwarm",
        center=0
    )
    plt.title("Air Quality Variables Correlation")
    plt.tight_layout()
    plt.savefig(output_folder / "correlation_heatmap.png")
    plt.close()

print("\nAnalysis completed!")
print("Cleaned dataset saved as air_quality_cleaned.csv")
print("Charts saved in the charts folder.")
