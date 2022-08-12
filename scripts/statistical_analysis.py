# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 05:23:53 2022

@author: Ghost
"""
import unicodedata
import re
import pandas as pd
#import geopandas as gpd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib as mpl
import os
#import osmnx
import math

"""
CONFIG
"""
ozone_filepath = r"D:\#PERSONAL\#STEDWARDS\#Summer2022Research\SOM_cluster_AUGMENTED3_july19.csv"
windrun_filepath = r"D:\#PERSONAL\#STEDWARDS\#Summer2022Research\data_210726.txt"
moody_wind_filepath = r"D:\#PERSONAL\#STEDWARDS\#Summer2022Research\wind_data_2010_2019_MOOT_C695.csv"
site_coords_filepath = r"D:\#PERSONAL\#STEDWARDS\#Summer2022Research\site_coordinates.txt"
particulate_filepath = r"D:\#PERSONAL\#STEDWARDS\#Summer2022Research\daily_pm25_hgb_junsep2010_2019.csv"
hourly_ozone_filepath = r"D:\#PERSONAL\#STEDWARDS\#Summer2022Research\ozone_1hr_editedcopy.xlsx"

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

hourlyozone_keys = ["Date", "Time", "C1_2", "C8_2", "C15_3", "C26_2", "C35_1", "C45_1", "C53_1", "C78_1", "C84_1", "C403_3", "C405_1", "C406_1", "C408_2", "C409_2", "C410_1", "C416_1", "C603_1", "C603_2", "C603_3", "C617_1", "C620_1", "C1015_1", "C1016_1", "C1034_1"]

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

def corr_formatter():
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


def correlation_builder(df1, unit1, df2, unit2):
    corr = df1[unit1].corr(df2[unit2])
    plt.scatter(df1[unit1],df2[unit2])
    
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
    return(True)

def unit_separator(df, unit):
    """
    At this time it is unclear what this does - I think it's supposed to feed me separated DataFrames for more granular visualization'
    """
    grouped = df.groupby(by=unit, as_index=True, sort=True, group_keys=True)
    return(True)

def cluster_byclusterplotter(df):
    i = 0
    while i < 16:
        cluster = df.loc[df['cluster'] == str(i)]
        graph = histo_builder(cluster, "Cluster", i,  True, global_output_path, "cluster_by_cluster")
        i = i + 1
    return(True)

def site_bysiteplotter(df):
    """
    Takes a dataframe and returns a bunch of ozone histograms split up by site.
    """
    unique_items = df["site"].unique()
    unique_items = unique_items[:-1]
    i = 0
    while i < len(unique_items):
        site = unique_items[i]
        site_slug = slugify(site)
        site_measurements = df.loc[df["site"] == site]
        histo_builder(site_measurements, "Site", site_slug, True, global_output_path, r"site_by_site")
        i = i + 1
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

#cluster_byclusterplotter(data)
#month_bymonthplotter(data)
#year_overyearplotter(data)
#site_bysiteplotter(data)


#histo_builder(data, "2010-2019", "Full Sample", True, global_output_path, r"full_sample")

lineplot_builder(data)
# Don't need right now
with open(windrun_filepath) as windrun:
    windrun_data = pd.read_csv(windrun_filepath, delim_whitespace=True)
# Don't need right now  
with open(moody_wind_filepath) as moody_wind:
    moody_data = pd.read_csv(moody_wind_filepath)
# Don't need right now
with open(site_coords_filepath) as site_locations:
    siteloc_df = pd.read_csv(site_coords_filepath, sep="\t")
# Working on this
with open(particulate_filepath) as particulate:
    partic_df = pd.read_csv(particulate_filepath, sep=",")
    orig_datecols = partic_df["Date"]
    dates = pd.to_datetime(orig_datecols, dayfirst = False, yearfirst = True, format = "%Y%m%d")
    partic_df["datetime"] = dates
    partic_df.drop("Date", inplace=True, axis=1)

    partic_df['day'] = partic_df['datetime'].dt.day
    partic_df['month'] = partic_df['datetime'].dt.month
    partic_df['year'] = partic_df['datetime'].dt.year
    
    
    
    data = data.rename(columns=({"date": "datetime"})) # This ins't working right now
    
    data['datetime'] = pd.to_datetime(data['datetime'])
    
    partic_df['datetime'] = pd.to_datetime(partic_df['datetime'])
    
    
    
    data = data.merge(partic_df, how="inner", on=["datetime", "day", "month", "year"])
    
#exceedance_counter(data, "year")


# Onward ho!

cols = data.columns.values.tolist()
cols.pop(0)
cols.pop(0)
cols.pop(0)
cols.pop(0)

cols.pop(0)
cols.pop(0)
cols.pop(0)

plt.cla()



i = 0
while i < len(cols):
    plt.scatter(data["maximum"], data[cols[i]], s=1)
    i = i + 1


plt.cla()

plt.xlim(0,50)
plt.ylim(0,50)
plt.scatter(data["C45_3"], data["C1_3"], s=1)


with open(hourly_ozone_filepath) as hourly_ozone:
    hourly_ozone_xls = pd.ExcelFile(hourly_ozone_filepath)
    df = pd.read_excel(hourly_ozone_xls, 0)
    print(df.iloc[0])
    print(df.shape)
    
    
    # At this point I've read the data in and need to split the individual column entries into two columns using whitespace as the delimiter
    
plt.cla()

plt.xlim(0,140)
plt.ylim(0,140)



"""
plt.scatter(hourlyozone_df["C45_3"], hourlyozone_df["C1_3"])
"""


    
"""
time_separator(data, "month")
time_separator(data, "year")
time_separator(data, "cluster")
"""


"""
i = 0
site_indexes = partic_df.columns
while i < 7:
    site = site_indexes[i]
    correlation_builder(data, "maximum", partic_df, site)
    i = i + 1

correlation_builder(data, "maximum", partic_df, "year")
"""




"""
Map Stuff I guess?
"""
#houston = osmnx.graph_from_place("Houston, Harris County, Texas, United States")

"""    
    plt.text(2, 4, "r2_cell", size=12, ha="center", va="center",
    bbox=dict(boxstyle="round",  facecolor='blue', alpha=0.3) )
"""

"""
FILE OUTPUT
"""