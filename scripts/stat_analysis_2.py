import numpy as np
import pandas as pd
import osmnx as ox
import geopandas as gpd
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib as mpl

def coords():
    coords = open(r"file_inputs\site_coordinates.txt")
    coords_line1 = coords.read()
    print(coords_line1)
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
    augmented_file()

main()