# -*- coding: utf-8 -*-
"""
Created on Sat May 28 21:26:20 2022

@author: Ghost
"""


"""
Libraries
"""

import os
import time
import datetime
import math
import string
import numpy as np
import csv
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

# Now we are starting to define some functions. The dependencies are all screwy here and some of this could probably be rearranged, but I'm mostly leaving it for now.

def find_dir():
    # Finds and navigates to the correct directory for the data.        
    os.getcwd()
    os.chdir('D:\\#PERSONAL\\#STEDWARDS\\#Summer2022Research\\') 

# Start of the use of the open file.
with open('D:\\#PERSONAL\\#STEDWARDS\\#Summer2022Research\\ozone_isoheight_2010-2020.txt', 'r') as inputfile:
# Some global variables start to be defined          

          
# Now we are going to try to visualize some of the data, and clean it, with whichever comes fastest taking priority.
    ozone_graph = [[]]

#          ozone_array = np.loadtxt(inputfile, delimiter=",")
    
    inputfile_read = csv.reader(inputfile)
# Trying this with pandas instead of csv now
#    inputfile_read = pandas.read_csv(inputfile, sep=",")
# Should load the input file in as an array
    ozone_array = list(inputfile_read)

    months_choices = []
    for i in range(1,13):
        months_choices.append((datetime.date(2009, i, i).strftime('%B')))

    years_choices = []
    for i in range(0,11):
        years_choices.append(i)
    
    month_date = []
    for i in range(5,117):
        month_date.append(str(months_choices[i % 12] + ' ' + str(2010 + years_choices[math.floor(i * 1/12)])))                 

#    print(ozone_array)
    
# Now we have printed the 1D array, we want to use numpy functions to turn the 1d array of lists into a 2d array.
    ozone_2d = np.array(ozone_array)
    ozone_2dnewrows = ozone_2d.reshape(5337,1)
    ozone_df = pd.DataFrame(data=ozone_2dnewrows)

# Sends the DataFrame to csv format
def makecsv(name):
    name.to_csv('changeme.csv')
    
"""
Declaration of Global Variables
"""
    
safe_sites = ['C1_2','C8_2','C15_3','C26_2','C35_1','C45_1','C53_1','C78_1','C84_1','C403_3','C405_1','C406_1','C408_2','C409_2','C410_1','C416_1','C603_1','C603_2','C603_3','C617_1','C620_1','C1015_1','C1016_1','C1034_1']
slice_locations = (0,49,98,148,199,250,301,352,403,454,505,607,658,708,758,809,
                858,907,957,1008,1059,1110,1160,1210,1261,1311,1361,1409,1457,
                1505,1553,1601,1649,1697,1743,1789,1836,1883,1930,1978,2025,
                2072,2119,2166,2213,2261,2309,2357,2405,2456,2507,2558,2609,
                2710,2761,2812,2863,2914,2965,3016,3067,3118,3169,3219,3270,
                3321,3371,3421,3471,3522,3772,3820,3866,3913,3960,4005,4053,
                4099,4145,4190,4235,4280,4324,4369,4412,4456,4495,4536,4579,
                4622,4665,4707,4750,4793,4836,4879,4920,4959,4998,5036,5075,
                5118,5160,5203,5246,5292)
safe_siteID = []
sites_good = []
instr_good = []
rows_good = []
safesite_final = np.asarray(safe_siteID)  
ozone_dflist_good = []
multi_ozone_index = pd.MultiIndex.from_product([sites_good, month_date])
final_df = [] 


# Function: want to print an item at a given slice location
def showitem(x):
    print(ozone_df[0][x])
    
def showarr(x,y):
    print(ozone_df[0][x + 1])
    print(ozone_df[0][x + 4])
    print(ozone_df[0][y-2])

# For refactoring before showarr to make it take two args which are the beginning and end of the month slice in question
# This seems to work okay.
def get_slicestrt(i):
    return(slice_locations[i])
    
def get_sliceend(i):
    return(slice_locations[i + 1])
    
    
"""    
x + 1 == list of column headers
x + 4 == first data site for the month
y - 2 == last data site for the month
"""
    
def min_arr(x,y):
    arr = []
    arr.append(ozone_df[0][x + 1])
    i = (x + 4)
    while i < (y - 2):
        arr.append(ozone_df[0][i])    
        i = i + 1
    print(arr)
    return(arr)
    
    
def stripped_month_arr():
    
    i = 0
    while i < 105:
        a = get_slicestrt(i)
        b = get_sliceend(i)
        print(min_arr(a,b))
        i = i + 1

# Now must create a function that loops this with get_slicestrt, get_cliceend for each of all the months.
# Should take one integer as an argument.
# Needs a for loop iterating through the months, indexed by the slice locations.    
    
    
# This function doesn't work yet. Don't let yourself be confused about what it means until it does.
# The goal is to iterate through the months and generate a rectangular array for each one.
def arr_loop(i):
    ozone_df[slice_locations[i]]
    final_df.append(min_arr(get_slicestrt, get_sliceend))
    
    
"""
Test Section     
This is for print statements, etc. for running diagnostics and QA on the functions. Expect much of this to be commented out.
"""
min_arr(0,49)

stripped_month_arr()
print(len(slice_locations))
