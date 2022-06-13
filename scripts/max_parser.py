# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 08:12:18 2022

@author: Ghost
"""

"""
1.LIBRARIES
"""
import pandas as pd
import numpy as np
import os
import datetime
import ast
import csv
import math
import time


"""
2.GLOBAL VARIABLES
"""

output_columns_array = []


"""
3.FUNCTION DEFINITIONS
"""

"""
4.MAIN
"""

os.chdir('D:\\#PERSONAL\\#STEDWARDS\\#Summer2022Research\\')
         
with open('onecolumn_md8ho.csv') as ozone_column:
    print(ozone_column)
    ozone_array = csv.reader(ozone_column)
    ozone_list = list(ozone_array)
    print(ozone_list)
    print(ozone_list[1]) # The data that needs to be parsed starts at index 1

    print(len(ozone_list))
    
    i = 0
    max_length = len(ozone_list)
    while i < max_length:
        print(ozone_list[i])
        i = i + 1

"""
5.UNIT TESTING
"""