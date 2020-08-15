#x=4X2 matrix, transpose it and perform all arthimetic operation

import numpy as np
a = np.array([[4, 5],[2,3],[4,3],[4, 8]])
print("Matrix A is \n{0}\n".format(a))

t = a.transpose()
print("Transpose of Matrix  A is \n{0}\n".format(t))

mul = a.dot(t)
print("Multiplication of matrices is\n{0}\n".format(mul))

# addition & subtraction of non sqaure matrices is not possible
print("Addition of Matrices is\n{0}\n".format(t+a))

print("Subtraction of Matrices is\n{0}\n".format(t-a))

'''
Output
Matrix A is 
[[4 5]
 [2 3]
 [4 3]
 [4 8]]

Transpose of Matrix  A is 
[[4 2 4 4]
 [5 3 3 8]]

Multiplication of matrices is
[[41 23 31 56]
 [23 13 17 32]
 [31 17 25 40]
 [56 32 40 80]]

Traceback (most recent call last):
  File "E:/csvproject/matrixpgm4.py", line 14, in <module>
    print("Addition of Matrices is\n{0}\n".format(t+a))
ValueError: operands could not be broadcast together with shapes (2,4) (4,2) 

'''