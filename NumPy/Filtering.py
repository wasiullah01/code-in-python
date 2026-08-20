import numpy as np

#generate a random array with in range 1-100 and total numbers 30
arr = np.random.randint(1,100,30)
print(arr)
#all greater than 70 from array
print(arr[arr > 70])
#numers between 40-60
print(arr[(arr >= 40) & (arr <= 60)])
#numbers from array less than 30
print(arr[arr < 30])
