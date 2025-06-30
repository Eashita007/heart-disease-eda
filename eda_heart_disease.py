import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Ensure plots folder exists
os.makedirs("plots", exist_ok=True)

# Load dataset
df = pd.read_csv("Dataset/heart_disease_uci.csv")

# -----------------------------
# Step 1: Handle Missing Values (safe method)
# -----------------------------
fill_values = {
    'trestbps': df['trestbps'].median(),
    'chol': df['chol'].median(),
    'thalch': df['thalch'].median(),
    'oldpeak': df['oldpeak'].median(),
    'fbs': df['fbs'].mode()[0],
    'restecg': df['restecg'].mode()[0],
    'exang': df['exang'].mode()[0],
    'slope': 'unknown',
    'thal': 'unknown'
}
df.fillna(fill_values, inplace=True)

# Drop 'ca' column due to excessive missing values
if 'ca' in df.columns:
    df.drop(columns=['ca'], inplace=True)

# -----------------------------
# Step 2: Basic Info
# -----------------------------
print("Dataset Info:")
print(df.info())

print("\nBasic Statistics:")
print(df.describe())

print("\nMissing Values:")
print(df.isnull().sum())

# -----------------------------
# Step 3: Categorical Counts
# -----------------------------
print("\nSex Distribution:")
print(df['sex'].value_counts())

print("\nChest Pain Type Distribution:")
print(df['cp'].value_counts())

# -----------------------------
# Step 4: Histograms
# -----------------------------
sns.histplot(df['age'], bins=20, kde=True)
plt.title("Age Distribution")
plt.xlabel("age")
plt.ylabel("Count")
plt.savefig("plots/age_distribution.png")
plt.clf()

sns.histplot(df['chol'], bins=20, kde=True)
plt.title("Cholesterol Distribution")
plt.xlabel("chol")
plt.ylabel("Count")
plt.savefig("plots/chol_distribution.png")
plt.clf()

# -----------------------------
# Step 5: Correlation Heatmap
# -----------------------------
numeric_df = df.select_dtypes(include=['float64', 'int64'])
plt.figure(figsize=(12, 8))
sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm")
plt.title("Feature Correlation Heatmap (Numerical Only)")
plt.savefig("plots/heatmap.png")
plt.clf()
