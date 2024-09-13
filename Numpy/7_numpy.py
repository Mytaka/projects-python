import numpy as np

arr_1 = np.arange(4*3*2).reshape(4,3,2)
arr_2 = np.arange(1*3*1).reshape(3,1)

# arr_2 += 1 # можно проводить только с согласоаными масивами
# arr_3 = arr_1 + arr_2

# согласованые масывы - это масивы с одинаковым размером

arr = np.arange(8).reshape(4,2)
# arr.shape = 4,3,2

print(arr_1)
print(arr)

print(arr[:,np.newaxis] * arr_1) 