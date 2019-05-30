#!/usr/bin/env python
# coding: utf-8

# In[15]:


# libraries
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import numpy as np
import pandas as pd
import matplotlib.cm as cmx
# Dataset
df = pd.read_csv("Tab-Morph.csv")

#np.random.seed(100)
#N = 25
#colors = np.random.rand(N)

# plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(df.plate_maria, df.sedim_thick, df.slope_angle, c='#0095d9', edgecolors='grey', s=130, alpha=.7)
ax.view_init(30, 185)
plt.title('Mariana Plate \ncorrelation of the factors: \n sediment thickness, slope steepness, bathymetry', 
          fontsize=10, fontfamily='serif')
plt.show()


# In[ ]:




