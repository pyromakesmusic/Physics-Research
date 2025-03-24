# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 18:06:58 2025

@author: paulj
"""

# Add this at the very beginning of your script
import sys
sys.path.append("C:/Users/brian/Documents/AQ_ Ozone and PM for HGB SOMs-20250201T165418Z-001 - Copy/AQ_ Ozone and PM for HGB SOMs/Regional Analysis maps AQ over sites/Codes/")

# Then continue with your original imports
import h5py
import numpy as np
import matplotlib.pyplot as plt
import contextily as cx
import pandas as pd
import matplotlib.dates as mdates
import matplotlib.colors as mcolors
import matplotlib.cm as cmx
import matplotlib as mpl
import matplotlib.text as mtext
from EPIC_Graph_Function import EPIC_Graph_Function  # This should now work
import matplotlib_inline

from EPIC_Graph_Function import EPIC_Graph_Function
import matplotlib_inline
matplotlib_inline.backend_inline.set_matplotlib_formats('png', 'jpeg')
from matplotlib import rcParams

#rcParams['font.family'] = 'serif'
rcParams['font.family'] = 'arial'
rcParams['font.size'] = 20



dataTCEQsites = pd.read_csv('../Data/TCEQ_Site_Location_Data (version 1).csv')


###############################################################################
#####################  Map only  ##############################################
###############################################################################

fig = plt.figure(figsize=(11.6, 7))
ax1 = fig.add_subplot(111)


#pull up necessary functions for making the map plot
lon_list,lat_list,df,min_lon_tx,max_lon_tx,min_lat_tx,max_lat_tx,gdf,world = EPIC_Graph_Function()
EPIC_lon_bounds = np.array(lon_list)+0.125
EPIC_lat_bounds = np.array(lat_list)-0.125

im2 =world.boundary.plot(ax=ax1,cmap='Greys', alpha=1)

# Specify the latitude and longitude bounds for the map
ax1.set_xlim(-96.1,-94.0)  # longitude bounds
ax1.set_ylim(29.0,30.3)    # latitude bounds



map_point_size = 200
line_width_value = 2
colorscheme = 'viridis'

label_size = 26
tick_label_size = 20

# Background image for the map
cx.add_basemap(im2,crs=gdf.crs,source='https://tiles.stadiamaps.com/tiles/stamen_toner/{z}/{x}/{y}{r}.png?api_key=bc4a6e42-ab94-4a2d-8b3a-9870188a8543')

# Add site locations to the map
#point_UH = ax1.scatter(-95.339, 29.724, s=map_point_size, marker='o', c='yellow', edgecolors='k', linewidths=line_width_value)
#point_UH_Liberty = ax1.scatter(-94.79, 30.0966, s=map_point_size, marker='o', c='yellow', edgecolors='k', linewidths=line_width_value)

tceq_sites = ax1.scatter(dataTCEQsites['CAMS_Long'], dataTCEQsites['CAMS_Lat'], c='orange', edgecolors='k', marker='.', s=map_point_size)


# Specifies tick mark locations
xticks_major = np.arange(-96, -93.95, 0.5)  # Major ticks every 0.5 degrees
xticks_minor = np.arange(-96, -93.95, 0.1)  # Minor ticks every 0.5 degrees
yticks_major = np.arange(29, 30.34, 0.5)  # Major ticks every 0.5 degrees
yticks_minor = np.arange(29, 30.34, 0.1)  # Minor ticks every 0.1 degrees

# Set major ticks for x axis
ax1.set_xticks(xticks_major)
ax1.set_xticklabels(xticks_major, fontsize=tick_label_size)  # Set fontsize for major tick labels

# Set minor ticks for x axis
ax1.set_xticks(xticks_minor, minor=True)

# Set major ticks for y axis
ax1.set_yticks(yticks_major)
ax1.set_yticklabels(yticks_major, fontsize=tick_label_size)  # Set fontsize for major tick labels

# Set minor ticks for y axis
ax1.set_yticks(yticks_minor, minor=True)

# Customize appearance of minor ticks (optional)
ax1.tick_params(axis='x', which='minor', length=6, color='gray')  # Shorter gray ticks
ax1.tick_params(axis='y', which='minor', length=6, color='gray')  # Shorter gray ticks        

# Customize ticks on both sides
ax1.tick_params(axis='x', which='both', direction='inout', top=True, bottom=True)
ax1.tick_params(axis='x', which='major', length=10)  # Longer ticks for major
ax1.tick_params(axis='x', which='minor', length=6, color='gray')  # Shorter gray ticks for minor
ax1.tick_params(axis='y', which='both', direction='inout', right=True, left=True)
ax1.tick_params(axis='y', which='major', length=10)  # Longer ticks for major
ax1.tick_params(axis='y', which='minor', length=6, color='gray')  # Shorter gray ticks for minor

ax1.set_title('Houston-Galveston-Brazoria (HBG) region', fontdict={'fontsize': label_size})

# Adjust layout to prevent overlap
plt.tight_layout()
plt.savefig('../Plots/HGB-map.png', dpi=300)
plt.show()

    
    