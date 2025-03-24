# -*- coding: utf-8 -*-
"""
Created on Wed Mar 19 10:56:18 2025

@author: brian
"""

# -*- coding: utf-8 -*-
"""
Houston-Galveston-Brazoria (HGB) Region Daily Ozone Map
"""

import sys
sys.path.append("C:/Users/brian/Documents/AQ_ Ozone and PM for HGB SOMs-20250201T165418Z-001 - Copy/AQ_ Ozone and PM for HGB SOMs/Regional Analysis maps AQ over sites/Codes/")

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.colors as mcolors
from EPIC_Graph_Function import EPIC_Graph_Function

# Load the TCEQ site location data
tceq_sites_file = '../Data/TCEQ_Site_Location_Data (version 1).csv'
dataTCEQsites = pd.read_csv(tceq_sites_file)

# Path to the ozone data Excel file
ozone_file = "G:/.shortcut-targets-by-id/1WLOv_L9wwz6Q8Xn55EiDYIyuYgN2nuta/AQ  Ozone and PM for HGB SOMs/Isoheight Ozone Mapping/2010-2019 TCEQ Ozone Max Daily 8-Hour Ozone.xlsx"

# Function to load ozone data for a specific date
def load_ozone_for_date(file_path, target_date):
    """Load ozone data for a specific date"""
    print(f"Loading ozone data for {target_date}...")
    
    try:
        # Convert target date to datetime
        target_dt = pd.to_datetime(target_date)
        
        # Read the Excel file
        xl = pd.ExcelFile(file_path)
        raw_df = pd.read_excel(file_path, sheet_name=xl.sheet_names[0])
        
        # Look for the site column
        site_col = None
        for col in raw_df.columns:
            if "Monitor" in str(col) or "Site" in str(col) or "CAMS" in str(col):
                site_col = col
                break
        
        if site_col is None:
            site_col = raw_df.columns[1]
        
        # Match sites to CAMS numbers
        site_mapping = {}
        for _, row in dataTCEQsites.iterrows():
            if 'CAMS_Name' in dataTCEQsites.columns and 'CAMS_Num' in dataTCEQsites.columns:
                site_mapping[row['CAMS_Name']] = row['CAMS_Num']
                site_mapping[f"CAMS {row['CAMS_Num']}"] = row['CAMS_Num']
        
        # Extract day from target date
        target_day = target_dt.day
        
        # Process data rows
        result_data = []
        for _, row in raw_df.iterrows():
            site_info = row.get(site_col)
            if pd.isna(site_info) or not isinstance(site_info, str):
                continue
                
            # Find matching site
            site_num = None
            for site_pattern, num in site_mapping.items():
                if site_pattern in site_info:
                    site_num = num
                    break
            
            if site_num is None and "CAMS" in site_info:
                parts = site_info.split("CAMS")
                if len(parts) > 1:
                    num_part = ''.join(c for c in parts[1] if c.isdigit())
                    if num_part:
                        site_num = int(num_part)
            
            if site_num is not None:
                # Match to TCEQ site
                tceq_site = dataTCEQsites[dataTCEQsites['CAMS_Num'] == site_num]
                
                if not tceq_site.empty:
                    # Get ozone value for target day
                    for col in raw_df.columns:
                        if isinstance(col, (int, float)) and not pd.isna(col):
                            if int(col) == target_day:
                                ozone_value = row[col]
                                if pd.notnull(ozone_value) and isinstance(ozone_value, (int, float)):
                                    # Convert to ppm if needed
                                    ozone_value = float(ozone_value)
                                    if ozone_value > 0.5:  # Likely in ppb
                                        ozone_value = ozone_value / 1000.0
                                    
                                    result_data.append({
                                        'CAMS_Num': site_num,
                                        'CAMS_Long': tceq_site.iloc[0]['CAMS_Long'],
                                        'CAMS_Lat': tceq_site.iloc[0]['CAMS_Lat'],
                                        'ozone': ozone_value
                                    })
        
        # Return dataframe with results
        if result_data:
            return pd.DataFrame(result_data)
        else:
            return None
            
    except Exception as e:
        print(f"Error loading ozone data: {e}")
        return None

# Create map with ozone data
def create_ozone_map(ozone_data, date_str):
    """Create map with dots colored by ozone values"""
    # Create figure
    fig = plt.figure(figsize=(11, 7))
    ax = fig.add_subplot(111)
    
    # Get map base from EPIC function
    lon_list, lat_list, df, min_lon_tx, max_lon_tx, min_lat_tx, max_lat_tx, gdf, world = EPIC_Graph_Function()
    world.boundary.plot(ax=ax, cmap='Greys', alpha=1)
    
    # Set map bounds
    ax.set_xlim(-96.1, -94.0)
    ax.set_ylim(29.0, 30.3)
    
    # First plot all CAMS sites
    ax.scatter(
        dataTCEQsites['CAMS_Long'], 
        dataTCEQsites['CAMS_Lat'], 
        c='orange', 
        edgecolors='k', 
        marker='.', 
        s=200
    )
    
    # If we have ozone data, color dots by value
    if ozone_data is not None and not ozone_data.empty:
        # Set up color scale
        vmin, vmax = 0.020, 0.120
        cmap = plt.cm.RdYlBu_r
        norm = mcolors.Normalize(vmin=vmin, vmax=vmax)
        
        # Plot colored dots
        scatter = ax.scatter(
            ozone_data['CAMS_Long'], 
            ozone_data['CAMS_Lat'],
            c=ozone_data['ozone'],
            s=200,
            cmap=cmap,
            norm=norm,
            marker='s',
            edgecolors='k',
            linewidths=1
        )
        
        # Add colorbar
        cbar = plt.colorbar(scatter, ax=ax)
        cbar.set_label('Ozone Concentration (ppm)')
        
        # Mark EPA standard
        epa_pos = (0.070 - vmin) / (vmax - vmin)
        cbar.ax.axhline(y=epa_pos, color='r', linestyle='-')
    
    # Set title
    display_date = pd.to_datetime(date_str).strftime('%B %d, %Y')
    ax.set_title(f'Ozone Concentrations on {display_date}\nHouston-Galveston-Brazoria Region')
    
    return fig

# Main execution
if __name__ == "__main__":
    # Select a date
    selected_date = "2019-09-11"
    
    # Load ozone data for this date
    ozone_data = load_ozone_for_date(ozone_file, selected_date)
    
    # Create the map
    fig = create_ozone_map(ozone_data, selected_date)
    
    # Display
    plt.show()