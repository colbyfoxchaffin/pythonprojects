import numpy as np
import pandas as pd
from numpy.random import randn

np.random.seed(101)

df = pd.DataFrame(randn(5,4),['A','B','C','D','E'],['W','X','Y','Z'])
print(df)

#A data frame is a bunch of series that share an index

print(df['W'])
print(type(df['W']))

#Grab a column from a dataframe
print(df['W'])

#Multiple Columns
print(df[['W','Z']])

#Creating a new column
df['new'] = df['W'] + df['Y']
print(df)

#df.drop('new') -> value error, labels new not contained in axis, refers to the index

df.drop('new',axis=1,inplace=True) #axis now refers to columns

print(df)

#Can also us .drop() to drop rows
print(df.drop('E'))

#Rows = 0, Columns = 1

print(df.shape) #returns tuple

#Selecting rows
print(df[['Z','X']])
