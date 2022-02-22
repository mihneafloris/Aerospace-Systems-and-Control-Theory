# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 17:26:06 2019

@author: Mihnea
"""
from scipy import signal
import numpy as np
import matplotlib.pyplot as plt
import scipy.linalg as la
import control.matlab as c
# parameter values
m = 4
b = 9
k = 60
w1 = 3.7059918
w2 = 3.5311117
t=np.arange(0.0, 20.01, 0.01)
f1=np.sin(t * w1)
f2=np.sin(t * w2)
# matrices
A = np.matrix([[ -b/m, -k/m], [ 1, 0]])
B = np.matrix([[ 1/m], [ 0]])
C = np.matrix([[ 0, 1]])
D = np.matrix([[ 0]])
# system
sys = c.ss(A, B, C, D)

x0 = np.matrix([[ 1.0], [0.0]])
t = np.arange(0.0, 4.01, 0.01)
y = c.initial(sys, t, x0)
plt.plot(t, y[0])
plt.show()