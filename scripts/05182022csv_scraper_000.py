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
    name.to_csv(str(name) + '.csv')
    
# The function below for printing the tables has proven useful. Probably need to refactor it and place it elsewhere.
                           #columns=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49])
#    print(ozone_2d)
#    for row in ozone_2d49rows:
#        print('%s'%row)

# Just trying to construct a loop here to display only the parts of these strings stripped of the underscore and everything after.
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
ozone_dflist_good = [[]]
multi_ozone_index = pd.MultiIndex.from_product([sites_good, month_date])
final_df = [[]] 
# I think some of these variables are essentially duplicates and can be eliminated. We will see.

# We need to figure out what the heck this function does. I think it checks if the current row intersects with the good sites.



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
    
        print(sites_good)
        print(instr_good)        


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

def rowcount():
    i = 0
    month_count = 0
    slice_index = []
    print(month_date[month_count])
    print(ozone_df[i][0][0])
    while i < 5337:
        if ozone_df[i][0][0] == month_date[month_count]:
            print(month_date[month_count])
            print(ozone_df[i][0][0])
            slice_index.append(i)
            month_count = month_count + 1
            i = i + 1
        else:
            print(i)
            i = i + 1
#        print(slice_index)
            
# May 25 0418 AM this is currently where i am at
   

     
def year_mod12(x):
    return x % 12


# This is the most important function there is
def master_loop():
    row_count = 0
    month_count = 0
    year_count = 2010
    print(row_count)
    print(month_date[month_count])
    print(year_count)
    
master_loop()

# print(year_mod12(15))

def df_create():
    i = 1 # i is  the row counter
    year_counter = 2010
    month_counter = 0
    while i < 5337:
        
        if ozone_df[0][i][0] == month_date[month_counter]:
            print(ozone_df[0][i][0])
            final_df[year_counter][i].append(ozone_df[month_counter])
            if month_counter % 12 == 0:
                year_counter = year_counter + 1
                i = i + 1    
            else:
                    i = i + 1
    else:
        print('This is a test.')
        i = i + 1
        
        
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
    
#   print(ozone_2d[first][second])
            
            
def row_scraper(x,p,q,r):  
#    print(month_date)
    print(ozone_df[0][0])
    row_intersect = []
    month_counter = 0
    year_counter = 2010
    ozone_df_good = []
    
    i = 0
    while i < x:
        if np.intersect1d(ozone_df[0][i][0], month_date) == number:
            row_intersect.append(np.intersect1d(ozone_df[0][i], month_date[month_counter]))
            month_counter = month_counter + 1
            if month_counter % 12 == 6:
                year_counter == year_counter + 1
                i = i + 1
            else:
                i = i + 1
        elif np.intersect1d(ozone_df[0][i][q], site_good) == number and np.intersect1d(ozone_df[0][i][r], instr_good) == number:
            i = i + 1
        else:
            i = i + 1
            
def site_pop():
    i = 1
    while i < len(safe_sites) + 1:
            if i == safe_sites.index(safe_sites[i]):
                safe_siteID.append(safe_sites[i])
            else:
                i = i + 1
    print(safe_sites)  
    
    
# Okay, now we want a function where the years go up vertically from 2010 to 2019, the months and days all lie along the y axis, and the x axis is max daily 8-hour ozone.


# This is not currently needed.


"""
def make_plot():
    x = np.linspace(start=1, stop=12,num=12)
    y = np.linspace(start=2010, stop=2019, num=12)
    z = np.linspace(start=-10, stop=150, num=15)
    fig = mpl.pyplot.figure()
    pyplot_2 = fig.plot3D(x,y,z, projection='3D')

    plt.axes(projection='3d')


    x = np.linspace(0, 2 *np.pi, 200)
    y = np.sin(x)
    fig, ax = plt.subplots()
    ax.plot(x,y)
    plt.show()
    

site_pop()
   

row_scraper(800,0,1,2)
"""    
df_create()



# print(month_date)
# print(len(month_date))
# month_dfinput()
#print(ozone_dflist_good)
# Some function calls for testing.
        
#print(safe_siteID)
#print(len(safe_sites))
#print(len(safe_siteID))


# Don't forget to call the fucking function!!!
# rowcount()
    
#asitename_strip()




