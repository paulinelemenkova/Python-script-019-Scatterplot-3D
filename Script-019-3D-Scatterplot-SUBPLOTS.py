#!/usr/bin/env python
# coding: utf-8
import numpy as np
import pandas as pd
import matplotlib.cm as cmx
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.colors import ListedColormap

df = pd.read_csv("Tab-Morph.csv")

fig = plt.figure(figsize=(10.0, 8.0), dpi=300)
fig.suptitle('3D correlation scatter plot, factors: \n sediment thickness, slope steepness, bathymetry',
             fontsize=10, fontweight='normal', x=0.5, y=0.97)

# subplot 1
ax = fig.add_subplot(221, projection='3d')
ax.scatter(df.plate_pacif, df.sedim_thick, df.slope_angle,
           c='#ee827c', edgecolors='grey', s=130, alpha=.9)
ax.view_init(30, 185)
ax.tick_params(axis='x', labelsize=7)
ax.tick_params(axis='y', labelsize=7)
ax.tick_params(axis='z', labelsize=7)
plt.title('Pacific Plate', fontsize=8, fontfamily='serif')

# subplot 2
ax = fig.add_subplot(222, projection='3d')
ax.scatter(df.plate_phill, df.sedim_thick, df.slope_angle,
           c='#f8b500', edgecolors='grey', s=130, alpha=.6)
ax.view_init(30, 185)
ax.tick_params(axis='x', labelsize=7)
ax.tick_params(axis='y', labelsize=7)
ax.tick_params(axis='z', labelsize=7)
plt.title('Phillipine Plate', fontsize=8, fontfamily='serif')

# subplot 3
ax = fig.add_subplot(223, projection='3d')
ax.scatter(df.plate_carol, df.sedim_thick, df.slope_angle,
           c='#aacf53', edgecolors='grey', s=130, alpha=.8)
ax.view_init(30, 185)
ax.tick_params(axis='x', labelsize=7)
ax.tick_params(axis='y', labelsize=7)
ax.tick_params(axis='z', labelsize=7)
plt.title('Caroline Plate', fontsize=8, fontfamily='serif')

# subplot 4
ax = fig.add_subplot(224, projection='3d')
ax.scatter(df.plate_maria, df.sedim_thick, df.slope_angle,
           c='#0095d9', edgecolors='grey', s=130, alpha=.7)
ax.view_init(30, 185)
ax.tick_params(axis='x', labelsize=7)
ax.tick_params(axis='y', labelsize=7)
ax.tick_params(axis='z', labelsize=7)
plt.title('Mariana Plate', fontsize=8, fontfamily='serif')

plt.tight_layout()
plt.subplots_adjust(top=0.85, bottom=0.08,
                    left=0.10, right=0.95,
                    hspace=0.05, wspace=0.05
                    )
fig.savefig('plot_3DScat.png', dpi=300)
