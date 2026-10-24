
import pandas as pd

# Load the HR employee attrition dataset
df = pd.read_csv("WA_Fn-UseC_-HR-Employee-Attrition.csv")

# Display the first 5 rows
print("First 5 rows of the dataset:")
print(df.head())

# Display dataset information
print("\nDataset shape (rows, columns):")
print(df.shape)

print("\nColumn names:")
print(df.columns.tolist())

# Check missing values in each column
print("\nMissing values in each column:")
print(df.isnull().sum())

# Calculate total missing values
print("\nTotal missing values:")
print(df.isnull().sum().sum())

# Check duplicate rows
print("\nTotal duplicate rows:")
print(df.duplicated().sum())

# Check data types
print("\nColumn data types:")
print(df.dtypes)

# Employee attrition analysis
print("\nEmployee Attrition Count:")
print(df["Attrition"].value_counts())

# Attrition percentage
print("\nEmployee Attrition Percentage:")
print(df["Attrition"].value_counts(normalize=True).mul(100).round(2))

# Department-wise employee count
print("\nDepartment-wise Employee Count:")
print(df["Department"].value_counts())

# Average age of employees
print("\nAverage Employee Age:")
print(round(df["Age"].mean(), 2))

# Average monthly income
print("\nAverage Monthly Income:")
print(round(df["MonthlyIncome"].mean(), 2))

import matplotlib.pyplot as plt
import seaborn as sns

# Count employees by attrition status
attrition_counts = df["Attrition"].value_counts()

# Create bar chart
plt.figure(figsize=(7, 5))
sns.barplot(
    x=attrition_counts.index,
    y=attrition_counts.values
)

plt.title("Employee Attrition Analysis")
plt.xlabel("Attrition Status")
plt.ylabel("Number of Employees")

plt.tight_layout()
plt.savefig("employee_attrition_chart.png")
plt.show()

# Department-wise employee attrition
plt.figure(figsize=(9, 5))

sns.countplot(
    data=df,
    x="Department",
    hue="Attrition"
)

plt.title("Department-wise Employee Attrition")
plt.xlabel("Department")
plt.ylabel("Number of Employees")
plt.xticks(rotation=15)
plt.legend(title="Attrition")

plt.tight_layout()
plt.savefig("department_attrition_chart.png")
plt.show()

# Job satisfaction and employee attrition
plt.figure(figsize=(8, 5))

sns.countplot(
    data=df,
    x="JobSatisfaction",
    hue="Attrition"
)

plt.title("Job Satisfaction vs Employee Attrition")
plt.xlabel("Job Satisfaction Rating (1 = Low, 4 = High)")
plt.ylabel("Number of Employees")
plt.legend(title="Attrition")

plt.tight_layout()
plt.savefig("job_satisfaction_attrition.png")
plt.show()

# Calculate attrition percentage by job satisfaction
satisfaction_attrition = pd.crosstab(
    df["JobSatisfaction"],
    df["Attrition"],
    normalize="index"
) * 100

print("\nAttrition Percentage by Job Satisfaction:")
print(satisfaction_attrition.round(2))

# Calculate attrition percentage by department
department_attrition = pd.crosstab(
    df["Department"],
    df["Attrition"],
    normalize="index"
) * 100

print("\nAttrition Percentage by Department:")
print(department_attrition.round(2))






