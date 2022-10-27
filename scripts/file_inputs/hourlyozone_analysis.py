# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 03:27:21 2022

@author: Ghost
"""

import unicodedata
import re
import pandas as pd
#import geopandas as gpd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib as mpl
import os
#import osmnx
import math

"""
CONFIG
"""
ozone_filepath = r"D:\#PERSONAL\#STEDWARDS\#Summer2022Research\SOM_cluster_AUGMENTED3_july19.csv"
windrun_filepath = r"D:\#PERSONAL\#STEDWARDS\#Summer2022Research\data_210726.txt"
moody_wind_filepath = r"D:\#PERSONAL\#STEDWARDS\#Summer2022Research\wind_data_2010_2019_MOOT_C695.csv"
site_coords_filepath = r"D:\#PERSONAL\#STEDWARDS\#Summer2022Research\site_coordinates.txt"
particulate_filepath = r"D:\#PERSONAL\#STEDWARDS\#Summer2022Research\daily_pm25_hgb_junsep2010_2019.csv"
hourly_ozone_filepath = r"D:\#PERSONAL\#STEDWARDS\#Summer2022Research\ozone_1hr_v2.csv"

global_output_path = r"D:\#PERSONAL\#STEDWARDS\#Summer2022Research\scripts\file_outputs\yearoveryear_histograms\\"

pd.options.display.width = 0
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

mpl.rcParams['figure.dpi'] = 300


plt.xticks(np.arange(0,150,10))
plt.yticks(np.arange(0,150,10))
    
plt.xticks(fontsize=11)
plt.yticks(fontsize=11)

"""
GLOBAL VARIABLES
"""
#toplayer = mpl.figure.Figure()

hourlyozone_keys = ["Date", "Time", "C1_2", "C8_2", "C15_3", "C26_2", "C35_1", "C45_1", "C53_1", "C78_1", "C84_1", "C403_3", "C405_1", "C406_1", "C408_2", "C409_2", "C410_1", "C416_1", "C603_1", "C603_2", "C603_3", "C617_1", "C620_1", "C1015_1", "C1016_1", "C1034_1"]
ozone_sites = ['C1_2', 'C8_2', 'C15_3', 'C26_2', 'C35_1',
       'C45_1', 'C53_1', 'C78_1', 'C84_1', 'C403_3', 'C405_1', 'C406_1',
       'C408_2', 'C409_2', 'C410_1', 'C416_1', 'C603_1', 'C603_2', 'C603_3',
       'C617_1', 'C620_1', 'C1015_1', 'C1016_1', 'C1034_1']



"""
MAIN FUNCTION CALLS
"""

with open(hourly_ozone_filepath) as hourly_ozone:
    hourlyozone_df = pd.read_csv(hourly_ozone_filepath)
    
    hourlyozone_df[hourlyozone_keys] = hourlyozone_df["data"].str.split(',', n=None, expand=True)
    
    # At this point I've read the data in and need to split the individual column entries into two columns using whitespace as the delimiter
#    pd.to_numeric(hourlyozone_df[ozone_sites], errors="coerce")

print(hourlyozone_df.keys)
print(hourlyozone_df.columns)

x_ozone = "C1_2"
y_ozone = "C15_3"

plt.scatter(hourlyozone_df[x_ozone], hourlyozone_df[y_ozone], s=.5)