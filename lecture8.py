# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 16:03:43 2019

@author: Mihnea
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.special import legendre
import scipy as sc
from functools import partial
from copy import copy
import control.matlab as c

s = c.tf([1, 0], [1])
G  = (6205)/( s*(s**2 + 13 * s + 1281) )
Heq = G.feedback(1)
p =c.pole(Heq)


#the real pole is -5(real axis, left plane) => 5/(5+s)

H1 = 5/(5+s)
H2 = c.minreal(Heq/H1)

endt = 3
dt = 0.01
t=sc.arange(0, endt+0.01, dt)

Yeq = c.step(Heq, t)
Y1 =c.step(H1, t)
Y2 = c.step(H2, t)


plt.plot(t, Yeq[0], 'r')
plt.plot(t, Y1[0], 'b')
plt.plot(t, Y2[0], 'g')


D1 = sc.integrate.trapz( np.abs(Yeq[0]-Y1[0]), t)
print(D1)

D2 = sc.integrate.trapz(np.abs(Yeq[0]-Y2[0]), t)
print(D2)
