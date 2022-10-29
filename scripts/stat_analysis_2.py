import numpy as np
import pandas as pd
import osmnx as ox
import geopandas as gpd
import matplotlib.pyplot as plt
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

mpl.rcParams['figure.dpi'] = 300



def map():
    houston = ox.graph_from_place("Houston, Texas")
    ox.plot_graph(houston)

def coords():
    coords = open(r"file_inputs\site_coordinates.txt")
    coords_labels = pd.Series(coords.readline().split(sep="\t"))
    coords_series_list = [coords_labels]
    for line in coords:
        elements = coords.readline().split(sep="\t")
        elements_series = pd.Series(elements)
        coords_series_list.append(elements_series)

    coords_output_df = pd.concat(coords_series_list, axis=1).T

    print(coords_output_df)
    coords.close()

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
    coords()
#    map()
#    augmented_file()

main()