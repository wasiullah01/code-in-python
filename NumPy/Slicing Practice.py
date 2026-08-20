import numpy as np


arr1 = np.array([5, 10, 15, 20, 25, 30, 35, 40, 45, 50])
#first three elements
print(arr1[:3])
#last three elements
print(arr1[-3:])
#get every 2nd elements
arr2 = arr1[arr1 % 2 == 0]
print(arr2)
#reversed the array
print(arr1[::-1])