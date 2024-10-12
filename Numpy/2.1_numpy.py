import numpy as np

arr_1 = np.array([[1,2,3],
                  [4,5,6],
                  [7,8,9]])

arr_1.ndim # количество осей в масиве (x,y,z,i,j,k ...)
arr_1.size # количество элементов в масиве
arr_1.shape = arr_1.size , 1 # меняет оси в масиве
arr_1.dtype = np.int8

arr_2 = np.empty([2,2,2]) # создает масив с неопределенными значениями

arr = np.ones([2,2,1])    # создает масив с еденицами
arr = np.ones_like(arr_2) # меняет в масиве все значения на еденици

arr = np.zeros([2,2,1])
arr = np.zeros_like(arr_2) 

arr = np.full([2,3,2], 7)
arr = np.full_like(arr_2, 8)

arr = np.arange(7,18,0.5) # (a,b,c) - где a,b - диапазое | c - шаг

print(arr)
