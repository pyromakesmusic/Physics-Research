# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 08:12:18 2022

@author: Ghost
"""


"""
CONFIGURATION
"""
filepath = 'D:\\#PERSONAL\\#STEDWARDS\\#Summer2022Research\\'
# filepath = r'C:\Users\Pyro\Documents\Summer2022Research\Summer-2022-Research'



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

def lit_eval(data, num):
    return(ast.literal_eval(list(data[num])))

"""
4.MAIN
"""
def getrow(rownum):
    return(ozone_list[rownum])

def rowlength(rownum):
    return(len(ozone_list[rownum]))

def rowtype(rownum):
    return(type(ozone_list[rownum]))




os.chdir(filepath)
         
with open('onecolumn_md8ho.csv') as ozone_column:
    print(ozone_column)
    ozone_array = csv.reader(ozone_column)
    ozone_list = list(ozone_array)
#    print(ozone_list)
#    print(ozone_list[1]) # The data that needs to be parsed starts at index 1

#    print(len(ozone_list))
# The ozone_list is 1191 rows long

print(getrow(0))
print(getrow(1))

print(rowtype(0))
print(rowtype(1))

null_cell = getrow(0)
first_cell = getrow(1)

print(null_cell[0])
print(first_cell[0])

print(type(null_cell[0]))
print(type(first_cell[0]))


"""        
    i = 0
    while i < 1169:
        print()
"""

"""

# This is a loop, so it's going to survive being commented out.
    
    i = 1 # It's 1 because that's where the important data starts
    max_length = len(ozone_list)
    print(type(ozone_list))
    while i < 500:
        print(ozone_list[i])
        print(type(ozone_list[i]))
        print(ozone_list[i][0])
        i = i + 1
"""



"""
5.UNIT TESTING
"""