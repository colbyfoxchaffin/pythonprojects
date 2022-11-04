import pandas as pd
import numpy as np
df = pd.DataFrame({'col1':[1,2,3,4],'col2':[444,555,666,444],'col3':['abc','def','ghi','xyz']})
df.head()

print(df['col2'].unique())

print(len(df['col2'].unique()))

print(df['col2'].nunique())

print(df['col2'].value_counts())

print(df[df['col1']>2])

print(df[(df['col1']>2) & (df['col2'] == 444)])


def times2(x):
    return x*2

print(df['col1'].apply(times2))

print(df['col3'].apply(len))

#Lambda for times2

print(df['col1'].apply(lambda x: x*2))

#Removing columns
print(df.drop('col1',axis=1))
print(df)
print(df.columns)

print(df.index)


#Soring and ordering a Dataframe

print(df.sort_values('col2'))


print(df.isnull()) #All Falses because there are no null values

#Pivot Tables

data = {'A':['foo','foo','foo','bar','bar','bar'],
     'B':['one','one','two','two','one','one'],
       'C':['x','y','x','y','x','y'],
       'D':[1,3,2,5,4,1]}
df = pd.DataFrame(data)

print(df)

print(df.pivot_table(values = 'D', index = ['A','B'], columns = ['C']))
