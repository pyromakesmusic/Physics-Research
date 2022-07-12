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
source_filepath = r"D:\#PERSONAL\#STEDWARDS\#Summer2022Research\july_8_test_version6.xlsx"


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
def histo_builder(df):
    return(True)

def cluster_plotter(df):
    return(True)

def year_overyearplotter(df):
    return(True)

def month_bymonthplotter(df):
    return(True)

"""
MAIN FUNCTION CALLS
"""
with open(source_filepath) as source:
    data = pd.read_excel(source_filepath)
    print("Hello World")
    print(data)
    print(data.keys())
    print(data.describe())
    data.groupby(by="cluster")
    print(data)
    print(data.describe())
    
    print(data.index)
    print(data.columns)
    
    plt.hist(data['maximum'], bins = 30)
#    data.hist(column = 'datestring', by = 'cluster')
"""
FILE OUTPUT
"""