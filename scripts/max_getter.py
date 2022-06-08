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
from calendar import monthrange
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
daily_som_deprecated = False

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
    
"""
row_aslist = ast.literal_eval(daily_ozonedf[0][0])
print(row_aslist)
print(len(row_aslist))
"""
def column_tryer(x):
    # x should be the column that we check all the values in for a month
    # i is the row within the month to be iterated through
    i = 0
    month = 0
    month_aslist = ast.literal_eval(daily_ozonedf[month][x])
    print(len(month_aslist))
    while i < len(month_aslist):
        threedee_df.append(month_aslist[i])
        i = i + 1
        
#column_tryer(0)
#print(threedee_df)

# print(threedee_df[4])
# Index 4 is the location of the first date
# First, let's call a date for each date in the SOM file.


"""
Here we make a function that returns the number of days in each month, and the 
year.
"""
def month_days(i):
    # I don't understand why using 5 instead of 6 here works for both the year 
    # and the month when the calendar starts in June, but I'm just gonna leave
    # it.
    # i should start at 0 in the loop whenever this function is called
    year = 2010 + math.floor((5 + i) * 1/12)
    month = ((5 + i) % 12) + 1
    dayrange = monthrange(year, month)[1]
    return_list = [dayrange, i, year, month]
    
# don't need this print statement for now        
#        print("The number of days in " + str(month_year[i]) + " is " + str(monthrange(year, month)[1]))
#        i = i + 1
# also don't need the iterator math since that will be happening in the parent loop
#    month = (((month + 1) % 12) + 1)
#    year = year + (i % 12)
    return (return_list)


def month_lengthtest():
    i = 0
    while i < 112:
        print(month_days(i))
        i = i + 1

"""
Each x in this function is a month. This returns all of the data columns, plus 
the headers, for the month.

I didn't explain this well. Each x should be a new month. each c should be a 
new day. We want to modify the function to create an internal list per day and 
return the max each day. Right now this gives me a list for each site that 
extends through the sample. I need it to compare samples from different sites 
for the same day. May need to make a subroutine returning the number of sites 
for each day.

Okay, now it gives the daily maximum. I need this to work given a particular 
date in the SOM file, and I also need it to return the site as a separate 
argument. Forcing int in the print/try loop seems to have made something work 
correctly that I don't really understand. Look there first when debugging.

"""

"""
So then, if I'm trying to return the site at which the daily max occurs, we do 
something with the index corresponding to the site_row while shifting the 
column backwards to the one that says site.
"""

def df_maxer(x, c, t, m):
# i is something else. i is the row in terms of which monitoring site.    
# c should be a column constant, after the first few columns it denotes the day
# what is x? no, x is the row+month. 
# m is the current month.
    

    daily_max = []
    date = t - 3
    month_name = str(month_year[m])
    i = 1    
    while i < 34:
        # Need to partition this into a list of strings
        try:
            evidence = ast.literal_eval(daily_ozonedf[i][x])
#            print(int(evidence[c]))
            daily_max.append(int(evidence[c]))
            i = i + 1
        except ValueError:
#            print("ValueError")
            i = i + 1
        except SyntaxError:
#            print("SyntaxError")
            i = i + 1

#    print('The daily max is ' + str(max(daily_max)))
    try:
        max_ozone = (max(daily_max))
        max_index = daily_max.index(max_ozone)
#    print(max_ozone)
#    print(max_index)
#        evidence = ast.literal_eval(daily_ozonedf[max_index][1])
#        site = str(evidence[1])
        month_name = str(month_year[m]) 
        max_name = daily_ozonedf[max_index][1]
        evidence = ast.literal_eval(max_name)
    except:
        print("hooty hoo")
#        print(evidence[1])
#        print(len(evidence))
    finally:
        site_name = str(evidence[1])
#    print("Max O3 on: " + str(date) + " " + month_name + ": " 
#                   + str(max_ozone) + " ppb; site: " + site)
    # all of these should be named variables in the function
    
    return(date, month_name, max_ozone, site_name)
        
