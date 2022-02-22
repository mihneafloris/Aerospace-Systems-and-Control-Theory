# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 13:04:51 2019

@author: Mihnea
"""

import control.matlab as ctrl
import numpy as np
import scipy.linalg as la
import matplotlib.pyplot as plt

s = ctrl.tf([1, 0], [1])

A = [[ 0,    0,    0 , -0.01 ],
     [ -1/15, -1/15, 0, 1/15],
     [ 1/(15*1100),    1/(15*1100),    0, -1/(15*1100)],
     [0, 0, 1, 0]
    ]
B = [[0.01, 0 ], 
     [-1/15, 0  ], 
     [1/(15*1100), 1/1100 ] ,
     [0,0]
    ]
C = [[1,   0, 0, -1 ],
     [1/15, 1/15, 0, -1/15 ],
     [1/15, 1/15, 0, -1/15 ],
     [0, 1, 0, 0 ],
     [0, 0, 0, 1 ],
     [0, 0, 0, -1 ]
    ]
D= [[1, 0],  
    [1/15, 0],
    [1/15, 1],
    [0,0],
    [0,0],
    [1,0]
   ]

sys = ctrl.ss(A, B, C, D)
print(la.eig(sys.A))

