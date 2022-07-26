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
import matplotlib.animation as animation
import matplotlib as mpl
import ast

"""
CONFIG
"""
ozone_filepath = r"D:\#PERSONAL\#STEDWARDS\#Summer2022Research\SOM_cluster_AUGMENTED3_july19.csv"
windrun_filepath = r"D:\#PERSONAL\#STEDWARDS\#Summer2022Research\data_210726.txt"
moody_wind_filepath = r"D:\#PERSONAL\#STEDWARDS\#Summer2022Research\wind_data_2010_2019_MOOT_C695.csv"
global_output_path = r"D:\#PERSONAL\#STEDWARDS\#Summer2022Research\scripts\file_outputs\yearoveryear_histograms"

pd.options.display.width = 0
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)



"""
GLOBAL VARIABLES
"""
#toplayer = mpl.figure.Figure()

"""
FUNCTION DEFINITIONS
"""


def exceedance_counter(df, time_unit):
    # Takes a dataframe and period of time and returns number and percentage of exceedance days graphed on the screen, for that unit of time
    df.groupby(by="cluster", axis =1, dropna="True")
#    print(df.index)
#    print(df.columns)
    maxes = df["maximum"]
#    print(maxes)
    exceedance = maxes.ge(71)
#    print(exceedance)
    masked = df[exceedance]
#    print(masked)
#    print(len(masked))
#    print(masked["maximum"])
   

def histo_builder(df, unit, graph_id, print_flag, output_path, output_prefix):
    # Takes a dataframe and returns a matplotlib histogram tuned to the output I want
    fig, ax = plt.subplots(1,1, sharex=True,sharey=True)
    bins = np.linspace(1,141,15)
    plt.xlim(0,140)
    plt.ylim(0, 50)
    hist = plt.hist(df["maximum"], bins=bins, histtype="barstacked", align="mid", rwidth=.92, label="maximum daily 8 hour ozone")
    dropped = df.dropna(axis=0, how="any") # Think I need dropna or ge rather than gt
    
    plt.axvline(x=71, color="red", linestyle="dashed")
    plt.title("Houston Area Ozone Levels by " + unit + ": " + str(graph_id), family="sans-serif")
    plt.xlabel("Maximum Daily 8 Hour Ozone (ppb)", family="sans-serif")
    plt.xticks(np.arange(0,140,10))
    plt.xticks(fontsize=11)
    plt.yticks(fontsize=11)
    plt.ylabel("Number of Days in Sample", family="sans=serif")
    plt.grid(True)
    plt.show()
    output_path_wname = str(output_path) + str(output_prefix) + str(unit) + str(graph_id)
    fig.savefig(output_path_wname, format="pdf")
    return(True)

def time_separator(df, time_unit):
    grouped = df.groupby(by=time_unit, as_index=True, sort=True, group_keys=True)
    print(grouped)
    print(len(grouped))
    print(grouped.max())
    return(True)

def histo_builder_deprecated(df, x, y):
#    axes = mpl.axes.Axes(fig=figure, rect=[0,0,5,5], xlim=(0,120), ylim=(0,50))
# Maybe ready to be deprecated
    hist = df.hist(column="maximum", figsize=(6,5), bins=[0,10,20,30,40,50,60,70,80,90,100,120], legend = True, xlabelsize=10, ylabelsize=10)

    return(hist)

def cluster_byclusterplotter(df):
    i = 0
    while i < 16:
        cluster = df.loc[df['cluster'] == i]
        graph = histo_builder(cluster, "Cluster", i)
        plt.savefig("foo.pdf")
        i = i + 1
    return(True)

def site_plotter(df):
    return(True)

def year_overyearplotter(df):
    i = 2010
    while i < 2020:
        year = df.loc[df['year'] == i]
        histo_builder(year, "Year", i, True, global_output_path, "year_over_year")
        i = i + 1
    return(True)

def month_bymonthplotter(df):
    i = 6
    while i < 10:
        month = df.loc[df['month'] == i]
        histo_builder(month, "Month", i)
        i = i + 1
    return(True)


"""
MAIN FUNCTION CALLS
"""
with open(ozone_filepath) as ozone:
    data = pd.read_csv(ozone_filepath)
#    print("Hello World")
#    print(data)
#    print(data.keys())
#    print(data.describe())
    data.groupby(by="cluster")
#    print(data)
#    print(data.describe())
    
#    print(data.index)
#    print(data.columns)
    
#    data.hist(column = 'datestring', by = 'cluster')
print("first by cluster")
#cluster_plotter(data)
print("now the months")
#month_bymonthplotter(data)
print("and finally years")
year_overyearplotter(data)
"""
with open(windrun_filepath) as windrun:
    windrun_data = pd.read_csv(windrun_filepath, delim_whitespace=True)
    print(windrun_data)
    print(windrun_data.index)
    print(windrun_data.describe())
    
with open(moody_wind_filepath) as moody_wind:
    moody_data = pd.read_csv(moody_wind_filepath)
    print(moody_data)
    print(moody_data.describe())
"""


#improved_hist(data)
    
exceedance_counter(data, "year")

"""
time_separator(data, "month")
time_separator(data, "year")
time_separator(data, "cluster")
time_separator(data, "site")
"""

#cluster_plotter(data)
"""    
    plt.text(2, 4, "r2_cell", size=12, ha="center", va="center",
    bbox=dict(boxstyle="round",  facecolor='blue', alpha=0.3) )
"""

"""
FILE OUTPUT
"""