import numpy as np

arr = np.arange(18).reshape(2,3,3)

arr.min()
arr.max()
arr.mean()
arr.sum()

np.abs(arr, axis=0)
print(np.max(arr, axis=(2,1)))
np.log(arr, axis=2) # натуральный логарифм каждого элемента в масиве
np.exp(arr) # экспонента e^x 

np.sin(arr)
np.cos(arr)
np.tan(arr)
np_cot = 1 / np.tan(arr)

np.arcsin(arr)
np.arccos(arr)
np.arctan(arr)
np_arccot = np.tan(1/arr)

np.median(arr) # медиана
np.var(arr) # дисперсия
np.std(arr) # стандартное отклонение 
