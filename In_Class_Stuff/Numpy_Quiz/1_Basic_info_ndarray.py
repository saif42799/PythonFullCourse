
# basic information about numpy ndarrays (structure, properties, etc) as multiple choice questions

# ndarray, an efficient multidimensional array providing fast
# array-oriented arithmetic operations and flexible broadcasting capabilities.

# N-dimensional array object = ndarrays

# !- You have to import numpy as np to use additional methods
import numpy as np

# NumPy enables batch computations with similar syntax to scalar values on built-in Python objects

data = np.random.randn(2, 3)  # np basically make array data set
print(data)


print()
# You can write  mathematical operations with your data: ---------------------------------------------
data2 = np.random.randn(2, 3)
data2 * 10
print(data2)
print()

data3 = np.random.randn(2, 3)
data3 + data3
print(data3)
print()


# Every array has a "shape", a tuple indicating the size of each dimension

print("Data shape of data: " , data.shape)

# "dtype", an object describing the data type of the array
print("Data dtype of data: " , data.dtype)
print()



# !------- Creating ndarrays ---------------------------------------------

# this is a list
data4 = [6, 7.5, 8, 0, 1]
# This is now an array
arr1 = np.array(data4)
print("Created array: ", arr1)
print()


# !-- multidimensional array
#1D array
# list
data5 = [[1,2,3,4,5]]
#array
arr1 = np.array(data5)
print("1D array [x]: ", arr1)
print()


#2D array
# list
data6 = [[1,2,3,4,5],[6,7,8,9,10]]
#array
arr3 = np.array(data6)
print("2D array [x, y]: ", arr3)
print()

#3D array
# list
data7 = [  [[ 1,  2,  3],[ 4,  5,  6]],   [[ 7,  8,  9],[10, 11, 12]], [[13,14,15],[16,17,18]]  ]
#array
arr4 = np.array(data7)
print("3D array [x, y, z]: ", arr4)
print()

# Check what dimension are being used with "ndim"
print(arr4.ndim)
print(arr4.shape)
print()

# create arrays full of zeros using "zeros"
# 1D "zeros"
arr5 = np.zeros(10)
print("1D zeros: " , arr5)
print()

# 2D "empty" returns random garbage
arr6 = np.empty((2,3))
print("2D empty: " , arr6)
print()

# 3D "ones"
arr7 = np.ones((2,3,2))
print("3D ones: " , arr7)
print()

# full
arr99 = np.full((2, 2), 5)
print("Full: ", arr99)
print()

# you can arange an array
arr8 = np.arange(15)
print("Aranged array: ", arr8)
print()

# you can change the dtype of an array
arr9 = np.array([1, 2, 3])
arr9_to_float = arr9.astype(np.float64)
print(arr9_to_float.dtype)

arr10 = np.array([ 3.7, -1.2, -2.6,  0.5, 12.9, 10.1], dtype=np.int32)
print(arr10.dtype)
print("Float to int: ", arr10)
print()


# Arithmetic with NumPy Arrays --------------------------------------
arr11 = np.array([[1., 2., 3.], [4., 5., 6.]])

print("Array: ", arr11)
print()
print("Multiplied array: ", arr11 * arr11)
print()
print("Added array: ", arr11 + arr11)
print()
print("Subtracted array: ", arr11 - arr11)
print()

# does this each element in the array
arr12 = np.array([1,2,3,4,5,6,7])
print("Divided each element: ", 1/arr12)
print()
print("Multiplied each element: ", arr12 ** 0.5)

# check if array are equal with booleans
arr13 = np.array([2,2,4,4,8,1])
arr14 = np.array([2,1,4,2,0,1])
print("Comparing two arrays: ", arr13 > arr14)
print()

# Basic Indexing and Slicing -----------------------
# 1D array 0-9
arr15 = np.arange(10)
print("Fifth element: ", arr15[5])
print(arr15[5:8])
# assign certain element to different number
arr15[5:8] = 12
print(arr15)

arr15[1] = 99
print(arr15)

arr15[:] = 88
print(arr15)
print()

# indexing from 2D array
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr2d[2])
print(arr2d[0][1])
print(arr2d[0,1])
print()

# indexing from 3D array
arr3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr3d[1])
print(arr3d[0][1])
print(arr3d[1][0][2])
print()

# this has the old values if you want it back
old_values = arr3d[0].copy()
arr3d[0] = 42
print(arr3d)
print()

# Indexing with slices
print(arr2d[:2])
print()
print(arr2d[:2, 1:])
print()
print(arr2d[1, :2])
print()


names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
data0 = np.random.randn(7, 4)

print(names == 'Bob')
print()
print(data0[names == 'Bob'])
print()
print(data0[names == 'Bob', 2:])
print()
print(data0[names == 'Bob', 3])
print()
print(data0[~(names == 'Bob')])
print()
mask = (names == 'Bob') | (names == 'Will')
print(mask)
print()
data0[data0 < 0] = 0
print(data0)
print()
data0[names != 'Joe'] = 7
print(data0)