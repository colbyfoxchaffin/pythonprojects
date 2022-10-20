#Handling Missing Data with Pandas

import numpy as np
import pandas as pd

d = {'A':[1,2,np.nan],'B':[5, np.nan, np.nan],'C':[1,2,3]}

df = pd.DataFrame(d)
print(df)

print(df.dropna()) # Drops all rows with at least one NaN

print(df.dropna(axis = 1)) #Drops all columns with at least one NaN

#Using 'thresh' value to set a threshold for the number of non-NaNs to be true
print(df.dropna(thresh = 2))

#Fill in missing values
print(df.fillna(value = 'FILL VALUE'))

print(df['A'].fillna(value = df['A'].mean()))