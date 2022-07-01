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
list_of_filepaths = []
output_filepath = r"D:\#PERSONAL\#STEDWARDS\#Summer2022Research\\scripts\\file_outputs"
source_filepath = r"D:\#PERSONAL\#STEDWARDS\#Summer2022Research\monthly_ozone_data\\"
# This file is 23 rows long.
"""
GLOBAL VARIABLES
"""
directory_list = os.listdir(r'D:\#PERSONAL\#STEDWARDS\#Summer2022Research\monthly_ozone_data')
june2010_df = pd.DataFrame()

"""
FUNCTION DEFINITIONS
"""
def row_operator(list_item, output_dataframe):
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

def file_dflooper(source_filepath, file_name, output_path, output_name):
    with open(source_filepath) as source_file:
        month_list = list(csv.reader(source_file))
        test_dataframe = row_operator(month_list, output_path)
        test_dataframe.to_csv('D:\#PERSONAL\#STEDWARDS\#Summer2022Research\\scripts\\file_outputs\\june_2010.csv')
    return(True)

"""
MAIN
"""


print(directory_list)
