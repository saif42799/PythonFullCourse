# Project - Stage 2
import pandas as pd

df1 = pd.read_csv("characters.csv", sep='\t')

df2 = pd.read_csv("episodes.csv", sep='\t')

df3 = pd.read_csv("locations.csv", sep='\t')

# Select a column to replace values, or add a new column to your dataset (see Ch 5 of PDA).
# For instance, you can create a new column by adding two other columns together.

# df3 = characters.csv
df3['Female or not'] = df3.gender == 'Female'
df3

# Run a filtering operation by using Dataframe row indexing using a
# comparison statement that yields a boolean array/matrix.

df3[df3.species == 'Alien']


# Change the index of your dataset using the set_index
# method to one of your columns and display the resulting table.

a = df1.set_index('name')
a


a.reset_index().set_index('dimension')


# Select a subset of rows from your dataset, and save it in a
# separate file as CSV or another format (see Ch 6)

b = df3[df3.species == 'Human']

b.to_csv('out.csv')
