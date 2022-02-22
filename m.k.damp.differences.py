# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 18:10:52 2019

@author: Mihnea
"""
import scipy.linalg as la
import numpy as np
import control.matlab as c
from matplotlib.pyplot import plot, show, figure, title

# parameter values
m = 3.0
b = 9.0
k = 60.0
# matrices
A = np.matrix([[ -b/m, -k/m], [ 1, 0]])
B = np.matrix([[ 1/m], [ 0]])
C = np.matrix([[ 0, 1]])
D = np.matrix([[ 0]])

# base system
sys = c.ss(A, B, C, D)

# increased mass
m = 2*m;
A = [[ -b/m, -k/m], [ 1, 0]]
B = [[ 1/m], [ 0]]
m = m / 2;
sys_2m = c.ss(A, B, C, D)

# increased stiffness
k = 2*k
A = [[ -b/m, -k/m], [ 1, 0]]
B = [[ 1/m], [ 0]]
k = k / 2;
sys_2k = c.ss(A, B, C, D)

# increased damping
b = 2*b
A = [[ -b/m, -k/m], [ 1, 0]]
B = [[ 1/m], [ 0]]
b = b / 2;
sys_2b = c.ss(A, B, C, D)

t = np.arange(0.0, 10.001, 0.01)

x0 = [1, 0]
y, tdum = c.initial(sys, X0=x0, T=t)
y_2m, tdum = c.initial(sys_2m, X0=x0, T=t)
y_2k, tdum = c.initial(sys_2k, X0=x0, T=t)
y_2b, tdum = c.initial(sys_2b, X0=x0, T=t)

for i, (l, y2) in enumerate(
    (('mass', y_2m), ('damping', y_2b), ('spring', y_2k))): 
    figure(i)
    plot(t, y, t, y2)
    title('increased %s' % l)