# Good, now this correctly prints the same column in each row meaning month
    
"""
now we need to write a function that calls df_maxer with the correct arguments for each date in the excel file.
think we need to look at the daily_function() function. probably add some args.
"""
# print(len(daily_somdf))
# This returns 1221, so 1221 rows in the file to match to something or N/A


"""
Note - the second argument, the date, should be 3 more than the actual numeric day of the month. We will use this to loop it somehow.

""" 
# 4 here gives me the first day of every month
# 31 gives me the 28th, what happens at out of bounds error?
# I currently have 0 as x, what does that do?

"""
Okay, now we know the dates for the SOM excel file appear in column index 1 and start at row 1.
Going to try to turn this in to a primary function body with recursive calls inside.
"""

def daily_function():
    i = 1
    while i < 1221:
        current_date = daily_somdf[1][i]
        current_month = daily_somdf[3][i]
        print(datetime.datetime.strptime(current_date, "%Y-%m-%d"))
        print(current_month)
        i = i + 1
    return(False)
    
# Here is our function to get the list of maxes for the whole moonth using 
# daily_max function and return them as a list or something.
def month_looper(month, length, month_count):
    i = 4
    while i < length:
        print(df_maxer(month, i, i, month_count))
        i = i + 1
 
def column_creator():
    i = 0
    new_columns = []
    date = 0
    month_name = 0
    max_ozone = 0
    site = 0
    while i < 73: # at this point in time, i seems to function properly up to 
        if i in (0,1,2,3,
                 12,13,14,15,
                 24,25,26,27,
                 36,37,38,39,
                 48,49,50,51,
                 60,61,62,63,
                 72,73,74,75, # commented out 73, list index out of range
                 84,85,86,87,
                 96,97,98,99,
                 108,109,110,111):
            try:
                date, month_name, max_ozone, site = (month_looper(i, 33, i))
                # 34 is the highest list index that is in range for middle term of month_looper
                columns_list = [date, month_name, max_ozone, site]
                new_columns.append(columns_list)
                i = i + 1
            except:
#                print(month_looper(i, 34, i))
#                print(i)
                i = i + 1
            finally:
                print(new_columns)
        else:
            i = i + 1
    return(new_columns)

       
"""
4. Main

"""
# Navigating to the right folder

os.chdir('D:\\#PERSONAL\\#STEDWARDS\\#Summer2022Research\\')
         
with open('som_cluster_10yr_700hpa_00utc.csv') as som_file, open('D:\\#PERSONAL\\#STEDWARDS\\#Summer2022Research\\cleaned_data.csv') as ozone_file:
              
    som_fileread = csv.reader(som_file)
    daily_som_deprecated = list(som_fileread)
#    print(daily_som[0])
    daily_somdf = pd.DataFrame(data = daily_som_deprecated)
    
    ozone_fileread = csv.reader(ozone_file)
    daily_ozone_deprecated = list(ozone_fileread)
    daily_ozone_deprecated.pop(0)
    daily_ozonedf = pd.DataFrame(data = daily_ozone_deprecated)


    
    
"""
5. Unit Tests
"""
# newlist = month_lengthtest()
# print(daily_somdf)
#daily_function()
#month_looper(0, 34)

print(column_creator())
output_somdf = column_creator()
output_df = pd.DataFrame(data = output_somdf)
output_df.to_csv('output_columns_2010-2016.csv')

# here i is the month

# Think I wanna do something so the function appends to a list given as an arg
# at a particular index.

# Also need to check if the month and year match the month and year in the 
# daily_som file.
# print(len(daily_ozone[1]))

"""
daily_function()

print(len(daily_ozone[110]))
print(daily_ozone[0][1])
print(len(daily_ozone[0][1][1]))
print(len(daily_ozone[0][2]))


print(daily_ozone[0][2])
print(len(daily_ozone[0][2]))
"""

# daily_function()
# something about the number of NAs in the data is making this inconsistent.
# Need to append something to the list even when it is NA.
# print(df_maxer(0, 6, 0, 6))

