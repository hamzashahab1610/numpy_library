import numpy as np

arr_a = np.array([1, 2, 3, 4, 5, 'hamza'])  #Converts all data to string (Homogenous data type numpy_array)
print(arr_a)
print(arr_a.shape)  #Gives the dimensions of array

arr_b = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr_b)
print(arr_b.shape)

# 3x3
seq_a = [1, 2, 3]
seq_b = [4, 5, 6]
seq_c = [7, 8, 9.8] #Converts whole array to float xD
arr_c = np.array([seq_a, seq_b, seq_c])
print(arr_c)
print(arr_c.shape)
print(arr_c.size)

#Reshaping
arr_reshape = arr_b.reshape(5, 2)
print(arr_b)
print(arr_reshape)

#Transpose
print(arr_c)
print(arr_c.T)

#Indexing
print(arr_c[:, 2])  #For all rows 3rd column

#Default array
arr1 = np.array([[1, 2, 3], [4, 5, 6]], dtype=float)
print(arr1)

#Zero Matrix
zero = np.zeros((3, 3))
print(zero)

one = np.ones((3, 3))
print(one)

x = np.full((3, 3), 'x')
print(x)

random_arr = np.random.random((3, 4))
print(random_arr)

#Advanced Indexing
r1 = [1, 2, 3, 4, 5]
r2 = [6, 7, 8, 9, 10]
r3 = [11, 12, 13, 14, 15]
arr_adv = np.array([r1, r2, r3])
#slice
print(arr_adv[:, 2:4:1])  # start : ending value : step size
#negative index
print(arr_adv[:, -2:-4:-1])

#Boolean
greater_than_five = arr_adv > 5
print(greater_than_five)
print(arr_adv[greater_than_five])

#where
drop_under_5_array = np.where(arr_adv > 5, arr_adv, 0)
print(drop_under_5_array)

#logical and
drop_under_5_and_10_array = np.logical_and(arr_adv > 5, arr_adv < 10)
print(drop_under_5_and_10_array)
print(arr_adv[drop_under_5_and_10_array])

#single array operations
array_a = np.array([[1, 2], [3, 4]])
array_b = np.array([[2, 2], [6, 6]])
print(array_a.sum(axis=0))
print(array_a.sum(axis=1))
print(array_a.cumsum())
print(array_a.cumprod())

#two array maths
print(array_a + array_b)
print(array_a - array_b)
print(array_a * array_b)
print(array_a / array_b)
print(np.dot(array_a, array_b))

#array_brodcasting
arr_1 = np.array([[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4]])
arr_2 = np.array([0, 1, 2, 3])
arr_3 = np.array([[1], [2], [3], [4]])
arr_4 = np.array([[0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3], [0,1,2,3]])
print(arr_1 + arr_2)
print(arr_1 + arr_4)
print(arr_1 + arr_3)

