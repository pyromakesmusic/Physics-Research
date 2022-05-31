# -*- coding: utf-8 -*-
"""
==========
MAX GETTER
==========

should take a .csv file, with a row for each month, and calculate the max ozone for each day at each data collection site.

Created on Tue May 31 03:52:47 2022

@author: Ghost
"""

"""
1. Libraries
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
from mpl_toolkits import mplot3d

"""
2. Variable Declaration
"""
daily_somdf = False
some_fileread = False
daily_som = False




months_choices = []
for i in range(1,13):
    months_choices.append((datetime.date(2009, i, i).strftime('%B')))

years_choices = []
for i in range(0,11):
    years_choices.append(i)
        
month_date = []
for i in range(5,117):
    month_date.append(str(months_choices[i % 12] + ' ' + str(2010 + years_choices[math.floor(i * 1/12)])))


"""
3. Function Definition
"""



def get_day():
    i = 1
    while i < 1221:
        current_date = daily_somdf[1][i]
        print(current_date)
        print(datetime.datetime.strptime(current_date, "%Y-%m-%d"))
        i = i + 1
    return(False)
    

"""
4. Main

"""
# Navigating to the right folder

os.chdir('D:\\#PERSONAL\\#STEDWARDS\\#Summer2022Research\\')
         
with open('som_cluster_10yr_700hpa_00utc.csv') as som_file, open('D:\\#PERSONAL\\#STEDWARDS\\#Summer2022Research\\cleaned_data.csv') as ozone_file:
              
    som_fileread = csv.reader(som_file)
    daily_som = list(som_fileread)
#    print(daily_som[0])
    daily_somdf = pd.DataFrame(data = daily_som)
    
    ozone_fileread = csv.reader(ozone_file)
    daily_ozone = list(ozone_fileread)
    daily_ozone.pop(0)
    daily_ozonedf = pd.DataFrame(data = daily_ozone)


    
    
"""
5. Unit Tests
"""

#print(len(daily_ozone[1]))

"""
get_day()

print(len(daily_ozone[110]))
print(daily_ozone[0][1])
print(len(daily_ozone[0][1][1]))
print(len(daily_ozone[0][2]))


print(daily_ozone[0][2])
print(len(daily_ozone[0][2]))
"""


"""
Each x in this function is a month. This returns all of the data columns, plus the headers, for the month.
"""
def max_grabber(x):
    i = 0    
    while i < 77:
        print(daily_ozone[x][i])
        i = i + 1
        
max_grabber(110)

"""
Okay, now we know the dates for the SOM excel file appear in column index 1 and start at row 1.
"""