# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 14:53:09 2019

@author: Mihnea
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.special import legendre
import scipy as sp
from functools import partial
from copy import copy
import control.matlab as c

# for 2-output, 1-input transfer functions, either enter the coefficient
# matrices directly, as done here 
hs = c.tf([[[1.]], 
         [[1, 0]]], 
        [[[1, 0, 0]], 3
         [[1., 0, 0]]])
ssat = c.ss(hs)
#print(ssat)


s = c.tf([1, 0], [1])

# or copy num and den from a transfer function created;
# need tf and derivative here
h2 = 40/(s**2 + 12*s + 40)
hm = c.tf([[h2.num[0][0]], 
         [(h2*s).num[0][0]]], 
        [[h2.den[0][0]], 
         [(h2*s).den[0][0]]])
ssen = c.ss(hm)

Ks = 0.5
sys = c.append(ssat, ssen, Ks)

'''
Let's look again at the list of inputs and outputs for the combined model:

The satellite attitude is output 1
The satellite rate is output 2
The attitude measured by the measurement sensor is output 3
The rate of the above is output 4
The controller gain is output 5
The satellite input is input 1
The measurement sensor is input 2
The controller input is input 3
INPUTS IN MORTII TAI: SATELLITE INPUT =    INPUT 1
                      MEASUREMENT SENSOR = INPUT 2
                      CONTROLLER INPUT =   INPUT 3
OUTPUTS IN MORTII EI: SATELLITE ATTITUDE = OUTPUT 1 (1,2 GIVEN BY SAT WITH TF)
                      SATELLITE RATE =     OUTPUT 2
                      SENSOR ATTITUDE =    OUTPUT 3 (3,4 given by sensor with tf)
                      SENSOR RATE =        OUTPUT 4
                      CONTROLLER GAIN =    OUTPUT 5
'''
# connect the inputs and outputs
# outputs 1 and 2: system theta and thetadot
# outputs 3 and 4: sensor theta and thetadot
# output 4: controller
# 1st input: system input, connected to the controller output (5)
# 2nd input: sensor input, connected to satellite theta (1)
# 3rd input: controller in, feedback from sensed position and speed (-3, -4)
Q = sp.mat('''1 5 0;
              2 1 0;
              3 -3 -4''')

# remaining input: controller (3)
inputv = [3]
# remaining outputs: controller, theta, thetadot
outputv = [5, 1, 2]
sysc = c.connect(sys, Q, inputv, outputv)
print(sysc)

hc = (Ks / s**2).feedback(h2 * (1 + s))
print( hc.pole())
print (sp.linalg.eig(sysc.A)[0])