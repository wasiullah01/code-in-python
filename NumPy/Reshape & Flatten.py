import numpy as np
#create array 1-20 in range 20
arr = np.random.randint(1,20,20)
#reshape to 4x5 matrix
arr1 = arr.reshape(4,5)
print(arr1)
#reshape to 2x10
arr2 = arr.reshape(2,10) 
print(arr2)
#now make it 1d array
arr3 = arr.ravel()
print(arr3)