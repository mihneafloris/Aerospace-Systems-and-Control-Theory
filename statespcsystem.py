# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 16:28:08 2019

@author: Mihnea
"""

import numpy as np
import control.matlab as c
# parameter values
m = 4
b = 9
k = 60

# matrices
A = np.matrix([[ -b/m, -k/m], [ 1, 0]])
B = np.matrix([[ 1/m], [ 0]])
C = np.matrix([[ 0, 1], [ 1, 0], [ -b/m, -k/m]])
D = np.matrix([[ 0], [ 0], [ 1/m]])
# to continue, and make the system
sys = c.ss(A, B, C, D)
print(sys)