#sitestrp()          
#print(safe_siteID)
#print(safesite_final)
# I've done it! I've isolated the site identifiers from their components!
#print(safesite_final[:, 0])
# Commmenting these next print statements out because I know that they work.
#print(sites_good)
#print(instr_good) 

#print(repr(ozone_df[0][0]))


# You're gonna need to move this function later.
#print(month_date[0])
# gonna do a while/for loop test just to see if stuff works

# Below me is the list of all the slcing locations for this sequence of matrices.



#montharray_slicer()






#print(multi_ozone_index[1][1])
    
"""

"""
     
# What if this worked....
#print(np.intersect1d(ozone_df, month_date))



#ef git_gud(): #rows. get good rows.
#   x = int(0)
#   i = int(0)
#   while i < int(5337):
#       
#       if np.intersect1d(ozone_df[i], month_date[x]) != False:
#           print('do something very embarassing')
#           i = i + 1
#       else:
#          print('do not do the embarrassing thing that you might otherwise have done')
#           i = i + 1       

  
#git_gud()
#for num, name in np.intersect1d(ozone_df, month_date, return_indices = True)
#rint("President{}}:{}".format(num, name))

#kay, so this all worked, and we need to do something and take advantage of this now.
#f a conditional statement is true, we want to:
#   add the contents of a particular cell OR row to a particular indexed list indexed in a manner useful for our purposes. Requirements may include:
#       - assign month to a PKI
#       - assign a particular cell/list/site+instr+month to particular KPI
#       - index the days in a comparable way across years, synoptic regimes
        

     




"""
i = 0
slice_line = []
list_of_months = []
good_samples = []
necessary_rows = []
month_counter = 0
row_counter = 0
while i < 5336:
    if np.in1d(ozone_df[i][0], month_date) == True:
        slice_line.append(i)
        month_counter = month_counter + 1
        row_counter = row_counter + 1
        i = i + 1
    elif (np.in1d(ozone_df[i][1], sites_good) == True) and (np.in1d(ozone_df[i][2] == True)):
        row_counter = row_counter + 1
        i = i + 1
    else row_counter = row_counter + 1
        i = i + !
"""

     
# print(slice_line)
# print(month_counter)
# print(row_counter)
        
# tceqstrp()
# The function call
# loc_slice(2)

# This next function is garbage. Zero points.

"""




for i in safe_sites:
    print(i)
"""

    




# Prints a list of the months in the study, and then the number of elements in the list.
    
# print(months_choices)
# print(years_choices)
# print(month_date)
# print(len(month_date))



# This runs in garbage time. I am saving the world's electricity system from having to pay for it. Genuinely have to consider optimization for this subproblem.

"""
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


#Let's list all the months in the data sample.


#    for i in ozone_2d:
#       print(ozone_2d[i])
#   print(ozone_2d)
    
#   for i in range(len(ozone_2d)):
#       print(ozone_2d[i])
    
 
"""
# Will need to use modular arithmetic for this next bit.
# Modulus is either 48, 49, or 50. Number of rows in each
# copy-paste of data. So when our index modulo that value
# is certain numbers, we want the row to be stricken from the record.
 
"""
"""

# Commenting this out briefly, since I have roughly the same thing being defined in a function definition up top.

"""


x = 0
while x < ozone_df.count():
    print(ozone_df[i, 0])
    x = x + 1
"""
     


"""



"""
"""
We need to find ways to identify and label the different sets of cells.
A few possible identifiers for cells: month, list of headings, site title, instrument identifier, regulated or non-regulatory, blank, dates, max daily ozone.
"""
"""


# Now let's give the user a chance to provide input in the form of  two integers which should be the index of some cell in the array so that we can attempt to find a pattern.
"""

"""

def sitename_strip():
    i = 0
    for i in range(0, len(safe_sites)):
        safe_siteID.append(i)
        safe_sitestrp = safe_sites[i].partition('_')
        safe_siteID[i] = safe_sitestrp
        i = i + 1 
       
        
def montharray_slicer():
    i = 0
    while i < len(slice_locations):
#        print(ozone_df[0][slice_locations[i]])
        i = i + 1

def month_dfinput():
    i = 0
    while i < len(month_date):
        ozone_dflist_good.append(month_date[i])
        i = i + 1
#        print(ozone_dflist_good)
    print(ozone_dflist_good)
#    print(ozone_dflist_good[0][0])
"""