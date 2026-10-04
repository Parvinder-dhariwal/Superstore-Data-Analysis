import pandas as pd

# Load the cleaned Superstore dataset
df = pd.read_excel("Data/Superstore_Clean.xlsx")

# -----------------------------
# 1. Dataset shape
# -----------------------------
print("\n--- DATASET SHAPE ---")
print(df.shape)

# -----------------------------
# 2. Column names
# -----------------------------
print("\n--- COLUMNS ---")
print(df.columns.tolist())

# -----------------------------
# 3. First 5 rows
# -----------------------------
print("\n--- FIRST 5 ROWS ---")
print(df.head())

# -----------------------------
# 4. Data types
# -----------------------------
print("\n--- DATA TYPES ---")
print(df.dtypes)

# -----------------------------
# 5. Missing values
# -----------------------------
print("\n--- MISSING VALUES ---")
print(df.isnull().sum())

# -----------------------------
# 6. Duplicate rows
# -----------------------------
print("\n--- DUPLICATE ROWS ---")
print(df.duplicated().sum())

# -----------------------------
# 7. Basic statistics
# -----------------------------
print("\n--- NUMERICAL SUMMARY ---")
print(df.describe())