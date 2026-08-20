import numpy as np

arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([10, 20, 30, 40, 50])

#add two arrays
arr3 = arr1 + arr2
print(arr3)

#multiply two arrays
arr4 = arr1 * arr2
print(arr4)
#find correlation
correlation = np.corrcoef(arr1, arr2)[0, 1]
print(correlation)
#concatenate 2 arrays
concatenated = np.concatenate((arr1, arr2))
print(concatenated)
