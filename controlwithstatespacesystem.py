# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 13:37:37 2019

@author: Mihnea
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.special import legendre
import scipy as sc
from functools import partial
from copy import copy
import control.matlab as c
# first enter the basic aircraft
#Kd = -0.5
A = np.mat('''-0.2  0.06 0    -1;
               0    0    1     0;
             -17    0   -3.8   1;
               9.4  0   -0.4  -0.6''')
B = np.mat('''-0.01  0.06;
               0     0;
             -32     5.4;
               2.6  -7''')

C = np.mat('''1 0 0 0;
           0 1 0 0;
           0 0 1 0;
           0 0 0 1''')
D = np.zeros((4,2))
sys =c.ss(A,B,C,D)


K= [[0,0,0,0],
    [0,0,0, -0.5]]
fsys = sys.feedback(K)

print(fsys)