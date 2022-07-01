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
pd.set_option('display.max_colwidth', None)

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

# This is the core DataFrame constructor for this dataset
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


# This opens a given csv file and makes a dataframe from that sample
def file_dflooper(source_path):
    with open(source_path) as source_file:
        month_list = list(csv.reader(source_file))
        test_dataframe = row_operator(month_list)
    return(test_dataframe)

# Builds up the input file paths
def input_pathbuilder(iterable, base_path):
    length = len(iterable)
    filepath_list = []
    i = 0
    while i < length:
        full_path = base_path + iterable[i]
        print(iterable[i])
        stringname = str(iterable[i])
        string_sep = stringname.split("_")
        date_series = pd.Series(string_sep, index = ["year", "month", "filename"])
        print(date_series)

        filepath_list.append(full_path)
        i = i + 1
    else:
        print("Hooray!")
    return(filepath_list)

# Creates a dataframe of labels based on the filenames
def month_dfbuilder(iterable, base_path, output_df):
    length = len(iterable)
    i = 0
    while i < length:
        print(iterable[i])
        stringname = str(iterable[i])
        string_sep = stringname.split("_")
        date_series = pd.Series(string_sep, index = ["year", "month", "filename"])
        print(date_series)
        output_df = pd.concat([output_df, date_series], axis = 1, )
        i = i + 1
    else:
        print("Hooray!")
        print(output_df)
    return(output_df)


# Builds a location to send a file to
def output_pathbuilder(name, base_path):
    return(name + base_path)

# Returns a list of dataframes from the files in a folder
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

# Returns a list of the max daily 8 hour ozone measurements for a month
def max_finder(df, date_indices):
    i = 0
    max_list = []
    while i < len(date_indices):
        x = date_indices[i]
        column = (df[x])
        numeric_entries = []
        a = 1
        length = len(column)
        while a < length:
            z = str(column[a])
            if z.isdigit():
               numeric_entries.append(column[a])
               a = a + 1
            else:
                a = a + 1
        else: 
            try:
                maximum = max(numeric_entries)
            except ValueError:
                maximum = "NaN"
        max_list.append(maximum)
        i = i + 1
    print(max_list)
    return(max_list)

# This makes sure the column headers are correct in the DataFrames
def column_headers(framelist):
    i = 0
    length = len(framelist)
    while i < length:
        df = framelist[i]
        df.columns = df.iloc[0]
        i = i + 1

# This makes sure the row headers are correct in the DataFrames
def row_headers(framelist):
    i = 0
    length = len(framelist)
    while i < length:
        df = framelist[i]
        df.index = df.iloc[:,0]
        df.style.hide(axis = 0)
        df.style.hide(axis = 1)
        i = i + 1

# This goes through a DataFrame to dynamically determine the number of days in the month
def month_looper(frame):
    i = 1
    days_list = []
    length = frame.shape[1] - 2
    while i < length:
        days_list.append(str(i))
        i = i + 1
    return(days_list)

# This function is supposed to remove the rows which correspond to sites that are not reliable. It is not yet ready.
def badrow_getter(df_column, frame):
    i = 1
    drop_rows = []
    while i < len(df_column):
        if df_column[i] not in good_sites:
            drop_rows.append(i)
            i = i + 1
        else:
            i = i + 1
#    frame.drop(labels = drop_rows, axis = 0)
    return(drop_rows)

# This gets the maxes for a month and gives back a pandas Series
def column_looper(str_list, input_df):
    max_list = max_finder(input_df, str_list)
    max_series = pd.Series(max_list)
    return(max_series)

# This takes a list of dataframes and returns a big DataFrame with all of the daily 8 hour maxes
# The month_set argument is expecting the dataframe with the month data in it
def ozone_parser(df_list, month_set):
    i = 0
    monthly_series = []
    output_df = pd.DataFrame(columns = ["year", "month", "day", "max_ozone"])
    
    # This is saying the program will loop through once for each DataFrame in
    # the set and perform the "else" logic when it is done.
    while i < len(df_list):
        df = df_list[i]
        
        # This gets me a list of the rows I don't want.
        badrows = badrow_getter(df['Monitoring_Site'], df)
        x = 0
        while x < len(good_sites):
            
            rowname = good_sites[x]
            site_list = df['Monitoring_Site']
            d = 0
            while d < site_list.shape[0]:
                site_name = site_list[str(d)]
                if (site_name in good_sites):
                    continue
                else:
                    df.drop(index = site_name)
                d = d + 1
                
            x = x + 1
        else:
            print(df)
        i = i + 1
        
        specials = df["Monitoring_Site"].unique()
        print(specials)

        
        
        cols = month_looper(df)
        month_maxes = max_finder(df, cols)
        maxes_series = pd.DataFrame(month_maxes)
        monthly_series.append(maxes_series)
        output_df = pd.concat([output_df, maxes_series])
        new_row = ["This string should be replaced by the time columns", output_df]
        i = i + 1
        
    else:
        ozone_maxdf = pd.concat(monthly_series, axis = 0)
        month_set = month_set.T
        return(ozone_maxdf)

"""
MAIN
"""
# A placeholder DataFrame
month_df = pd.DataFrame()
# List of all the filepaths that will be parsed.
filepath_list= input_pathbuilder(directory_list, source_filepath) # This is a global variable declaration, which I normally wouldn't want to put here but it needs to go after the function definitions.
# This is a Dataframe that contains time data derived from the file all the data came from. It isn't stored anywhere else.
month_df = month_dfbuilder(directory_list, source_filepath, month_df)

# This is the list of all the DataFrames for every month
df_set = directory_looper(filepath_list)

# An experimental multidex
multidex = pd.concat(df_set)

# Correcting the column headers
column_headers(df_set)

# Correcting the row headers
row_headers(df_set)


month_df.set_index(0)
# This is going to get the max for every month and make a file out of it.
# It should probably also remove the bad rows first
ozone_parser(df_set, month_df)
"""
Need to clean out the bad rows and get the max for the whole dataset. Then error check, then start getting the histograms going.
"""