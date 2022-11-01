import numpy as np
import pandas as pd
# import osmnx as ox
import geopandas as gpd
import matplotlib.pyplot as plt
import shapefile
import matplotlib.animation as animation
import matplotlib as mpl

"""
CONFIG
"""


pd.options.display.width = 0
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

mpl.rcParams['figure.dpi'] = 90



"""
def ox_map():
    houston = ox.graph_from_place("Houston, Texas")
    fig, ax = ox.plot_graph(houston, show=False, close=False)
    coordinates = coords()
    print(coordinates)
    plt.plot(coordinates.Latitude, coordinates.Longitude)
    plt.show()
"""

def map():
    with open(r"D:\#PERSONAL\#STEDWARDS\#Summer2022Research\scripts\file_inputs\COH_ADMINISTRATIVE_BOUNDARY_-_MIL\COH_ADMINISTRATIVE_BOUNDARY_-_MIL.csv") as houston_shape:
#        fig, ax = plt.subplots(111)
        houston = pd.read_csv(houston_shape)
        print(houston)
#        houston.plot()
#        plt.show()
#        plt.draw()
#        site_coordinates = coords()
#        plt.plot(site_coordinates.Latitude, site_coordinates.Longitude)

def coords():
    with open(r"file_inputs\site_coordinates.txt") as coords:
        coords_labels = pd.Series(coords.readline().split(sep="\t"))
        coords_series_list = [coords_labels]
        for line in coords:
            elements = coords.readline().split(sep="\t")
            elements_series = pd.Series(elements)
            coords_series_list.append(elements_series)
        coords_output_df = pd.concat(coords_series_list, axis=1).T
        coords_output_df.columns = coords_output_df.iloc[0]
        coords_output_df = coords_output_df[1:]
        return coords_output_df

def augmented_file():
    aug = open(r"file_inputs\SOM_cluster_ozone_augmentedv3.csv")
    aug_df = pd.read_csv(aug)
    print(aug_df)
    stacked_bars(aug_df)
    aug.close()

def stacked_bars(df):
    df.plot.bar(x="site", y="maximum", stacked=True)
    plt.show()
    return
def main():
    map()
#    augmented_file()

main()