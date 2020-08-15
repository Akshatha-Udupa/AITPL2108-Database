#perform 2X3 matrix, 3X2 matrix arthimetic,substraction,multiplication

import numpy as np
a = np.array([[4, 5, 3], [4, 8, 6]])
print("Matrix A is \n{0}\n".format(a))
b= np.array([[3, 2], [4, 6], [3, 4]])
print("Matrix B is \n{0}\n".format(b))

#Since 2 matrices should have same dimension to add and subtract, transpose any one of the matrix
t = a.transpose()
print("Transpose of Matrix  A is \n{0}\n".format(t))

print("Addition of Matrices is\n{0}\n".format(t+b))

print("Subtraction of Matrices is\n{0}\n".format(t-b))

mul = a.dot(b)
print("Multiplication of matrices is\n{0}".format(mul))



'''
Output

Matrix A is 
[[4 5 3]
 [4 8 6]]

Matrix B is 
[[3 2]
 [4 6]
 [3 4]]

Transpose of Matrix  A is 
[[4 4]
 [5 8]
 [3 6]]

Addition of Matrices is
[[ 7  6]
 [ 9 14]
 [ 6 10]]

Subtraction of Matrices is
[[1 2]
 [1 2]
 [0 2]]

Multiplication of matrices is

[41 50]
[62 80]
'''