import numpy as np
import pandas as pd
import osmnx as ox
import geopandas as gpd
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib as mpl

def main():
    houston = ox.graph_from_place("Harris County, Texas")
    ox.plot_graph(houston)

main()