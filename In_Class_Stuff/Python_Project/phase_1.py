import pandas as pd

# Project - Stage 1

df1 = pd.read_csv("characters.csv", sep='\t')
print(df1)
print('*-------*')
print(df1.dtypes)
print('*-------*')
print(df1.head())
print('*-------*')
print(df1.describe())

print('---------------------------------------------------------------------------------------------------------------')

df2 = pd.read_csv("episodes.csv", sep='\t')
print(df2)
print('*-------*')
print(df2.dtypes)
print('*-------*')
print(df2.head())
print('*-------*')
print(df2.describe())

print('---------------------------------------------------------------------------------------------------------------')

df3 = pd.read_csv("locations.csv", sep='\t')
print(df3)
print('*-------*')
print(df3.dtypes)
print('*-------*')
print(df3.head())
print('*-------*')
print(df3.describe())
