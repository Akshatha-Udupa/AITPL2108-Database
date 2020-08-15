#Transpose of a mtarix
import numpy as np
a = np.array([[1,2,3],[4,5,6],[7,8,9]])
print("Matrix A is\n{0}\n".format(a))
print("Transpose of Matrix is \n{0}".format(a.transpose()))

'''
output
Matrix A is
[[1 2 3]
 [4 5 6]
 [7 8 9]]

Transpose of Matrix is 
[[1 4 7]
 [2 5 8]
 [3 6 9]]

'''