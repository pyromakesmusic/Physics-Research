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
output_filepath = "D:\#PERSONAL\#STEDWARDS\#Summer2022Research\\scripts\\file_outputs"
source_filepath = "D:\\#PERSONAL\\#STEDWARDS\\#Summer2022Research\\monthly_ozone_data\\"
# This file is 23 rows long.
"""
GLOBAL VARIABLES
"""
directory_list = os.listdir('D:\\#PERSONAL\\#STEDWARDS\\#Summer2022Research\\monthly_ozone_data\\')
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

def directory_looper(input_list):
    i = 0
    length = len(input_list)
    list_of_dataframes = []
    while i < length:
        month_df = file_dflooper(input_list[i]) # Given the filepath, this should return the corresponding DataFrame
        print(month_df)
        list_of_dataframes.append(month_df)
        i = i + 1
    else:
        return(list_of_dataframes)

"""
MAIN
"""


list_of_filepaths = input_pathbuilder(directory_list, source_filepath) # This is a global variable declaration, which I normally wouldn't want to put here but it needs to go after the function definitions.
test_multidex = pd.concat(directory_looper(list_of_filepaths)) # I don't think I want to concat them. I want to manipulate them separately and then create a dataframe at the end that is concatenated.
print(test_multidex)
test_multidex.to_csv('test_multidex.csv')