#create a diagnoal matrix and multiply it with 4X2 matrix

import numpy as np
a = np.array([1,2,4,3])
print("Matrix a is \n{0}\n". format(a))
d = np.diagflat(a)
print("Diagonal Matrix  is \n{0}\n".format(d))

b = np.array([[1,2],[2,3],[4,2],[5,1]])

print("Matrix b is {0}".format(b))
mul=d.dot(b)
print("Multiplication of matrices is\n{0}\n".format(mul))


'''
Output

Matrix a is 
[1 2 4 3]

Diagonal Matrix  is 
[[1 0 0 0]
 [0 2 0 0]
 [0 0 4 0]
 [0 0 0 3]]

Matrix b is [[1 2]
 [2 3]
 [4 2]
 [5 1]]
Multiplication of matrices is
[[ 1  2]
 [ 4  6]
 [16  8]
 [15  3]]
'''