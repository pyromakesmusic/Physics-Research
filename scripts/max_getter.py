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
import ast


"""
2. Variable Declaration
"""
daily_somdf = False
some_fileread = False
daily_som = False

month_year = ['June 2010', 'July 2010', 'August 2010', 'September 2010',
              'October 2010', 'November 2010', 'December 2010', 'January 2011',
              'February 2011', 'March 2011', 'April 2011', 'May 2011',
              'June 2011', 'July 2011', 'August 2011', 'September 2011',
              'October 2011', 'November 2011', 'December 2011', 'January 2012',
              'February 2012', 'March 2012', 'April 2012', 'May 2012',
              'June 2012', 'July 2012', 'August 2012', 'September 2012',
              'October 2012', 'November 2012', 'December 2012', 'January 2013',
              'February 2013', 'March 2013', 'April 2013', 'May 2013',
              'June 2013', 'July 2013', 'August 2013', 'September 2013',
              'October 2013', 'November 2013', 'December 2013', 'January 2014',
              'February 2014', 'March 2014', 'April 2014', 'May 2014',
              'June 2014', 'July 2014', 'August 2014', 'September 2014',
              'October 2014', 'November 2014', 'December 2014', 'January 2015',
              'February 2015', 'March 2015', 'April 2015', 'May 2015',
              'June 2015', 'July 2015', 'August 2015', 'September 2015',
              'October 2015', 'November 2015', 'December 2015', 'January 2016',
              'February 2016', 'March 2016', 'April 2016', 'May 2016',
              'June 2016', 'July 2016', 'August 2016', 'September 2016',
              'October 2016', 'November 2016', 'December 2016', 'January 2017',
              'February 2017', 'March 2017', 'April 2017', 'May 2017',
              'June 2017', 'July 2017', 'August 2017', 'September 2017',
              'October 2017', 'November 2017', 'December 2017', 'January 2018',
              'February 2018', 'March 2018', 'April 2018', 'May 2018',
              'June 2018', 'July 2018', 'August 2018', 'September 2018',
              'October 2018', 'November 2018', 'December 2018', 'January 2019',
              'February 2019', 'March 2019', 'April 2019', 'May 2019',
              'June 2019', 'July 2019', 'August 2019', 'September 2019']

threedee_df = []


"""
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
New function. We've found we need to use ast.literal_eval() on each of these matrix entries to get them to read as a list.
"""
def append_test():
    month = 0
    row = 1
    row_aslist = False
    month_sample_length = len(ast.literal_eval(daily_ozonedf[month][row]))
    # Currently 29 is a magic number. I think it needs to be 34, the number of rows in this table
    print(month_sample_length)
    while row < month_sample_length:
        row_aslist = ast.literal_eval(daily_ozonedf[month][row])
        threedee_df.append(row_aslist)
        row = row + 1
    
# Test function call
    

print(threedee_df)
row_aslist = ast.literal_eval(daily_ozonedf[0])
print(row_aslist)


"""
Each x in this function is a month. This returns all of the data columns, plus the headers, for the month.
"""
def max_grabber(x):
# Need to find out what i means
    i = 0    
    while i < 29:
        # Need to partition this into a list of strings
        evidence = ast.literal_eval(daily_ozone[x][i])


        print(evidence[0])
        i = i + 1
        


"""
Okay, now we know the dates for the SOM excel file appear in column index 1 and start at row 1.
"""