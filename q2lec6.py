# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 19:50:17 2019

@author: Mihnea
"""


import control.matlab as ctrl
import numpy as np
import scipy.linalg as la
# first create Laplace variable
s = ctrl.tf([1, 0], [1])
# the coefficients
b0 = 0.4
b1 = 0.1
b2 = 0.5
a0 = 2.3
a1 = 6.3
a2 = 3.6
a3 = 1.0
# create a basic transfer function
h = (b0 + b1*s + b2*s**2)/(a0 + a1*s + a2*s**2 + a3*s**3)
# this combined transfer function has velocity out and the signal itself
H = ctrl.tf([[h.num[0][0]], [(h*s).num[0][0]]], 
       [[h.den[0][0]], [(h*s).den[0][0]]])

# convert to state-space
sys = ctrl.ss(H)
print(la.eig(sys.A)[0])
print(h.pole())
