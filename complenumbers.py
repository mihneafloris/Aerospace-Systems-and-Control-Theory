# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 14:59:53 2019

@author: Mihnea
"""
import numpy as np 
import random as rnd
rnd.seed(5)
z = np.rnd.normal(0,1,(5,5))
m=np.matrix(z)
la = np.linalg.eigvals(m)
print(la)
length=[]
for i in range(5):
    length.append((la.real[i]**2 + la.imag[i]**2)**(1/2))
print(length)
m1=length.index(max(length))
print(la.real[m1])
m2=length.index(min(length))
print(la.imag[m2])