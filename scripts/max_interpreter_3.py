# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 11:18:18 2022

@author: Ghost
"""

"""
LIBRARY IMPORTS
"""

import pandas as pd
import numpy as np
import os
import math
import string
import csv
from mpl_toolkits import mplot3d
import ast
from calendar import monthrange # Probably don't need this

"""
CONFIG
"""

filepath = "D:\#PERSONAL\#STEDWARDS\#Summer2022Research"
june_2010filepath = "D:\#PERSONAL\#STEDWARDS\#Summer2022Research\monthly_ozone_data\june_2010csv.csv"

"""
GLOBAL VARIABLES
"""
june2010_df = pd.DataFrame()

"""
FUNCTION DEFINITIONS
"""
def row_operator(list_item, dataframe):
    i = 0
    length = len(list_item)
    while i < length:
        print(list_item[i])
        row = pd.Series(data = list_item[i])
        print(row)
        dataframe = pd.concat([dataframe, row])
        i = i + 1
    else:
#        print(dataframe)
        return("Complete")

"""
MAIN
"""
with open(june_2010filepath) as june_file:
    june_list = list(csv.reader(june_file))
    
    row_operator(june_list, june2010_df)
    
    june_series = pd.Series(data = june_list)
    print(june_series)
    print(len(june_series))
    print(june_series[0])