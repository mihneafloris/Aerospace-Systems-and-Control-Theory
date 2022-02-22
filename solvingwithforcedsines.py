# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 18:06:31 2019

@author: Mihnea
"""

import numpy as np
import control.matlab as c
from matplotlib.pyplot import plot, show

# parameter values
m = 4.0
b = 9.0
k = 60.0
# matrices
A = np.matrix([[ -b/m, -k/m], [ 1, 0]])
B = np.matrix([[ 1/m], [ 0]])
C = np.matrix([[ 0, 1]])
D = np.matrix([[ 0]])
# system
sys = c.ss(A, B, C, D)
w1 = 3.7059918
w2 = 3.5311117

t = np.arange(0.0, 20.001, 0.01)
u1 = np.sin(t*w1)
u2 = np.sin(t*w2)
y1, tdum, xdum = c.lsim(sys, U=u1, T=t)
y2, tdum, xdum = c.lsim(sys, U=u2, T=t)
plot(t, y1, t, y2)
show()
print(y1.max())
print(y2.max())