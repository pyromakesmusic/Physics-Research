import numpy as np
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib as mpl



"""
CONFIG
"""

crs = {'init':'epsg:4326'} # This is setting a coordinate reference system for geopandas, check this later if it doesn't work.


pd.options.display.width = 0
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

mpl.rcParams['figure.dpi'] = 90

def map():
    houston_file = (r"D:\Downloads\COH_ADMINISTRATIVE_BOUNDARY_-_MIL(1)\COH_ADMINISTRATIVE_BOUNDARY_-_MIL.shp")
    houston = gpd.read_file(houston_file)
    houston.plot()
    plt.title("Houston/Galveston Bay Area")
    site_coords = coords()
    print(site_coords)
    # ax = site_coords.plot()

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
    #stacked_bars(aug_df)
    aug.close()

def stacked_bars(df):
    df.plot.bar(x="site", y="maximum", stacked=True)
    plt.show()
    return
def main():
    #augmented_file()
    #basemap()
    map()

    plt.draw()

main()