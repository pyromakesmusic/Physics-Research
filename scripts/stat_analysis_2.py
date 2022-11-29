import numpy as np
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib as mpl
from shapely.geometry import Point


"""
CONFIG
"""

crs = {'init':'epsg:4326'} # This is setting a coordinate reference system for geopandas, check this later if it doesn't work.


pd.options.display.width = 0
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

mpl.rcParams['figure.dpi'] = 150

def exceedance_counter(df):
    """
    Takes a dataframe and period of time and returns number and percentage of exceedance days graphed on the screen, for that unit of time
    """

    maxes = df["maximum"]
    exceedance = maxes.ge(71)
    masked = df[exceedance]
    exceedance_count = len(masked)
    sample_length = len(df)
    if sample_length != 0:
        exceedance_ratio = exceedance_count/sample_length
        exceedance_percent = str(round(exceedance_ratio*100, 2)) + "%"
    else:
        exceedance_percent = "NULL"
    output_string = "Exceedance Events: " + str(exceedance_count) + "/" + str(sample_length) + "\nPercentage of Sample in Exceedance: " + exceedance_percent
    return(exceedance_percent, output_string)

def dotcolor(data):
    percent, info = exceedance_counter(data)
    color = "placeholder"
    return color

def map(chemdata):


    fig, ax = plt.subplots()
    houston_file = (r"D:\Downloads\COH_ADMINISTRATIVE_BOUNDARY_-_MIL(1)\COH_ADMINISTRATIVE_BOUNDARY_-_MIL.shp")
    houston = gpd.read_file(houston_file)
    houston.plot(ax=ax)
    geo_coords, site_info = coords()

    for name in site_info["Site Name"]:
        stat, info = exceedance_counter(chemdata.loc[name])
        color = dotcolor(chemdata.loc[name]) # need to change both of these to account for wildcard chars in front and back
        print(stat)
    geo_coords.plot(ax=ax, color="red")
    plt.title("Houston/Galveston Bay Area")
    plt.xticks(rotation=90)
    plt.show()


def basemap():
    plt.title("Houston/Galveston Bay Area")
    plt.show()
    return

def coords():
    with open(r"file_inputs\site_coordinates.txt") as coords:
        coords_labels = pd.Series(coords.readline().split(sep="\t"))
        coords_series_list = [coords_labels]
        lat_long_list = []
        for line in coords:
            elements = coords.readline().split(sep="\t")
            elements_series = pd.Series(elements)
            coords_series_list.append(elements_series)
            lat_long_list.append(Point(float(elements_series[7]), float(elements_series[6])))
        coords_output_df = pd.concat(coords_series_list, axis=1).T
        coords_output_df.columns = coords_output_df.iloc[0]
        coords_output_df = coords_output_df[1:]
        print(coords_output_df)
        coords_geoseries = gpd.GeoSeries(lat_long_list, crs="EPSG:4326")
        return coords_geoseries, coords_output_df

def augmented_file():
    aug = open(r"file_inputs\SOM_cluster_ozone_augmentedv3.csv")
    aug_df = pd.read_csv(aug)
    print(aug_df)
    #stacked_bars(aug_df)
    aug.close()
    return aug_df

def stacked_bars(df):
    df.plot.bar(x="site", y="maximum", stacked=True)
    plt.show()
    return



def main():
    chem_df = augmented_file()
    #basemap()
    map(chem_df)

    plt.draw()

main()