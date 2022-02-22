# -*- coding: utf-8 -*-
"""
Created on Thu May  9 15:30:46 2019

@author: Mihnea
"""
import numpy as np
import numpy.random as rnd
import scipy.linalg as la

t = la.toeplitz(np.arange(1, 6))
rnd.seed(9)
m = rnd.rand(5,5)
mT = m.transpose()
c=np.concatenate((mT, t))
print(c)
print(sum(c[:,0]))
'[print(dir(c))