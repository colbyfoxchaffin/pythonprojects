#Pandas Series
import numpy as np
import pandas as pd

labels = ['a','b','c']
my_data = [10,20,30] #python list
arr = np.array(my_data) #numpy array
d = {'a':10,'b':20,'c':30} #python dictionary

print(labels)
print(my_data)
print(arr)
print(d)


#create series from 'my_data'

print(pd.Series(data = my_data, index = labels))
#Unlike Numpy Array we have labeled indices that we can call on

pd.Series(my_data,labels) #same things as above

pd.Series(arr,labels) #passing in numpy array/python list

print(pd.Series(d)) #passing in dictionary - keys become indices, values become corresponding values in columns

print(pd.Series(data = labels))

print(pd.Series(data = [sum, print, len]))

#Using the index

ser1 = pd.Series([1,2,3,4],['USA','Germany','USSR','Japan'])
print(ser1)

ser2 = pd.Series([1,2,5,4],['USA','Germany','Italy','Japan'])

print(ser2)

print(ser1['USA'])

ser3 = pd.Series(data=labels)
print(ser3[0])
