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



"""
3. Function Definition
"""



"""
4. Main

"""
# Navigating to the right folder

os.chdir('D:\\#PERSONAL\\#STEDWARDS\\#Summer2022Research\\')
         
with open('som_cluster_10yr_700hpa_00utc.csv') as som_file:
              
    som_fileread = csv.reader(som_file)
    print(som_fileread)  
    daily_som = list(som_fileread)
    print(daily_som)
    daily_somdf = pd.DataFrame(data = daily_som)
"""
5. Unit Tests
"""
print(os.getcwd())