import numpy as np
import pandas as pd

#-----Group By--------
# Groupby allows you to group together rows based off of a column and perform an aggregate function on them.

data = {'Company':['GOOG', 'GOOG', 'MSFT', 'MSFT', 'FB', 'FB'], 'Person':['Sam','Charlie','Amy','Vanessa','Carl','Sarah'], 'Sales':[200,120,430,124,243,350]}

df = pd.DataFrame(data)

print(df)

byComp = df.groupby('Company')

print(byComp.mean())

print(byComp.sum())

print(byComp.std())

print(byComp.sum().loc['FB'])

print(df.groupby('Company').count())

print(df.groupby('Company').max())

#Use the groupby method with the describe method

print(byComp.describe())