import numpy.random as rnd
import numpy as np
import scipy.linalg as la


rnd.seed(5)
v=np.random.normal(0,1,1000)
x=[i for i in v if -2<i<2]
k=len(x)
print(k/10)
