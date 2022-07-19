# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 05:23:53 2022

@author: Ghost
"""

import pandas as pd
import numpy as np
import os
import math
import string
import csv
import matplotlib.pyplot as plt
import ast

"""
CONFIG
"""
ozone_filepath = r"D:\#PERSONAL\#STEDWARDS\#Summer2022Research\SOM_cluster_AUGMENTED3_july19.csv"
windrun_filepath = r"D:\#PERSONAL\#STEDWARDS\#Summer2022Research\data_210726.txt"
moody_wind_filepath = r"D:\#PERSONAL\#STEDWARDS\#Summer2022Research\wind_data_2010_2019_MOOT_C695.csv"


pd.options.display.width = 0
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)



"""
GLOBAL VARIABLES
"""

"""
FUNCTION DEFINITIONS
"""
def histo_builder(df, x, y):
    hist = df.hist(column="maximum", figsize=(6,5))
    return(hist)

def cluster_plotter(df):
    i = 0
    while i < 16:
        cluster = df.loc[df['cluster'] == i]
        histo_builder(cluster, "maximum daily 8 hour ozone (ppb)", "number of days")
        i = i + 1
    return(True)

def site_plotter(df):
    return(True)

def year_overyearplotter(df):
    i = 2010
    while i < 2020:
        year = df.loc[df['year'] == i]
        histo_builder(year, "maximum daily 8 hour ozone (ppb)", "number of days")
        i = i + 1
    return(True)

def month_bymonthplotter(df):
    i = 6
    while i < 10:
        month = df.loc[df['month'] == i]
        histo_builder(month, "maximum daily 8 hour ozone (ppb)", "number of days")
        i = i + 1
    return(True)


"""
MAIN FUNCTION CALLS
"""
with open(ozone_filepath) as ozone:
    data = pd.read_csv(ozone_filepath)
    print("Hello World")
    print(data)
    print(data.keys())
    print(data.describe())
    data.groupby(by="cluster")
    print(data)
    print(data.describe())
    
    print(data.index)
    print(data.columns)
    
#    data.hist(column = 'datestring', by = 'cluster')
print("first by cluster")
#cluster_plotter(data)
print("now the months")
#month_bymonthplotter(data)
print("and finally years")
year_overyearplotter(data)

with open(windrun_filepath) as windrun:
    windrun_data = pd.read_csv(windrun_filepath, delim_whitespace=True)
    print(windrun_data)
    print(windrun_data.index)
    print(windrun_data.describe())
    
with open(moody_wind_filepath) as moody_wind:
    moody_data = pd.read_csv(moody_wind_filepath)
    print(moody_data)
    print(moody_data.describe())
"""
FILE OUTPUT
"""