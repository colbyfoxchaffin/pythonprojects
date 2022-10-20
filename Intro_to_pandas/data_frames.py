from hashlib import new
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

df.drop('new',axis=1,inplace=True) #axis now refers to columns instead of rows

print(df)

#Can also us .drop() to drop rows
print(df.drop('E'))

#Index of Rows = 0, Columns = 1

print(df.shape) #returns tuple (5,4)

#Selecting columns - Pass a list of column names and return a dataframe with just those columns
print(df[['Z','X']])

#Selecting Rows - 2 ways to do this
#1: .loc() for location, accepts a label
print(df.loc['A'])
#2:Based off of index position - accepts a numberical index position
print(df.iloc[2])

print(df.loc['B','Y']) # will return a single value

#returns a subset of the df given the columns and rows
print(df.loc[['A','B'],['W','Y']]) 

#-------------Conditional Selection & Multi-index parts----------

#Perform conditional selection using bracket notation
booldf = df > 0
print(booldf)

print(df[booldf])

print(df['W'] > 0)
print(df['W'])

#grab all rows where 'Z' is less than 0
print(df[df['Z']<0])

#Can call methods off of resulting df's
resultdf = df[df['W']>0]

#Following 2 print statements will return the same dataframe
print(resultdf['X'])
print(df[df['W']>0]['X'])

boolser = df['W']>0
print(boolser)

result = df[boolser]
print(result)

mycols = ['Y','X']
print(result[mycols])

#Using 2 or more conditions
#Must use '&' not 'and' operator.
#Must use '|' not 'or' operator.

res = df[(df['W']> 0) & (df['Y'] > 1)]
print(res)

#Reset the index back to the default
# makes index a column and resets a new index to be numerical
df.reset_index()
print(df.reset_index())

newind = 'CA NY WY OR CO'.split()
print(newind)

#Set newind as a column in the Dataframe
df['States'] = newind

print(df.set_index('States'))

#-------------Multi level index Dataframes --------------

outside = ['G1','G1','G1','G2','G2','G2']
inside = [1,2,3,1,2,3]
hier_index = list(zip(outside, inside))
hier_index = pd.MultiIndex.from_tuples(hier_index)

df = pd.DataFrame(randn(6,2),hier_index,['A','B'])
print(df)

#Call from the outside moving in regarding indices
print(df.loc['G1'].loc[1])
df.index.names = ['Groups', 'Nums']
print(df)

# Grab G2 #2 Column B
print(df.loc['G2'].loc[2]['B'])

#Return a cross section
print(df.xs('G1'))

#grab all values where Num = 1 in both G1 and G2
print(df.xs(1, level = 'Nums'))