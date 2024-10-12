import numpy as np

# arr["индекс масива"]["индекс строки"]["индекс столбца"]

a,b,c = 2,3,4
print(np.arange(10))
print(np.arange(a*b).reshape(a,b))
print(np.arange(a*b*c).reshape(a,b,c)) # a - сколько матриц | b,c - размер матрици 

arr = np.array([[1,2,3],
                [4,5,6],
                [6,7,8]])
print(arr)

