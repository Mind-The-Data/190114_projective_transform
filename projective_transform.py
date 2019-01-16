#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 10:09:20 2019

@author: brian
"""

import numpy as np
import matplotlib.pyplot as plt

array = np.loadtxt('coordinates.txt')

n = array.shape[0] # rows in array to iterate through
f = 1000 # focal length in pixels
sensor_x = 2000 # sensor size in pixels
sensor_y = 1000 # sesnor size in pixels

for i in range(n):
    array[i,0] /= array[i,2] #divide x by z direction (projective space)
    array[i,1] /= array[i,2] # divide y by z direction (projective space)
    
    
u = f * array[:,0] + sensor_x/2 #
v = f * array[:,1] + sensor_y/2 #
I = array[:,3]  # intensity
I = (I - I.min())/I.max() * -1  # shifted,scaled and flipped # now between 0-1

plt.scatter(u,v, c=I, s=10)
plt.colorbar(label='Intensity')
plt.xlim(0,sensor_x) # crop
plt.ylim(0,sensor_y)
plt.ylabel('sensor_y (pixels)')
plt.xlabel('sensor_x (pixels)')
plt.show()
