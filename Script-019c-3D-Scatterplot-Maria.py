#!/usr/bin/env python
# coding: utf-8
#
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cmx
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.colors import ListedColormap
#
# Dataset
df = pd.read_csv("Tab-Morph.csv")
#
# Plotting
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(df.plate_maria, df.sedim_thick, df.slope_angle,
           c='#0095d9', edgecolors='grey', s=130, alpha=.7)
ax.view_init(30, 185)
plt.title('Mariana Plate \ncorrelation of the factors: \n sediment thickness, slope steepness, bathymetry', fontsize=10, fontfamily='serif')
plt.show()
