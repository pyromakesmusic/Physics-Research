#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 12:08:00 2023

@author: samuelflusche
"""



import geopandas as gpd
import geodatasets
import h5py
import pandas as pd






def EPIC_Graph_Function():
    filepath = './EPIC_Files/'


    #read data from hdf5 file, make list of keys
    data = h5py.File(filepath+'ALL_EPIC.h5','r')
    epic_date_list = list(data['tco'].keys())

    #do the same but for the geos_cf
    #data = h5py.File(geos_cf_filename,'r')
  #  geos_cf_date_list = list(data.keys())


    #make df of the first day only for use in finding the coordinates, the first array is an empty one
    df0 = pd.read_hdf(filepath+'All_EPIC.h5','/tco/'+epic_date_list[0]+'/df')


    #this df zooms in the previous one to just the Houston area
    df_tx = df0.iloc[21:27,13:20]

    #make list of coordinates for full area
    lat_list = []
    for epic_lat in df0.index:
        lat_list.append(epic_lat)

    lon_list = []
    for epic_lon in pd.to_numeric(df0.columns):
        lon_list.append(epic_lon)
        
        
    #make list of coordinates for houston area
    lat_list_tx=[]
    for epic_lat in df_tx.index:
        lat_list_tx.append(epic_lat)

    lon_list_tx = []
    for epic_lon in pd.to_numeric(df_tx.columns):
        lon_list_tx.append(epic_lon)
        
    min_lon = min(lon_list)
    max_lon = max(lon_list)
    min_lat = min(lat_list)
    max_lat = max(lat_list)

    min_lon_tx = min(lon_list_tx)
    max_lon_tx = max(lon_list_tx)
    min_lat_tx = min(lat_list_tx)
    max_lat_tx = max(lat_list_tx)

    # creates boundary points for map
    boundary_points = [(min_lon,min_lat),
                                (max_lon,min_lat),
                                (max_lon,max_lat),
                                (min_lon,max_lat)
                                ]
    
    boundary_points_tx = [(min_lon_tx,min_lat_tx),
                                (max_lon_tx,min_lat_tx),
                                (max_lon_tx,max_lat_tx),
                                (min_lon_tx,max_lat_tx)
                                ]

    # creates geodataframe for the map based on boundary points
    gdf = gpd.GeoDataFrame(geometry=gpd.points_from_xy(*zip(*boundary_points)),crs ='epsg:4326')
    gdf_tx = gpd.GeoDataFrame(geometry=gpd.points_from_xy(*zip(*boundary_points_tx)),crs ='epsg:4326')

    world = gpd.read_file(geodatasets.get_path('naturalearth.land'))
    
    return lon_list,lat_list,df0,min_lon_tx,max_lon_tx,min_lat_tx,max_lat_tx,gdf,world