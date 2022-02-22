# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 16:41:05 2019

@author: Mihnea
"""

from control.matlab import *
import numpy as np
import matplotlib.pyplot as plt

# first enter the basic aircraft
A = np.mat('''-0.2  0.06 0    -1;
               0    0    1     0;
             -17    0   -3.8   1;
               9.4  0   -0.4  -0.6''')
B = np.mat('''-0.01  0.06;
               0     0;
             -32     5.4;
               2.6  -7''')
# only need rudder input!
# note that specifying the column index as [1], keeps the B
# as a column vector
B = B[:,[1]]
# only need yaw rate r, so create custom output matrices
C = np.mat(''' 0   0   0   1''')
D = np.mat([[0]])
# the system
sys0 = ss(A, B, C, D)
# calculate a step response
T = np.arange(0, 20, 0.01)
y, t = step(sys0, T)
# plot the response
plt.plot(t, y)
plt.show()
# it looks like the minimum is in the first second
print("minimum", np.min(y[t<1]))