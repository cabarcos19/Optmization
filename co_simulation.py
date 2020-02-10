# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 14:40:37 2019

@author: Alex8Cabarcos
"""

import fmpy
from matplotlib import pyplot as plt

dahl = 'Dahlquist1.fmu';
#fmpy.dump(dahl)
#results=fmpy.simulate_fmu(dahl)
#results=fmpy.simulate_fmu(dahl,start_values={'x':3})
#l =['hello',1.0,2];
#print(l[0])
#l.append('bye')
result = [];
xStart = [i for i in range(11)]
#list_a = list(range(11))
#len(xStart)==len(list_a)

for i in xStart:
    rs = fmpy.simulate_fmu(dahl,start_values={'x':i},start_time=0,stop_time=5)
    result.append(rs)

for j in range(11): 
    plt.plot(result[j]['time'],result[j]['x'])


plt.xlabel("Time (s)")
plt.ylabel("x")
plt.grid(color='grey', linestyle='-', linewidth=2)
kValues = [0,1,2,3,4,5,6,7,8,9]
plt.legend(kValues)

#dtype <f8 -> little-endian single-precision float
#result[0].dtype.kind 'V'-> raw data