# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 19:41:44 2019

@author: Mihnea
"""

import control.matlab as c
s = c.tf([1, 0], [1])
k1=1

h1 = (5.0)/(s**2 +3*s + 5)
g = k1* (1+ 0.2/s)


a=((g*h1)/(1+g*h1)).minreal()
print(a)
print(a.num)
print(a.den)

b=1

c= (h1/(1+g*h1)).minreal()
print(c.num)
print(c.den)

d=h1
print(d.num)
print(d.den)