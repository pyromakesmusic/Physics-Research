import numpy as np
import pandas as pd
import osmnx as ox
import geopandas as gpd
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib as mpl

def main():
    houston = ox.gdf_from_place("Houston, Texas")
    fig, ax = plt.subplots()
    houston.plot(ax=ax)
    pass

main()