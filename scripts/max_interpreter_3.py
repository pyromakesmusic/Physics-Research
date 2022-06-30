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


"""
FUNCTION DEFINITIONS
"""
def row_operator(list):
    i = 0
    length = len(list)
    while i < length:
        print(list[i])
        i = i + 1
    else:
        print("Success")

"""
MAIN
"""
with open(june_2010filepath) as june_file:
    june_list = list(csv.reader(june_file))
    
    row_operator(june_list)