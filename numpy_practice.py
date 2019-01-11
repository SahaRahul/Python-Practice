# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 20:06:46 2019

@author: rahul
"""
import sys
from datetime import datetime
import numpy as np


### Definition of function
def numpysum(n):
    a = np.arange(n) **2
    b = np.arange(n) **3
    c = a + b
    
    return c

def pythonsum(n):
    a = list(range(n))
    b = list(range(n))
    c = []
    
    for i in range(len(a)):
        a[i] = i ** 2
        b[i] = i ** 3
        c.append(a[i] + b[i])
        
    return c

### Program execution start here
size = int(sys.argv[1])

start = datetime.now()

c = pythonsum(size)
delta = datetime.now() - start
print("The last 2 elements of the sum", c[-2:])
print("pythonsum : Elapse time in microsecond" + str(delta))

start = datetime.now()
c = numpysum(size)
delta = datetime.now() - start
print("The last 2 elements of the sum", c[-2:])
print("numpysum : Elapse time in microsecond" + str(delta))


        
    


