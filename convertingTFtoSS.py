# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 18:55:39 2019

@author: Mihnea
"""

import control.matlab as ctrl
import numpy as np

# can you recognise this one?
a = np.matrix(""" 0       1      0   ;
                 -0.0071 -0.111  0.12;
                  0       0.07  -0.3""")
b = np.matrix(""" 0 ;    -0.095; 0.072""")
c = np.matrix(""" 1       0     0    """)
d = np.matrix(""" 0     """)
sys = ctrl.ss(a, b, c, d)
h = ctrl.tf(sys)

# a random transfer function
sys = ctrl.rss(3, 2, 3)
print(sys)

h = ctrl.tf(sys)
#print(h)
#print(h.__class__)

# select one of the transfer functions
h11 = ctrl.tf(h.num[0][0], h.den[0][0])
print(h11)