# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 05:23:53 2022

@author: Ghost
"""

import pandas as pd
import numpy as np
import os
import math
import string
import csv
import matplotlib.pyplot as plt
import ast

"""
CONFIG
"""
source_filepath = "D:\\#PERSONAL\\#STEDWARDS\\#Summer2022Research\\SOM_cluster_augmented_2.csv"


pd.options.display.width = 0
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)



"""
GLOBAL VARIABLES
"""

"""
FUNCTION DEFINITIONS
"""
def histo_builder(df):
    return(True)


"""
MAIN FUNCTION CALLS
"""
with open(source_filepath) as source:
    data = pd.read_csv(source_filepath)
    print("Hello World")
    print(data)
    data = data.iloc[: , :-1]
    print(data)
    data.drop(data.tail(1).index, inplace = True)
    print(data)
    
    print(data.describe())
    
    plt.hist(data['max D8HO'])


"""
FILE OUTPUT
"""