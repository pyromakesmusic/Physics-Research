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
import datetime

"""
CONFIG
"""
output_filepath = "D:\#PERSONAL\#STEDWARDS\#Summer2022Research\\scripts\\file_outputs"
source_filepath = "D:\\#PERSONAL\\#STEDWARDS\\#Summer2022Research\\monthly_ozone_data\\"
# This file is 23 rows long.

output_filename = "july_8_test_version2.csv"

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

def row_operator(list_item):
    '''This is the core DataFrame constructor for this dataset'''
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
    '''This opens a given csv file and makes a dataframe from that sample'''
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
#        print(iterable[i])
        stringname = str(iterable[i])
        string_sep = stringname.split("_")
        date_series = pd.Series(string_sep, index = ["year", "month", "filename"])
#        print(date_series)

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
#        print(iterable[i])
        stringname = str(iterable[i])
        string_sep = stringname.split("_")
        date_series = pd.Series(string_sep, index = ["year", "month", "filename"])
#        print(date_series)
        output_df = pd.concat([output_df, date_series], axis = 1, )
        i = i + 1
    else:
        print("Hooray!")
#        print(output_df)
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

def dailymax_logic(pdseries, datelabel):
    """
    This is the function to look at later when I want to add the site names.
    Takes a column of information about one site and WANTS TO return the maximum daily 8 hour ozone, plus the site location at which it was measured.
    HERE BE BUGS
    """
    number_series = pd.to_numeric(pdseries, errors = 'coerce')
#    print(number_series)
    maximum = number_series.max()
    max_index = number_series.idxmax()
#    print(maximum, max_index)
#    print("The max of this day is " + str(maximum))
    return_list = [maximum, max_index, datelabel]
    return_df = pd.DataFrame(data=return_list,index=["maximum", "site", "date"])
    return(return_df)

# Returns a list of the max daily 8 hour ozone measurements for a month
def max_finder(df, date_indices, date_df):
    i = 0
    max_list = []
    while i < len(date_indices): # For the sake of debugging, we are going to change this
        day = date_indices[i] # This gives us the day of the month as a string.
        year = date_df['year']
        month = date_df['month']
        date_index = pd.Timestamp(year=int(year), month=int(month), day=int(day))
        column = df[day] # This gives us the column of ozone measurements corresponding to that day.
        daily_max = dailymax_logic(column, date_index)
        print(type(max_list))
        max_list.append(daily_max)
        print(type(max_list))
        #max_list.append(except_logic(column)) # I need to change this into the dataframe equivalent of the same thing: max_list.append(except_logic(column))
#        max_df = max_df.merge(except_logic(column, date_df), how="outer", on="date")
        i = i + 1
    max_df = pd.concat(max_list)
    return(max_df)

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
#    print(days_list)
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

def badrow_remover(clean_sitelist, bad_rowlist, df):
    '''
    Takes a list of good sites, a list of indexes of bad rows, and a dataframe
    and drops the bad rows from the dataframe, returning the good one.
    '''
    d = 1
    while d < len(df.shape):
        site_name = str(df[d])
        if (site_name in clean_sitelist):
#            print(site_name)
            d = d + 1
        else:
            df.drop(index = site_name)
            d = d + 1   
    else:
        output_df = df
    return(output_df)

def label_sep(df, i):
    """
    Should take a dataframe and an index and return the row sliced at that
    index as a series.
    """
    df['row_num'] = np.arange(len(df))
    
    output = df.loc[df['row_num'] == i]
#    print(output)
#    print(type(x))
#    month = df.loc['month'].iloc[i]
#    print(type(y))
#    filename = df.loc['filename'].iloc[i]
#    print(type(z))
#    label_df = pd.DataFrame(data = [year, month, filename]).T
    
    return(output)

# This takes a list of dataframes and returns a big DataFrame with all of the daily 8 hour maxes
# The month_set argument is expecting the dataframe with the month data in it
def ozone_parser(df_list, month_set):
    i = 0
    monthly_series = pd.DataFrame(index = ["year", "month", "day", "max D8HO"])
#    print(monthly_series.shape)
#    print(monthly_series)
    monthly_series = monthly_series.T
    month_set = month_set.T
    month_list=[monthly_series]
    # This is saying the program will loop through once for each DataFrame in
    # the set and perform the "else" logic when it is done.
    while i < len(df_list): # For the sake of debugging we're going to write this a different way:
#    while i < 7:
        df = df_list[i]
        label_row = label_sep(month_set, i)
#        print("The label for the row is " + str(label_row))
        # This gets me a list of the rows I don't want.
        badrows = badrow_getter(df['Monitoring_Site'], df)
        x = 0
        while x < len(good_sites):
            rowname = good_sites[x]
            site_list = df['Monitoring_Site']
            badrow_remover(good_sites, badrows, site_list)
            cleaned_rows = [z for z in site_list if site_list[x] in good_sites]
            
            x = x + 1
        else:
            x = x + 1
        


        
        
        cols = month_looper(df)
        month_maxes = max_finder(df, cols, label_row).T
        print(month_maxes.shape)
#        print(month_maxes)

        month_maxes.insert(0, 'year', label_row['year'], allow_duplicates=True)
        
        month_maxes.insert(1, 'month', label_row['month'], allow_duplicates=True)
        
        month_maxes.insert(2, 'month_string', label_row['filename'], allow_duplicates=True)
#        print(month_maxes.shape)
#        print(month_maxes) # Okay, this works, up to here, so we have to find a way to add this to a larger dataframe - and correctly.
        monthly_series = month_list.append(month_maxes)
#        print(monthly_series)
        
        i = i + 1
        
    else:
        print(month_list)
        print(len(month_list))
        final_df=pd.concat(month_list, axis=1)
        print(final_df)
        return(final_df) # Made string to simplify reading for testing

"""
MAIN
"""
# A placeholder DataFrame
month_df = pd.DataFrame()

# List of all the filepaths that will be parsed.
filepath_list= input_pathbuilder(directory_list, source_filepath) 
# This is a global variable declaration, which I normally wouldn't want to put here but it needs to go after the function definitions.


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



#labels = label_sep(month_df, 0)
#print(labels)

# This is going to get the max for every month and make a file out of it.
# It should probably also remove the bad rows first
#print(month_df)
#print(label_sep(month_df, 0))
final = ozone_parser(df_set, month_df)





final.to_csv(output_filename)

"""
Need to clean out the bad rows. Then error check, then start getting the histograms going.
"""