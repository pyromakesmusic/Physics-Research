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
source_filepath = r"D:\#PERSONAL\#STEDWARDS\#Summer2022Research\SOM_cluster_AUGMENTED3_july19.csv"


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
with open(source_filepath) as source:
    data = pd.read_csv(source_filepath)
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
"""
FILE OUTPUT
"""