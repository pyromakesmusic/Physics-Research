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
output_filepath = r"D:\#PERSONAL\#STEDWARDS\#Summer2022Research\\scripts\\file_outputs"
source_filepath = r"D:\#PERSONAL\#STEDWARDS\#Summer2022Research\monthly_ozone_data"
# This file is 23 rows long.
"""
GLOBAL VARIABLES
"""
directory_list = os.listdir(r'D:\#PERSONAL\#STEDWARDS\#Summer2022Research\monthly_ozone_data')
june2010_df = pd.DataFrame()

"""
FUNCTION DEFINITIONS
"""
def row_operator(list_item):
    i = 0
    length = len(list_item)
    list_series = pd.Series(data = list_item)
    list_of_rows = []
    print(list_series)
    while i < length:
        row_item = pd.Series(data = list_series[i])
        list_of_rows.append(row_item)
        i = i + 1
    else:
        output_dataframe = pd.concat(list_of_rows, axis = 1)
        output_dataframe = output_dataframe.T
        print(output_dataframe)
        return(output_dataframe)

def file_dflooper(source_path):
    with open(source_path) as source_file:
        month_list = list(csv.reader(source_file))
        test_dataframe = row_operator(month_list)
    return(test_dataframe)

def input_pathbuilder(iterable, base_path):
    length = len(iterable)
    filepath_list = []
    i = 0
    while i < length:
        full_path = base_path + iterable[i]
        filepath_list.append(full_path)
        i = i + 1
    else:
        return(filepath_list)

def output_pathbuilder(name, base_path):
    return(name + base_path)

"""
MAIN
"""


list_of_filepaths = input_pathbuilder(directory_list, source_filepath) # This is a global variable declaration, which I normally wouldn't want to put here but it needs to go after the function definitions.
