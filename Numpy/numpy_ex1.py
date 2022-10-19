#Numpy Arrays

#Numpy arrays come as 1-d "vectors" or 2-d "matracices"

import numpy as np

my_list = [1,2,3]

arr = np.array(my_list)
print(arr)

my_mat = [[1,2,3],[4,5,6],[7,8,9]]
print(np.array(my_mat))

arr = np.arange(0,10)
print(arr)

arr = np.zeros(3)
print(arr)

arr = np.zeros((5,5))
print(arr)

#lin space

arr = np.linspace(0,5,10)
print(arr)

#identity matrix

arr = np.eye(4)
print(arr)

rand_arr = np.random.rand(5)
print(rand_arr)

rand_arr = np.random.rand(5,5)
print(rand_arr)

#sample from std normal or gaussian dist
rand_arr = np.random.randn(2)
print(rand_arr)

#random integer
rand_int = np.random.randint(1,100,10)
print(rand_int)

arr = np.arange(25)

ranarr = np.random.randint(0,50,10)

#Reshape method
print(arr.reshape(5,5))

#finding max or min values and their index locations

print(ranarr.max())
print(ranarr.min())
print(ranarr)
print(ranarr.argmax())
print(arr.shape)

arr = arr.reshape(5,5)
print(arr.shape)

print(arr.dtype)