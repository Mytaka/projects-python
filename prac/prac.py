import numpy as np

matrix1 = np.arange(9).reshape(3,3)
matrix2 = np.arange(9).reshape(3,3)

res1 = matrix1 + matrix2
res2 = matrix1 @ matrix2
res3 = np.linalg.det(res2)
res4 = matrix1.T
# res5 = np.linalg.inv(matrix1)
print(res1, res2, res3, res4,  sep='\n')