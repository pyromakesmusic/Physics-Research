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
pd.options.display.width = 0
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', -1)

"""
GLOBAL VARIABLES
"""
directory_list = os.listdir('D:\\#PERSONAL\\#STEDWARDS\\#Summer2022Research\\monthly_ozone_data\\')

good_sites = ["Houston East C1/G316", "Houston Aldine C8/AF108/X150", "Channelview C15/AH115",
              "Northwest Harris Co. C26/A110/X154", "Hou.DeerPrk2 C35/235/1001/AFH139FP239",
              "Seabrook Friendship Park C45", "Houston Bayland Park C53/A146", "Conroe Relocated C78/A321",
              "Manvel Croix Park C84", "Clinton C403/C304/AH113", "Houston North Wayside C405/C1033", 
              "Houston Monroe C406", "Lang C408", "Houston Croquet C409", "Houston Westhollow C410/C3003",
              "Park Place C416", "HRM-3 Haden Road C603/A114", "Wallisville Road C617", "Texas City 34th St. C620"
              "Lynchburg Ferry C1015/A165", "Lake Jackson C1016", "Galveston 99th St. C1034/A320/X183"]


"""
FUNCTION DEFINITIONS
"""
def row_operator(list_item):
    i = 0
    length = len(list_item)
    list_series = pd.Series(data = list_item)
    list_of_rows = []
    while i < length:
        row_item = pd.Series(data = list_series[i])
        list_of_rows.append(row_item)
        i = i + 1
    else:
        output_dataframe = pd.concat(list_of_rows, axis = 1)
        output_dataframe = output_dataframe.T
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
#        test_element = month_df[0]
#        print(test_element)
        list_of_dataframes.append(month_df)
        i = i + 1
    else:
        return(list_of_dataframes)


def max_finder(df, column):
    day = df[column]
    maximum = day.max()
    return(maximum)

def column_headers(framelist):
    i = 0
    length = len(framelist)
    while i < length:
        df = framelist[i]
        df.columns = df.iloc[0]
        i = i + 1

def row_headers(framelist):
    i = 0
    length = len(framelist)
    while i < length:
        df = framelist[i]
        df.index = df.iloc[:,0]
        df.style.hide(axis = 0)
        df.style.hide(axis = 1)
        i = i + 1

# Doesn't work atm
def day_return(df, day):
    index = day + 2
    print(df.columns[index])
    return(df[str(index)])

def month_looper(frame):
    i = 1
    days_list = []
    length = frame.shape[1] - 3
    while i < length:
        days_list.append(str(i))
        i = i + 1
    print(days_list)

def badrow_getter(df_column, frame):
    i = 1
    drop_rows = []
    while i < len(df_column):
        if df_column[i] not in good_sites:
            drop_rows.append(i)
            i = i + 1
        else:
            i = i + 1
    print(drop_rows)
#    frame.drop(labels = drop_rows, axis = 0)
    return(drop_rows)



"""
MAIN
"""


list_of_filepaths = input_pathbuilder(directory_list, source_filepath) # This is a global variable declaration, which I normally wouldn't want to put here but it needs to go after the function definitions.
# test_multidex = pd.concat(directory_looper(list_of_filepaths)) # I don't think I want to concat them. I want to manipulate them separately and then create a dataframe at the end that is concatenated.
df_set = directory_looper(list_of_filepaths)

column_headers(df_set)
row_headers(df_set)

df = df_set[0]
columns = df.columns
day_return(df, 25)


bad_rows = badrow_getter(df['Monitoring_Site'], df)


"""
print(bad_rows)
i = 0
length = len(bad_rows)
while i < length:
    row = bad_rows[i]
    print(df[:row])
    i = i + 1
"""

print(bad_rows)
print(df)
i = 0
while i < len(bad_rows):
    row = int(bad_rows[i])
    frame_row = df[:row]
    print(row)
    i = i + 1
    

month_looper(df)