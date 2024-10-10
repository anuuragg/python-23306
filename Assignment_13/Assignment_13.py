import pandas as pd

df_read = pd.read_csv('./sample_data.csv')

print("First few rows:")
print(df_read.head())

print("\nDataFrame info:")
df_read.info()

print("\nBasic statistics:")
print(df_read.describe())


 