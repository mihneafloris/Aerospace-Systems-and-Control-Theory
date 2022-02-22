# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 13:58:01 2019

@author: Mihnea
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.special import legendre
import scipy as sc
from functools import partial
from copy import copy
import control.matlab as c


Kr=-0.5

A = np.mat('''-0.2  0.06 0    -1;
               0    0    1     0;
             -17    0   -3.8   1;
               9.4  0   -0.4  -0.6''')
B = np.mat('''-0.01  0.06;
               0     0;
             -32     5.4;
               2.6  -7''')

C = np.mat('''0 0 0 1''')
D = np.zeros((1,2))
sys1=c.ss(A,B,C,D)

K =np.mat([[0], [Kr]])
sys2=sys1.feedback(K)

A_fb = np.mat([[-0.5]])
B_fb = np.mat([[0.5]])
C_fb = np.mat([[0], [-Kr]])
D_fb = np.mat([[0], [Kr]])
K_wash = c.ss(A_fb, B_fb, C_fb, D_fb)
sys3= sys1.feedback(K_wash)

t =np.arange(0.1, 20.1, 0.1)

u = np.zeros((t.size,2))
u[:10,0]=1.0
        
for i, (name, system) in enumerate([ ('no damper', sys1), 
                                     ('plain damper', sys2),
                                     ('washout damper', sys3) ]):
    print(name)
    c.damp(system, True)
    y, t, _x = c.lsim(system, u, t)
    print("value at 20s", y[-1])
    plt.subplot(3,1,i+1)
    plt.plot(t, y)
    plt.title(name)

plt.show()

wash = c.ss(-0.5, 0.5, -1, 1)
t = np.arange(0, 10, 0.1)
y, t = c.step(wash, t)
plt.plot(t, y)
plt.show()