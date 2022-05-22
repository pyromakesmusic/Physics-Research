# -*- coding: utf-8 -*-
"""
Made to cross-reference data in reading a .csv file with a list of known good data collection sites
to copy the stripped data to a second, cleaner file.
"""

# Package importations, blah blah blah

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
"""
"""
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
    ozone_2d49rows = ozone_2d.reshape(9,593)
    ozone_df = pd.DataFrame(data=ozone_2d49rows)

# Sends the DataFrame to csv format
def makecsv(name):
    name.to_csv(str(name) + '.csv')
    
# The function below for printing the tables has proven useful. Probably need to refactor it and place it elsewhere.
                           #columns=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49])
#    print(ozone_2d)
#    for row in ozone_2d49rows:
#        print('%s'%row)

# Just trying to construct a loop here to display only the parts of these strings stripped of the underscore and everything after.
safe_sites = ['C1_2','C8_2','C15_3','C26_2','C35_1','C45_1','C53_1','C78_1','C84_1','C403_3','C405_1','C406_1','C408_2','C409_2','C410_1','C416_1','C603_1','C603_2','C603_3','C617_1','C620_1','C1015_1','C1016_1','C1034_1']
safe_siteID = []
sites_good = []
instr_good = []
rows_good = []
def sitename_strip():
    i = 0
    for i in range(0, len(safe_sites)):
        safe_siteID.append(i)
        safe_sitestrp = safe_sites[i].partition('_')
        safe_siteID[i] = safe_sitestrp
        i = i + 1 
       
# Some function callls for testing.
        
#print(safe_siteID)
#print(len(safe_sites))
#print(len(safe_siteID))
def loc_slice(x):
    i = 0
    current_row = []
    row_intersect = []
    while i < 124:
        current_row = ozone_2d[i]
        print(current_row)
        row_intersect = np.in1d(current_row, safe_sites) 
        if  any(row_intersect) == True:
            print(row_intersect)
            safe_siteID.append(current_row)
            row_intersect= []
            i = i + 1
        else:
            row_intersect = []
            i = i + 1

def sitestrp():
    i = 0
    while i < len(safesite_final):
        sites_good.append(safesite_final[i, 0])
        instr_good.append(safesite_final[i, 2])
        i = i + 1    
"""        
        print(sites_good)
        print(instr_good)        
"""



# This is supposed to be the start of a function to strip out all the necessary rows. Will need to perform some Boolean logic concatenation to get the total sum of conditions. Some ands and ors.

def tceqstrp():
    i = 0
    while i < 2:
#    while i < ozone_df.length():
#        print(ozone_df[i, 1])
#        if np.in1d(ozone_df[i, 1], sites_good).empty() == False:
#            rows_good.append(ozone_df[i])
        ozone_df
        i = i + 1
    
#    print(rows_good)
    
sitename_strip()
safesite_final = np.asarray(safe_siteID)  
sitestrp()          
#print(safe_siteID)
#print(safesite_final)
# I've done it! I've isolated the site identifiers from their components!
# print(safesite_final[:, 0])
#print(sites_good)
#print(instr_good)
tceqstrp()
# The function call
# loc_slice(2)

# This next function is garbage. Zero points.
"""
def site_pop():
    i = 1
    while i < len(safe_sites) + 1:
            if i == safe_sites.index(safe_sites[i]):
                safe_siteID.append(safe_sites[i])
            else:
                i = i + 1
    print(safe_sites)  
    
site_pop()
"""

"""
for i in safe_sites:
    print(i)
"""

    




# Prints a list of the months in the study, and then the number of elements in the list.
    
# print(months_choices)
# print(years_choices)
# print(month_date)
# print(len(month_date))


"""
# This runs in garbage time. I am saving the world's electricity system from having to pay for it. Genuinely have to consider optimization for this subproblem.
for month in month_date:
    for row in ozone_2d:
        if row == month:
            print(row[month])
        else: print("x")
"""        
# we want to parse the names with underscores into an array with three columns: input string, site ID, site instrumentID#
# for i in safe_sites:
#   break
# for row in inputfile:
#    break

"""
Okay, now we want a function where the years go up vertically from 2010 to 2019, the months and days all lie along the y axis, and the x axis is max daily 8-hour ozone.
"""
def make_plot():
    x = np.linspace(start=1, stop=12,num=12)
    y = np.linspace(start=2010, stop=2019, num=12)
    z = np.linspace(start=-10, stop=150, num=15)
    fig = mpl.pyplot.figure()
    pyplot_2 = fig.plot3D(x,y,z, projection='3D')

    plt.axes(projection='3d')
"""
    x = np.linspace(0, 2 *np.pi, 200)
    y = np.sin(x)
    fig, ax = plt.subplots()
    ax.plot(x,y)
    plt.show()
"""

"""
Let's list all the months in the data sample.
"""

#    for i in ozone_2d:
#       print(ozone_2d[i])
#   print(ozone_2d)
    
#   for i in range(len(ozone_2d)):
#       print(ozone_2d[i])
    
 
"""
 Will need to use modular arithmetic for this next bit.
 Modulus is either 48, 49, or 50. Number of rows in each
 copy-paste of data. So when our index modulo that value
 is certain numbers, we want the row to be stricken from the record.
"""

# Commenting this out briefly, since I have roughly the same thing being defined in a function definition up top.
"""
x = 0
while x < ozone_df.count():
    print(ozone_df[i, 0])
    x = x + 1

     
"""

"""
We need to find ways to identify and label the different sets of cells.
A few possible identifiers for cells: month, list of headings, site title, instrument identifier, regulated or non-regulatory, blank, dates, max daily ozone.
"""
# Now let's give the user a chance to provide input in the form of  two integers which should be the index of some cell in the array so that we can attempt to find a pattern.
"""
def index_check():
    while True:
        try:
            first = int(input('What is the first index of your desired cell? '))
            break
        except:
            print('That is invalid input.')
    while True:
        try:
            second = int(input('What is the second index of your desired cell? '))
            break
        except:
            print('That is invalid input.')
    
    print(ozone_2d[first][second])
"""
