

import numpy.random as rnd
import numpy as np
import scipy.linalg as la

rnd.seed(5)
a = rnd.randn(5,5)
e = la.eig(a, right=False) # don't need eigenvectors
# calculate the norm of the complex numbers
print(np.abs(e))
print(e)
#--------------------------------
d=-9-1.j
theta = np.arcsin(np.imag(d)/np.abs(d))
print(theta*180/np.pi)
#-------------------------------------------
print(np.sum(np.sin(np.arange(0,5.001,0.1))))
#-------------------------------------------
rnd.seed(4)
A=rnd.randn(20,70)

twos=np.ones((20,70))*2
s=0
for i in range(20):
    for j in range(70):
        if(A[i,j] >2):
            s=s+A[i,j]

print(s)

#OR

rnd.seed(4)
a = rnd.randn(20, 70)
print(np.sum(a[a > 2]))
#--------------------------------------------

rnd.seed(5)
v=np.random.normal(0,1,1000)
x=[i for i in v if -2<i<2]
k=len(x)
print(k/10)

#OR
rnd.seed(5)
a = rnd.randn(1000)
print(100.0*np.sum((a < 2.0) & (a > -2.0))/1000)

