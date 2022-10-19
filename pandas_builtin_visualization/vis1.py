#Pandas Built In Data Vis
import matplotlib
import numpy as np
import pandas as pd

df1 = pd.read_csv('file_name',index_col=0)
df1.head() #show head of dataframe

#histogram of a column in df1
df1['A'].hist() #call matplotlib under the hood

#plots types

#histogram
df1['A'].plot(kind = 'hist')

df1['A'].plot.hist()

# Area plot
df1.plot.area() #area plot / set alpha for transparency

#Bar plot
df1.plot.bar() #takes index as a category, column values as bars
#can be a stacked bar plot, stacked values

