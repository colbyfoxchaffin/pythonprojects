from multiprocessing.dummy import Array
import numpy as np

#Array with Array
#Array with Scalars
#Universal Array Functions

arr = np.arange(0,11)
print(arr)

print( arr + arr) #adding the array to itself
print(arr - arr) #subtracting the array from itself
print(arr * arr) #multiply the array by itself

#Scalar
print(arr*100) #multiply the array by 100
print(arr - 100) #subtract 100 from each value in the array

# arr/arr will throw RuntimeWarning due to 0/0. Every other num will return '1'

print(arr **2) #square the array


print(np.sqrt(arr)) #get square root of each value of the array
print(np.exp(arr)) #get the exponential 
print(np.max(arr)) #equivalent to arr.max()
print(np.sin(arr)) #return sin(val) of each val in the array
