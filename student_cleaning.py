
import pandas as pd

df = pd.read_csv("student-mat.csv", sep=";")

print(df.head())

# Check the number of rows and columns
print("Dataset shape:", df.shape)

# Check missing values in each column
print("\nMissing values:")
print(df.isnull().sum())

# Check duplicate rows
print("\nDuplicate rows:", df.duplicated().sum())

# Check data types of all columns
print("\nData types:")
print(df.dtypes)

# Check basic statistical information
print("\nStatistical Summary:")
print(df.describe())

# Check unique values in important columns
print("\nStudent ages:")
print(sorted(df["age"].unique()))

print("\nFinal grades (G3):")
print(sorted(df["G3"].unique()))

# Clean column names
df.columns = df.columns.str.strip()

# Remove completely empty rows
df.dropna(how="all", inplace=True)

# Check the cleaned dataset
print("\nDataset after cleaning:")
print("Rows and columns:", df.shape)
print("Missing values after cleaning:")
print(df.isnull().sum().sum())

# Save the cleaned dataset
df.to_csv("student-mat-cleaned.csv", index=False)

print("\nCleaned dataset saved successfully!")

# Final cleaning report
print("\n===== DATA CLEANING REPORT =====")
print("Original dataset loaded successfully")
print("Duplicate rows found: 0")
print("Completely empty rows removed")
print("Column names cleaned")
print("Cleaned dataset saved as student-mat-cleaned.csv")
print("Final dataset shape:", df.shape)
print("================================")

# Validate the cleaned dataset
cleaned_df = pd.read_csv("student-mat-cleaned.csv")

print("\n===== DATASET VALIDATION =====")
print("Cleaned dataset shape:", cleaned_df.shape)
print("Missing values:", cleaned_df.isnull().sum().sum())
print("Duplicate rows:", cleaned_df.duplicated().sum())
print("Column names:", list(cleaned_df.columns))
