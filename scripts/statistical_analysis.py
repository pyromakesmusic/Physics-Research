# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 05:23:53 2022

@author: Ghost
"""
import unicodedata
import re
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
import geopandas as gpd

"""
CONFIG
"""
ozone_filepath = r"D:\#PERSONAL\#STEDWARDS\#Summer2022Research\SOM_cluster_AUGMENTED3_july19.csv"
windrun_filepath = r"D:\#PERSONAL\#STEDWARDS\#Summer2022Research\data_210726.txt"
moody_wind_filepath = r"D:\#PERSONAL\#STEDWARDS\#Summer2022Research\wind_data_2010_2019_MOOT_C695.csv"
site_coords_filepath = r"D:\#PERSONAL\#STEDWARDS\#Summer2022Research\site_coordinates.txt"
global_output_path = r"D:\#PERSONAL\#STEDWARDS\#Summer2022Research\scripts\file_outputs\yearoveryear_histograms\\"

pd.options.display.width = 0
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

mpl.rcParams['figure.dpi'] = 300



"""
GLOBAL VARIABLES
"""
#toplayer = mpl.figure.Figure()

"""
FUNCTION DEFINITIONS
"""
def slugify(value, allow_unicode=False):
    """
    Taken from https://github.com/django/django/blob/master/django/utils/text.py
    Convert to ASCII if 'allow_unicode' is False. Convert spaces or repeated
    dashes to single dashes. Remove characters that aren't alphanumerics,
    underscores, or hyphens. Convert to lowercase. Also strip leading and
    trailing whitespace, dashes, and underscores.
    """
    value = str(value)
    if allow_unicode:
        value = unicodedata.normalize('NFKC', value)
    else:
        value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore').decode('ascii')
    value = re.sub(r'[^\w\s-]', '', value.lower())
    return re.sub(r'[-\s]+', '-', value).strip('-_')

def exceedance_counter(df):
    # Takes a dataframe and period of time and returns number and percentage of exceedance days graphed on the screen, for that unit of time

    maxes = df["maximum"]
    exceedance = maxes.ge(71)
    masked = df[exceedance]
    exceedance_count = len(masked)
    sample_length = len(df)
    exceedance_ratio = exceedance_count/sample_length
    exceedance_percent = str(round(exceedance_ratio*100, 2)) + "%"
    output_string = "Exceedance Events: " + str(exceedance_count) + "/" + str(sample_length) + "\nPercentage of Sample in Exceedance: " + exceedance_percent
    return(output_string)
   
def histo_formatter():
    # Formatting for the ozone histograms
    # Change the y-axis scale here
    plt.ylim(0, 80)
    plt.xlabel("Maximum Daily 8 Hour Ozone (ppb)", family="sans-serif")
    plt.xticks(np.arange(0,150,10))
    plt.xticks(fontsize=11)
    plt.yticks(fontsize=11)
    plt.ylabel("Number of Days in Sample", family="sans=serif")
    plt.grid(True)
    plt.xlim(0,150)
    plt.axvline(x=71, color="red", linestyle="dashed")
    return(True)

def histo_builder(df, unit, graph_id, print_flag, output_path, output_prefix):
    # Takes a dataframe and returns a matplotlib histogram tuned to the output I want
    fig, ax = plt.subplots(1,1, sharex=True,sharey=True)
    bins = np.linspace(1,151,16)
   
    # Here is the histogram itself
    hist = plt.hist(df["maximum"], bins=bins, histtype="barstacked", align="mid", rwidth=.92, label="maximum daily 8 hour ozone")
    dropped = df.dropna(axis=0, how="any") # Think I need dropna or ge rather than gt
    
    
    # Mostly formatting stuff
    plt.title("Houston Area Ozone Levels by " + unit + ": " + str(graph_id), family="sans-serif")

    
    histo_formatter()
    
    text_string = exceedance_counter(df)
    props = dict(boxstyle="round", facecolor="wheat", alpha=0.5)
    
    plt.text(75, -20, text_string, size=12, ha="center", va="center",
         bbox=dict(boxstyle="round",  facecolor='white', alpha=1) )
    
    plt.show()
    output_path_wname = str(output_path) + str(output_prefix) + str(unit) + str(graph_id)
    
    # Saving the file, this should be linked to a checkbutton flag once implemented in the GUI
    fig.savefig(output_path_wname, format="pdf", bbox_inches="tight")
    
    return(True)

def lineplot_builder(df):
    fig, ax = plt.subplots(1,1, sharex=True, sharey=True)
    df.plot(x="date",y="maximum")
    plt.xticks(fontsize=7)
    print(df.columns)
    return(True)

def time_separator(df, time_unit):
    """
    At this time it is unclear what this does - I think it's supposed to feed me separated DataFrames for more granular visualization'
    """
    grouped = df.groupby(by=time_unit, as_index=True, sort=True, group_keys=True)
    print(grouped)
    print(len(grouped))
    print(grouped.max())
    return(True)

def cluster_byclusterplotter(df):
    i = 0
    while i < 16:
        cluster = df.loc[df['cluster'] == str(i)]
        print(cluster)
        graph = histo_builder(cluster, "Cluster", i,  True, global_output_path, "cluster_by_cluster")
        i = i + 1
    return(True)

def site_bysiteplotter(df):
    """
    Takes a dataframe and returns a bunch of ozone histograms split up by site.
    """
    unique_items = df["site"].unique()
    unique_items = unique_items[:-1]
    print(unique_items)
    i = 0
    while i < len(unique_items):
        site = unique_items[i]
        site_slug = slugify(site)
        site_measurements = df.loc[df["site"] == site]
        histo_builder(site_measurements, "Site", site_slug, True, global_output_path, r"site_by_site")
        i = i + 1
    print(df["site"].unique())
    return(True)

def year_overyearplotter(df):
    i = 2010
    while i < 2020:
        year = df.loc[df['year'] == i]
        histo_builder(year, "Year", i, True, global_output_path, r"year_over_year")
        i = i + 1
    return(True)

def month_bymonthplotter(df):
    i = 6
    while i < 10:
        month = df.loc[df['month'] == i]
        histo_builder(month, "Month", i,  True, global_output_path, r"month_by_month")
        i = i + 1
    return(True)


"""
MAIN FUNCTION CALLS
"""
with open(ozone_filepath) as ozone:
    data = pd.read_csv(ozone_filepath)
    print(data.describe())

#cluster_byclusterplotter(data)
print("now the months")
#month_bymonthplotter(data)
print("and finally years")
#year_overyearplotter(data)
#site_bysiteplotter(data)


#histo_builder(data, "2010-2019", "Full Sample", True, global_output_path, r"full_sample")

lineplot_builder(data)
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
with open(site_coords_filepath) as site_locations:
    siteloc_df = pd.read_csv(site_coords_filepath, sep="\t")
    print(siteloc_df)
    print(siteloc_df.describe())

#exceedance_counter(data, "year")

"""
time_separator(data, "month")
time_separator(data, "year")
time_separator(data, "cluster")
time_separator(data, "site")
"""

"""    
    plt.text(2, 4, "r2_cell", size=12, ha="center", va="center",
    bbox=dict(boxstyle="round",  facecolor='blue', alpha=0.3) )
"""

"""
FILE OUTPUT
"""