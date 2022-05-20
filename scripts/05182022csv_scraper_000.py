# -*- coding: utf-8 -*-
"""
Made to cross-reference data in reading a .csv file with a list of known good data collection sites
to copy the stripped data to a second, cleaner file.
"""
import os
import time
import numpy as np
import csv
import pandas

safe_sites = ['C1_2','C8_2','C15_3','C26_2','C35_1','C45_1','C53_1','C78_1','C84_1','C403_3','C405_1','C406_1','C408_2','C409_2','C410_1','C416_1','C603_1','C603_2','C603_3','C617_1','C620_1','C1015_1','C1016_1','C1034_1']

for i in safe_sites:
    print(i)
    
with open('D:\\#PERSONAL\\#STEDWARDS\\#Summer2022Research\\ozone_isoheight_2010-2020.txt', 'r') as inputfile:
#          ozone_array = np.loadtxt(inputfile, delimiter=",")
    
    inputfile_read = csv.reader(inputfile)
#Trying this with pandas instead of csv now
#    inputfile_read = pandas.read_csv(inputfile, sep=",")
# Should load the input file in as an array
    ozone_array = list(inputfile_read)

                 
# Finds and navigates to the correct directory for the data.
          
    os.getcwd()
    os.chdir('D:\\#PERSONAL\\#STEDWARDS\\#Summer2022Research\\') 

#    print(ozone_array)
    
# Now we have printed the 1D array, we want to use numpy functions to turn the 1d array of lists into a 2d array.
    ozone_2d = np.array(ozone_array)
 
#    for i in ozone_2d:
#       print(ozone_2d[i])
    print(ozone_2d)
    
    for i in range(len(ozone_2d)):
        print(ozone_2d[i])
        
        
"""
We need to find ways to identify and label the different sets of cells.
A few possible identifiers for cells: month, list of headings, site title, instrument identifier, regulated or non-regulatory, blank, dates, max daily ozone.
"""
# Now let's give the user a chance to provide input in the form of  two integers which should be the index of some cell in the array so that we can attempt to find a pattern.
"""
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
    
# we want to parse the names with underscores into an array with three columns: input string, site ID, site instrumentID#
#for i in safe_sites:
#   break
#for row in inputfile:
#    break
