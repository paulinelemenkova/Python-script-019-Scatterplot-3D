#!/usr/bin/env python
# coding: utf-8
#
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import numpy as np
import pandas as pd
import matplotlib.cm as cmx
#
# Dataset
df = pd.read_csv("Tab-Morph.csv")
#
# Plotting
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(df.plate_carol, df.sedim_thick, df.slope_angle, c='#aacf53',
           edgecolors='grey', s=130, alpha=.8)
ax.view_init(30, 185)
plt.title('Caroline Plate \ncorrelation of the factors: \n sediment thickness, slope steepness, bathymetry', fontsize=10, fontfamily='serif')
plt.show()
