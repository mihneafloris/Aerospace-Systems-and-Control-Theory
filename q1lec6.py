# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 19:00:52 2019

@author: Mihnea
"""
import control.matlab as ctrl
import numpy as np

A = [ [ -1,    0,    0  ],
      [ 0.4, -1.2, -5.0],
      [ 0,    1,    0  ] ]
B = [ [0.3 ], [0 ], [0 ] ]
C = [ [0,   1, 0 ],
      [0.1, 0, 1 ]]
D= [ [0], 
     [0] ]

sys = ctrl.ss(A, B, C, D)
h=ctrl.tf(sys)
h1=ctrl.tf(sys)[[0,0]]
h2=ctrl.tf(sys)[[1,0]]
print(h1)
print(h2)
print(ctrl.pole(h1))

#---------------------
A = [ [-2,    0,    0  ],
      [ 0.4, -1.2, -5.0],
      [ 0,    1,    0  ] ]
B = [ [0.3 ], [0 ], [0 ] ]
C = [ [0,   1, 0 ],
      [0.1, 0, 1 ]]
D= [ [0], 
     [0] ]

sys = ss(A, B, C, D)
H = tf(sys)
print(H)
roots(H.den[0][0])