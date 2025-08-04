# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 00:30:04 2020

@author: Lenovo
"""

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import math

pi = math.pi 

xval = np.arange(0, 2*pi, 0.01)
yval = np.ones_like(xval)

colormap = plt.get_cmap('hsv')
norm = mpl.colors.Normalize(0.0, 2)
ax = plt.subplot(1, 1, 1, polar=True)
ax.scatter(xval, yval, c=xval, s=300, cmap=colormap, norm=norm, linewidths=0)
ax.set_yticks([])