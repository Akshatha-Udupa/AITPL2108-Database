#x=4x2, y= 2x4,z=2x2 perform (x*y*z)+(y*z)+x

import numpy as np
x = np.array([[4, 5],[2, 3],[2, 3],[1, 8]])
print("Matrix X is \n{0}\n".format(x))

y = np.array([[4, 1, 2, 3],[4, 2, 1, 5]])
print("Matrix Y is \n{0}\n".format(y))

z = np.array([[2, 3],[4, 3]])
print("Matrix Z is \n{0}\n".format(z))

xy = x.dot(y)
print("x * y =\n{0}".format(xy))
xyz = xy.dot(z)

#cannot multiply xy * z i.e (4 X 4) (2 x2)
print("x*y*z=\n{0}".format(xyz))

#cannot multiply y * z i.e((2 X 4)(2 x 2))
yz= y.dot(z)
print("y * z")

eq1 = xyz + yz
print("(x*y*z)+(y*z)+x)={0}\n".format(eq1+x))
# therefore (x*y*z)+(y*z)+x cannot be performed

'''
Output
Matrix X is 
[[4 5]
 [2 3]
 [2 3]
 [1 8]]

Matrix Y is 
[[4 1 2 3]
 [4 2 1 5]]

Matrix Z is 
[[2 3]
 [4 3]]

x * y =
[[36 14 13 37]
 [20  8  7 21]
 [20  8  7 21]
 [36 17 10 43]]
Traceback (most recent call last):
  File "E:/csvproject/matrixpgm5.py", line 15, in <module>
    xyz = xy.dot(z)
ValueError: shapes (4,4) and (2,2) not aligned: 4 (dim 1) != 2 (dim 0)
'''