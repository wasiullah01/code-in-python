import numpy as np 


arr = np.random.randint(1,12,12)
#convert it 3x4 matrix 
arr1 = arr.reshape(3,4)
print(arr1)
#show shape
print(np.shape(arr1))
#get first row
print(arr1[1])
#get first column
print(arr1[:,3])
