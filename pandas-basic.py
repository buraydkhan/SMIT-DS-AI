pip install pandas

# ==============================================================================
# PANDAS BASICS CRASH COURSE
# ==============================================================================

import pandas as pd
import numpy as np

# ------------------------------------------------------------------------------
# 1. CORE DATA STRUCTURES: SERIES & DATAFRAMES
# ------------------------------------------------------------------------------
print("=== 1. SERIES & DATAFRAMES ===")

# Series: 1D labeled array
series = pd.Series([10, 20, 30, 40], index=["a", "b", "c", "d"])
print("Pandas Series:\n", series)

# DataFrame: 2D labeled tabular data (Dictionary of lists pattern)
data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "Age": [25, 30, 35, 40, 22],
    "City": ["New York", "London", "Paris", "Tokyo", "London"],
    "Salary": [70000, 85000, 95000, np.nan, 62000] # np.nan represents missing data
}

df = pd.DataFrame(data)
print("\nDataFrame:\n", df)
print("-" * 50)


# ------------------------------------------------------------------------------
# 2. INSPECTING THE DATA
# ------------------------------------------------------------------------------
print("\n=== 2. INSPECTING DATA ===")

print("First 2 rows (head):\n", df.head(2))
print("\nSummary Info (dtypes, missing values):")
df.info()

print("\nStatistical Summary:\n", df.describe())
print("\nShape (rows, columns):", df.shape)
print("Column Names:", list(df.columns))
print("-" * 50)


# ------------------------------------------------------------------------------
# 3. SELECTION & INDEXING (loc vs iloc)
# ------------------------------------------------------------------------------
print("\n=== 3. SELECTION & INDEXING ===")

# Selecting a single column (returns a Series)
print("Single Column ('Name'):\n", df["Name"])

# Selecting multiple columns (returns a DataFrame)
print("\nMultiple Columns:\n", df[["Name", "Salary"]])

# .loc[] -> Selection by LABELS (row index label, column name)
print("\n.loc[0, 'Name'] ->", df.loc[0, "Name"])
print(".loc[1:3, ['Name', 'Age']]:\n", df.loc[1:3, ["Name", "Age"]])

# .iloc[] -> Selection by POSITION / INTEGER INDEX (0-based)
print("\n.iloc[0, 0] ->", df.iloc[0, 0])
print(".iloc[0:2, 0:2] (Exclusive end index):\n", df.iloc[0:2, 0:2])
print("-" * 50)


# ------------------------------------------------------------------------------
# 4. CONDITIONAL FILTERING
# ------------------------------------------------------------------------------
print("\n=== 4. CONDITIONAL FILTERING ===")

# Filter rows where Age > 28
over_28 = df[df["Age"] > 28]
print("Age > 28:\n", over_28)

# Multiple conditions: Use & (AND), | (OR) with parenthesis!
london_high_salary = df[(df["City"] == "London") & (df["Age"] < 30)]
print("\nCity == 'London' AND Age < 30:\n", london_high_salary)

# Using .isin() to match a list of values
selected_cities = df[df["City"].isin(["New York", "Tokyo"])]
print("\nCity is New York or Tokyo:\n", selected_cities)
print("-" * 50)


# ------------------------------------------------------------------------------
# 5. MODIFYING & CREATING COLUMNS
# ------------------------------------------------------------------------------
print("\n=== 5. MODIFYING COLUMNS ===")

# Create a copy so we don't alter the base frame unexpectedly
df_mod = df.copy()

# Adding a calculated column
df_mod["Bonus"] = df_mod["Salary"] * 0.10

# Modifying column values using conditional logic / scalar values
df_mod["Is_Senior"] = df_mod["Age"] >= 35

# Renaming columns
df_mod = df_mod.rename(columns={"Salary": "Base_Salary"})

# Dropping a column (axis=1 refers to columns)
df_mod = df_mod.drop(columns=["Bonus"])

print(df_mod)
print("-" * 50)


# ------------------------------------------------------------------------------
# 6. HANDLING MISSING DATA (NaN)
# ------------------------------------------------------------------------------
print("\n=== 6. HANDLING MISSING DATA ===")

df_clean = df.copy()

print("Check for NaN values:\n", df_clean.isna())
print("\nTotal missing values per column:\n", df_clean.isna().sum())

# Option 1: Fill missing values with fillna()
salary_median = df_clean["Salary"].median()
df_clean["Salary"] = df_clean["Salary"].fillna(salary_median)
print(f"\nDataFrame after filling NaN with median ({salary_median}):\n", df_clean)

# Option 2: Drop rows with missing values -> df_clean.dropna()
print("-" * 50)


# ------------------------------------------------------------------------------
# 7. GROUPING & AGGREGATION (groupby)
# ------------------------------------------------------------------------------
print("\n=== 7. GROUPBY & AGGREGATIONS ===")

# Group by City and calculate mean of numeric columns
city_group = df_clean.groupby("City")[["Age", "Salary"]].mean()
print("Average Age and Salary by City:\n", city_group)

# Aggregating multiple metrics at once
city_stats = df_clean.groupby("City").agg(
    Employee_Count=("Name", "count"),
    Avg_Salary=("Salary", "mean"),
    Max_Age=("Age", "max")
)
print("\nDetailed City Aggregations:\n", city_stats)
print("-" * 50)


# ------------------------------------------------------------------------------
# 8. SORTING & MERGING (JOINING)
# ------------------------------------------------------------------------------
print("\n=== 8. SORTING & MERGING ===")

# Sorting
sorted_df = df_clean.sort_values(by="Salary", ascending=False)
print("Sorted by Salary (Descending):\n", sorted_df)

# Merging DataFrames (Inner Join example)
dept_data = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Department": ["HR", "Engineering", "Engineering", "Finance"]
})

merged_df = pd.merge(df_clean, dept_data, on="Name", how="inner")
print("\nMerged DataFrame (JOIN on 'Name'):\n", merged_df)

print("-" * 50)
print("\n=== ALL PANDAS CODE EXECUTED SUCCESSFULLY! ===")
