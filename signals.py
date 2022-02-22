# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 21:03:08 2019

@author: Mihnea
"""
import control.matlab as c
import numpy as np
import matplotlib.pyplot as plt
import scipy.linalg as la
import numpy.random as rnd

dt = 0.15
t = np.arange(0.0, 30+dt, dt)
u = np.hstack( ( 6.5*np.arange(0, 1.02 , 0.02), 6.5* np.ones( (150) ) ) )
plt.plot(t, u)
plt.show()
print(sum(u))
'''
dt = 0.04
t = np.arange(0.0, 30+dt, dt)
u = np.hstack( (np.zeros( (25) ), np.arange(0, 1.01, 0.01), np.ones( (625) ) ) )
plt.plot(t, u)
plt.show()
'''

rampend = 7.5   # end time of ramp phase
rampsize = 6.5 # size of the ramp
dt = 0.15

t = np.arange(0, 30+dt, dt)
u = np.minimum(t/rampend, 1.)*rampsize

print(u.sum())

# these things are easily verified by plotting, so this is a good idea....
plt.plot(t, u)
plt.show()

#their shit ^