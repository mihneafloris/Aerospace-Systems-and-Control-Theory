# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 15:30:39 2019

@author: Mihnea
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.special import legendre
import scipy as sp
from functools import partial
from copy import copy
import control.matlab as c

Ka =4
TAUa = 1.1
Kap = 0.5

#output y contains output of autopilot, actuator output, aircraft roll angle
#(theta)
s = c.tf([1, 0], [1])
Ha = 9 /(s**2 +5*s +9)
Hr = Ka /((TAUa *s +1)*s)


