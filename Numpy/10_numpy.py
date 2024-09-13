import numpy as np

np.random.seed(42)

vector_1 = np.array([1, 2, 3, 4, 5]) 
vector_2 = np.array([2, 3, 4, 5, 6]) 
matrix_1 = np.random.randint(10, size=[3, 3])
matrix_2 = np.random.randint(10, size=[3, 3])

np.dot(vector_1,vector_2)   # скалярный добуток
vector_1 @ vector_2         # скалярный добуток
np.inner(vector_1,vector_2) # скалярный добуток

np.outer(vector_1,vector_2) # внешнее произведение векторов. (первый элемент первого вектора * на все элементы второго)

print( np.dot(matrix_1, matrix_2) )    # умножение матриц
print( np.matmul(matrix_1, matrix_2) ) # умножение матриц
print( matrix_1 @ matrix_2 )           # умножение матриц

# -------------------------------------------------------------

vec_1 = np.array([1,2,3])
vec_2 = np.array([1,2,3,4])
mat = np.random.randint(10,size=[4,3])

print(np.dot(mat, vec_1)) # умножение матрици на вектор
print(mat @ vec_1) # вектор умножаеться на матрицу (ответ горизонтальный)

print(mat @ vec_1[:,np.newaxis]) # вектор умножаеться на матрицу (ответ вертикальный)

# -------------------------------------------------------------

mat = np.arange(16).reshape(4,4)

print(mat) 
print(np.linalg.matrix_rank(mat)) # ранг матрици
print(np.linalg.trace(mat)) # след матрици ( сума главной диагонали )
print(np.linalg.det(mat))   # находит определитель матрици, Δ  "визначник" 
print(np.linalg.eig(mat))   # возвращает 2 масива: первый с собственными значениями матрицами, а второй с собственными векторами
print(np.linalg.inv(mat))   # обратная матрица
print(np.linalg.svd(mat))   # сингулярное различие


