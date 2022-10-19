import numpy as np

arr = np.arange(0,11)
print(arr)

print(arr[8])

print(arr[1:5])
print(arr[0:5])

print(arr[:6])

print(arr[5:])

arr[0:5] = 100
print(arr)

arr = np.arange(0,11)

print(arr)

slice_of_arr = arr[0:6]
print(slice_of_arr)

#Data is not copied, just shows a view of the original array
slice_of_arr[:] = 99
print(slice_of_arr)
print(arr)

arr_copy = arr.copy()
arr_copy[:] = 100
print(arr_copy)

#Indexing on a matrix / 2-d array
arr_2d = np.array([[5,10,15],[20,25,30],[35,40,45]])

#double bracket format for indexing a matrix
print(arr_2d[0][0]) #print "5" first row, first column
print(arr_2d[0]) #print entire first row
print(arr_2d[1][1]) #print '25' second row, second column

#Get sub-matrices

print(arr_2d[:2,1:]) # print 'top right' corner (4 values)

#Conditional Selection
arr = np.arange(1,11)
print(arr)

bool_arr = arr > 5

print(bool_arr)

print(arr[bool_arr])

#All elements of the array that are less than 3
print(arr[arr<3])

arr_2d = np.arange(50).reshape(5,10)
print(arr_2d)