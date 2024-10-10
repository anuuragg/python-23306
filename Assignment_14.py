import pandas as pd

data = {
    'Name': ['Sophia', 'Liam', 'Noah', 'Emma', 'Mason', 'Olivia', 'Lucas', 'Ava', 'Elijah', 'Isabella'],
    'Age': [22, 28, 45, 34, 39, 24, 31, 29, 41, 27],
    'Salary': [45000, 67000, 98000, 72000, 86000, 52000, 75000, 61000, 90000, 58000],
    'Department': ['Marketing', 'Sales', 'Engineering', 'Marketing', 'Engineering', 'Sales', 'HR', 'Finance', 'HR', 'Finance']
}

df = pd.DataFrame(data)

print("First few rows of the DataFrame (head()):\n", df.head())

print("\nLast few rows of the DataFrame (tail()):\n", df.tail())

print("\nInformation about the DataFrame (info()):")
df.info()

print("\nBasic statistics of the DataFrame (describe()):\n", df.describe())

print("\nSummary statistics for non-numeric columns (describe(include='object')):\n", df.describe(include='object'))
