# -*- coding: utf-8 -*-
"""
Houston-Galveston-Brazoria (HGB) Region Daily Ozone Map
Combines site map with ozone data visualization
"""

import sys
sys.path.append("C:/Users/brian/Documents/AQ_ Ozone and PM for HGB SOMs-20250201T165418Z-001 - Copy/AQ_ Ozone and PM for HGB SOMs/Regional Analysis maps AQ over sites/Codes/")

import numpy as np
import matplotlib.pyplot as plt
import contextily as cx
import pandas as pd
import matplotlib.colors as mcolors
import os
from datetime import datetime
from matplotlib.lines import Line2D
from EPIC_Graph_Function import EPIC_Graph_Function

# Set plot style
plt.rcParams['font.family'] = 'arial'
plt.rcParams['font.size'] = 14

# Define styling parameters
map_point_size = 200
line_width_value = 2
colorscheme = 'RdYlBu_r'  # Red-Yellow-Blue reversed
label_size = 16
tick_label_size = 12

# Load the TCEQ site location data
tceq_sites_file = '../Data/TCEQ_Site_Location_Data (version 1).csv'
dataTCEQsites = pd.read_csv(tceq_sites_file)
print("TCEQ site data columns:", dataTCEQsites.columns.tolist())

# Ensure required columns exist
if 'CAMS_Name' not in dataTCEQsites.columns:
    alt_name_cols = [col for col in dataTCEQsites.columns if 'name' in col.lower()]
    if alt_name_cols:
        dataTCEQsites['CAMS_Name'] = dataTCEQsites[alt_name_cols[0]]
    else:
        dataTCEQsites['CAMS_Name'] = [f'Site {i}' for i in range(len(dataTCEQsites))]

if 'CAMS_Num' not in dataTCEQsites.columns:
    alt_num_cols = [col for col in dataTCEQsites.columns if 'num' in col.lower() or 'id' in col.lower() or 'code' in col.lower()]
    if alt_num_cols:
        dataTCEQsites['CAMS_Num'] = dataTCEQsites[alt_num_cols[0]]
    else:
        dataTCEQsites['CAMS_Num'] = range(1, len(dataTCEQsites) + 1)

# Make sure we have coordinate columns
for col_name in ['CAMS_Long', 'CAMS_Lat']:
    if col_name not in dataTCEQsites.columns:
        alt_cols = [c for c in dataTCEQsites.columns if col_name[-4:].lower() in c.lower()]
        if alt_cols:
            dataTCEQsites[col_name] = dataTCEQsites[alt_cols[0]]

# Print updated columns
print("Updated TCEQ site data columns:", dataTCEQsites.columns.tolist())

# Path to the ozone data Excel file
ozone_file = "G:/.shortcut-targets-by-id/1WLOv_L9wwz6Q8Xn55EiDYIyuYgN2nuta/AQ  Ozone and PM for HGB SOMs/Isoheight Ozone Mapping/2010-2019 TCEQ Ozone Max Daily 8-Hour Ozone.xlsx"

def load_ozone_for_date(file_path, target_date):
    """
    Load ozone data for a specific date
    
    Parameters:
    file_path (str): Path to the ozone data file
    target_date (str): Date string in 'YYYY-MM-DD' format
    
    Returns:
    DataFrame: Ozone data for the specified date
    """
    print(f"Loading ozone data for {target_date}...")
    
    try:
        # Convert target date to datetime
        target_dt = pd.to_datetime(target_date)
        
        # Read the Excel file
        xl = pd.ExcelFile(file_path)
        raw_df = pd.read_excel(file_path, sheet_name=xl.sheet_names[0])
        
        # Look for the sheet structure
        site_col = None
        for col in raw_df.columns:
            if "Monitor" in str(col) or "Site" in str(col) or "CAMS" in str(col):
                site_col = col
                break
        
        if site_col is None:
            print("Could not find site column, using first non-date column")
            site_col = raw_df.columns[1]  # Usually the second column
        
        # Create a simplified mapping of site names to site numbers
        site_mapping = {}
        for _, row in dataTCEQsites.iterrows():
            site_name = row['CAMS_Name']
            site_num = row['CAMS_Num']
            site_mapping[site_name] = site_num
            # Add some variations for better matching
            site_mapping[f"Site {site_num}"] = site_num
            site_mapping[f"CAMS {site_num}"] = site_num
            site_mapping[f"C{site_num}"] = site_num
        
        # Extract data for the target month/year
        target_month = target_dt.month
        target_year = target_dt.year
        target_day = target_dt.day
        
        print(f"Searching for data from {target_year}-{target_month:02d}")
        
        # Create a result dataframe
        result_data = []
        
        # For each row in the ozone data, try to match it to a TCEQ site
        for i, row in raw_df.iterrows():
            site_info = row.get(site_col)
            
            if pd.isna(site_info) or not isinstance(site_info, str):
                continue
                
            # Try to match the site to a site number
            site_num = None
            for site_pattern, num in site_mapping.items():
                if site_pattern in site_info:
                    site_num = num
                    break
            
            if site_num is None:
                # Try to extract site number from the site info
                if "Site" in site_info:
                    parts = site_info.split("Site")
                    if len(parts) > 1:
                        num_part = ''.join(c for c in parts[1] if c.isdigit())
                        if num_part:
                            site_num = int(num_part)
                elif "CAMS" in site_info:
                    parts = site_info.split("CAMS")
                    if len(parts) > 1:
                        num_part = ''.join(c for c in parts[1] if c.isdigit())
                        if num_part:
                            site_num = int(num_part)
            
            if site_num is not None:
                # Now find the matching TCEQ site
                tceq_site = dataTCEQsites[dataTCEQsites['CAMS_Num'] == site_num]
                
                if not tceq_site.empty:
                    # Get the day column (should correspond to our target day)
                    for col in raw_df.columns:
                        if isinstance(col, (int, float)) and not pd.isna(col):
                            if int(col) == target_day:
                                ozone_value = row[col]
                                if pd.notnull(ozone_value) and isinstance(ozone_value, (int, float)):
                                    # Print the raw value to help with debugging
                                    print(f"Raw ozone value for Site {site_num}: {ozone_value}")
                                    
                                    # Always convert to float to ensure proper handling
                                    ozone_value = float(ozone_value)
                                    
                                    # Check if data is already in ppm or needs conversion from ppb
                                    if ozone_value > 0.5:  # Likely in ppb
                                        ozone_value = ozone_value / 1000.0  # Convert ppb to ppm
                                    
                                    result_data.append({
                                        'CAMS_Num': site_num,
                                        'CAMS_Name': tceq_site.iloc[0]['CAMS_Name'],
                                        'CAMS_Long': tceq_site.iloc[0]['CAMS_Long'],
                                        'CAMS_Lat': tceq_site.iloc[0]['CAMS_Lat'],
                                        'ozone': ozone_value
                                    })
        
        # Create result dataframe
        if result_data:
            result_df = pd.DataFrame(result_data)
            print(f"Found ozone data for {len(result_data)} sites on {target_date}")
            print(f"Ozone value range: {result_df['ozone'].min()} to {result_df['ozone'].max()} ppm")
            return result_df
        else:
            print(f"No ozone data found for {target_date}")
            return None
            
    except Exception as e:
        print(f"Error loading ozone data: {e}")
        import traceback
        traceback.print_exc()
        return None

def create_ozone_map(ozone_data, date_str, output_path=None):
    """
    Create a map showing ozone concentrations at TCEQ sites
    
    Parameters:
    ozone_data (DataFrame): DataFrame with ozone data including CAMS_Long, CAMS_Lat, and ozone
    date_str (str): Date string for title
    output_path (str): Optional path to save the figure
    """
    # Format the date for display
    display_date = pd.to_datetime(date_str).strftime('%B %d, %Y')
    
    # Create the figure with a larger size to ensure map is prominent
    fig = plt.figure(figsize=(14, 10))
    ax1 = fig.add_subplot(111)
    
    # Maximize the map area by adjusting subplot parameters
    plt.subplots_adjust(left=0.05, right=0.95, top=0.9, bottom=0.05)
    
    # Get map base from EPIC function
    lon_list, lat_list, df, min_lon_tx, max_lon_tx, min_lat_tx, max_lat_tx, gdf, world = EPIC_Graph_Function()
    
    # Plot the map boundary
    im2 = world.boundary.plot(ax=ax1, cmap='Greys', alpha=1)
    
    # Set map bounds using the values from EPIC_Graph_Function to ensure proper city visibility
    # Use the Texas-specific bounds from the function
    ax1.set_xlim(min_lon_tx - 0.2, max_lon_tx + 0.2)  # Add a small buffer
    ax1.set_ylim(min_lat_tx - 0.2, max_lat_tx + 0.2)  # Add a small buffer
    
    # Print the coordinates for debugging
    print(f"Map bounds: lon ({min_lon_tx-0.2}, {max_lon_tx+0.2}), lat ({min_lat_tx-0.2}, {max_lat_tx+0.2})")
    
    # Add basemap with better map style for visibility
    try:
        # Try a more detailed map style first
        cx.add_basemap(im2, crs=gdf.crs, 
                      source=cx.providers.CartoDB.Positron, 
                      zoom=10)  # Higher zoom level for more detail
    except Exception as e:
        print(f"Error with primary basemap, falling back to alternative: {e}")
        # Fallback to the original style
        cx.add_basemap(im2, crs=gdf.crs, 
                      source='https://tiles.stadiamaps.com/tiles/stamen_toner/{z}/{x}/{y}{r}.png?api_key=bc4a6e42-ab94-4a2d-8b3a-9870188a8543',
                      zoom=10)
    
    # Set tick locations and styling - dynamically based on the map extent
    x_range = ax1.get_xlim()
    y_range = ax1.get_ylim()
    
    # Calculate appropriate tick intervals
    x_major_interval = 0.5
    x_minor_interval = 0.1
    y_major_interval = 0.5
    y_minor_interval = 0.1
    
    # Generate tick positions
    x_start = np.floor(x_range[0] / x_major_interval) * x_major_interval
    x_end = np.ceil(x_range[1] / x_major_interval) * x_major_interval
    y_start = np.floor(y_range[0] / y_major_interval) * y_major_interval
    y_end = np.ceil(y_range[1] / y_major_interval) * y_major_interval
    
    xticks_major = np.arange(x_start, x_end + x_major_interval, x_major_interval)
    xticks_minor = np.arange(x_start, x_end + x_minor_interval, x_minor_interval)
    yticks_major = np.arange(y_start, y_end + y_major_interval, y_major_interval)
    yticks_minor = np.arange(y_start, y_end + y_minor_interval, y_minor_interval)
    
    # Set major ticks for x axis
    ax1.set_xticks(xticks_major)
    ax1.set_xticklabels(xticks_major, fontsize=tick_label_size)
    
    # Set minor ticks for x axis
    ax1.set_xticks(xticks_minor, minor=True)
    
    # Set major ticks for y axis
    ax1.set_yticks(yticks_major)
    ax1.set_yticklabels(yticks_major, fontsize=tick_label_size)
    
    # Set minor ticks for y axis
    ax1.set_yticks(yticks_minor, minor=True)
    
    # Customize appearance of ticks
    ax1.tick_params(axis='x', which='minor', length=6, color='gray')
    ax1.tick_params(axis='y', which='minor', length=6, color='gray')
    ax1.tick_params(axis='x', which='both', direction='inout', top=True, bottom=True)
    ax1.tick_params(axis='x', which='major', length=10)
    ax1.tick_params(axis='y', which='both', direction='inout', right=True, left=True)
    ax1.tick_params(axis='y', which='major', length=10)
    
    # Add geographic/city labels for better context
    city_labels = [
        {'name': 'Houston', 'lon': -95.3698, 'lat': 29.7604},
        {'name': 'Galveston', 'lon': -94.7977, 'lat': 29.3013},
        {'name': 'Brazoria', 'lon': -95.5605, 'lat': 29.0547},
        {'name': 'Sugar Land', 'lon': -95.6349, 'lat': 29.6197},
        {'name': 'Baytown', 'lon': -94.9719, 'lat': 29.7355},
        {'name': 'The Woodlands', 'lon': -95.5047, 'lat': 30.1658}
    ]
    
    # Add city labels with white background for visibility
    for city in city_labels:
        # Check if the city is within the map bounds
        if (ax1.get_xlim()[0] <= city['lon'] <= ax1.get_xlim()[1] and
            ax1.get_ylim()[0] <= city['lat'] <= ax1.get_ylim()[1]):
            ax1.text(city['lon'], city['lat'], city['name'], 
                    fontsize=14, ha='center', va='center', 
                    bbox=dict(facecolor='white', alpha=0.6, edgecolor='gray', boxstyle='round,pad=0.3'),
                    zorder=100)  # High zorder to ensure it's on top
    
    # Plot TCEQ sites with ozone values
    if ozone_data is not None and not ozone_data.empty:
        # First plot ALL sites in orange (like mentor's code)
        background_sites = ax1.scatter(
            dataTCEQsites['CAMS_Long'], 
            dataTCEQsites['CAMS_Lat'], 
            c='orange', 
            edgecolors='k', 
            marker='o', 
            s=map_point_size * 0.8,  # Slightly smaller for background sites
            alpha=0.3,  # Make them semi-transparent
            zorder=5,
            label='All CAMS Sites'
        )
        
        # Print actual ozone values to verify data
        print("Ozone values in dataset:")
        for _, row in ozone_data.iterrows():
            print(f"CAMS {row['CAMS_Num']}: {row['ozone']} ppm")
            
        # Force values to be numeric
        ozone_data['ozone'] = pd.to_numeric(ozone_data['ozone'], errors='coerce')
        
        # Remove any rows with NaN ozone values
        ozone_data = ozone_data.dropna(subset=['ozone'])
        
        if ozone_data.empty:
            print("No valid ozone values found after conversion")
            return None
            
        # Determine appropriate color scale based on actual data range
        min_ozone = ozone_data['ozone'].min()
        max_ozone = ozone_data['ozone'].max()
        
        # Fix: Use fixed color range to ensure colors are visible
        # EPA standard is 0.070 ppm
        vmin = 0.020  # Fixed minimum
        vmax = 0.120  # Fixed maximum
        
        print(f"Actual data range: {min_ozone} to {max_ozone} ppm")
        print(f"Using color scale from {vmin} to {vmax} ppm")
        
        # Create colormap for ozone values - using the colorscheme from global variables
        cmap = plt.cm.RdYlBu_r  # Use RdYlBu_r instead of viridis for better contrast with ozone data
        norm = mcolors.Normalize(vmin=vmin, vmax=vmax)
        
        # Create a ScalarMappable for the colorbar
        sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
        sm.set_array([])
        
        # Plot the ozone values - use slightly different markers for better visibility
        scatter = ax1.scatter(
            ozone_data['CAMS_Long'], 
            ozone_data['CAMS_Lat'],
            c=ozone_data['ozone'],
            s=map_point_size * 1.2,  # Slightly larger
            cmap=cmap,
            norm=norm,
            marker='s',  # Square markers for ozone sites
            edgecolors='k',
            linewidths=line_width_value,
            zorder=10,  # Ensure this displays on top
            label='Ozone Data'
        )
        
        # Highlight sites that exceed the EPA standard
        exceed_sites = ozone_data[ozone_data['ozone'] > 0.070]
        if not exceed_sites.empty:
            ax1.scatter(
                exceed_sites['CAMS_Long'], 
                exceed_sites['CAMS_Lat'],
                s=map_point_size * 1.5,  # Even larger for emphasis
                facecolors='none',  # No fill
                edgecolors='red',
                linewidths=3,
                marker='o',  # Circle around the square
                zorder=11,  # Display on top of everything
                label='Exceeds EPA Std'
            )
        
        # Add site labels with ozone values - improve label placement to reduce overlaps
        for _, row in ozone_data.iterrows():
            # Adjust text color based on whether the site exceeds standards
            text_color = 'red' if row['ozone'] > 0.070 else 'black'
            
            # Get numeric value from CAMS_Num, handling both string and numeric formats
            try:
                if isinstance(row['CAMS_Num'], str) and 'CAMS' in row['CAMS_Num']:
                    # Extract the numeric part if it's a string like "CAMS 1"
                    cams_num_val = int(''.join(filter(str.isdigit, row['CAMS_Num'])))
                else:
                    # Otherwise just try to convert directly to int
                    cams_num_val = int(row['CAMS_Num'])
            except (ValueError, TypeError):
                # If conversion fails, use a fallback value based on row index
                cams_num_val = _ % 4  # Use row index for modulo
            
            # Calculate a position offset that varies for each site to reduce overlap
            # This creates a staggered effect for the labels
            idx = cams_num_val % 4  # Use modulo to get 4 different patterns
            
            if idx == 0:
                x_offset, y_offset = 0.02, 0.02  # Upper right
            elif idx == 1:
                x_offset, y_offset = -0.12, 0.02  # Upper left
            elif idx == 2:
                x_offset, y_offset = 0.02, -0.08  # Lower right
            else:
                x_offset, y_offset = -0.12, -0.08  # Lower left
            
            # Create a white background for the text to improve readability
            text_obj = ax1.text(
                row['CAMS_Long'] + x_offset, 
                row['CAMS_Lat'] + y_offset, 
                f"CAMS {str(row['CAMS_Num']).replace('CAMS ', '')}\n{row['ozone']:.3f}", 
                fontsize=9,
                ha='center' if idx in [0, 2] else 'right',
                va='center',
                color=text_color,
                weight='bold' if row['ozone'] > 0.070 else 'normal',
                bbox=dict(facecolor='white', alpha=0.7, edgecolor='none', pad=1)
            )
        
        # Add a colorbar with EPA threshold marked
        cbar = fig.colorbar(sm, ax=ax1, pad=0.01)
        cbar.set_label('Ozone Concentration (ppm)', fontsize=16)
        
        # Add EPA standard line to colorbar if it's within our range
        epa_pos = (0.070 - vmin) / (vmax - vmin)
        cbar.ax.axhline(y=epa_pos, color='r', linestyle='-', linewidth=2)
        cbar.ax.text(1.5, epa_pos, 'EPA std (0.070 ppm)', color='r', 
                    ha='left', va='center', fontsize=10, weight='bold')
        
        # Create a legend with fewer, more meaningful categories
        legend_elements = [
            Line2D([0], [0], marker='o', color='w', markerfacecolor='none', 
                markeredgecolor='red', markersize=15, markeredgewidth=3,
                label='Exceeds EPA Std'),
            Line2D([0], [0], marker='s', color='w', markerfacecolor='#990000', 
                markersize=10, label='>0.080 ppm'),
            Line2D([0], [0], marker='s', color='w', markerfacecolor='#FF9933', 
                markersize=10, label='0.060-0.080 ppm'),
            Line2D([0], [0], marker='s', color='w', markerfacecolor='#3366FF', 
                markersize=10, label='<0.060 ppm'),
            Line2D([0], [0], marker='o', color='w', markerfacecolor='orange', 
                markersize=10, label='Other CAMS Sites')
        ]
        
        # Place legend in a location with less data, like lower left
        leg = ax1.legend(handles=legend_elements, loc='lower left', fontsize=10, 
                    framealpha=0.8, facecolor='white', edgecolor='gray')
        
        # Calculate exceedance percentage
        exceed_count = sum(ozone_data['ozone'] > 0.070)
        exceed_percent = (exceed_count / len(ozone_data)) * 100
    else:
        # If no ozone data, just plot the TCEQ sites like in mentor's code
        ax1.scatter(dataTCEQsites['CAMS_Long'], dataTCEQsites['CAMS_Lat'], 
                   c='orange', edgecolors='k', marker='o', s=map_point_size)
        exceed_percent = 0
    
    # Set the title using mentor's style with label_size
    if ozone_data is not None and not ozone_data.empty:
        ax1.set_title(f'Ozone Concentrations on {display_date}\n'
                    f'Houston-Galveston-Brazoria (HGB) Region\n'
                    f'{exceed_percent:.1f}% of CAMS stations exceed EPA standard', 
                    fontdict={'fontsize': label_size}, pad=20)  # Add padding above title
    else:
        ax1.set_title(f'TCEQ Monitoring Stations (CAMS)\n'
                    f'Houston-Galveston-Brazoria (HGB) Region',
                    fontdict={'fontsize': label_size}, pad=20)  # Add padding above title
    
    # Adjust layout - don't use tight_layout as it can make the map smaller
    # Instead, we've already set good subplot parameters above
    
    # Save the figure if requested - use higher DPI for better quality
    if output_path:
        plt.savefig(output_path, dpi=300, bbox_inches='tight')
        print(f"Figure saved to {output_path}")
    
    return fig

# Main execution
if __name__ == "__main__":
    # Select a date to visualize
    selected_date = "2019-09-11"  # September 11, 2019
    
    # Format the date in a more readable format for display
    display_date = pd.to_datetime(selected_date).strftime('%B %d, %Y')  # "September 11, 2019"
    
    # Load ozone data for this date
    ozone_data = load_ozone_for_date(ozone_file, selected_date)
    
    # Debug: Create a sample dataset if no data is found
    if ozone_data is None or ozone_data.empty:
        print("WARNING: No data found. Creating sample data for testing.")
        # Create sample data using TCEQ site locations
        sample_data = []
        
        # Check if required columns exist in dataTCEQsites
        required_cols = ['CAMS_Num', 'CAMS_Name', 'CAMS_Long', 'CAMS_Lat']
        missing_cols = [col for col in required_cols if col not in dataTCEQsites.columns]
        
        if missing_cols:
            print(f"WARNING: Missing columns in TCEQ data: {missing_cols}")
            print("Creating completely artificial sample data")
            
            # Create artificial site data
            for i in range(10):
                # Houston area coordinates - random points
                long = -95.3698 + np.random.uniform(-0.5, 0.5)
                lat = 29.7604 + np.random.uniform(-0.3, 0.3)
                sample_data.append({
                    'CAMS_Num': i + 1,
                    'CAMS_Name': f'Site {i+1}',
                    'CAMS_Long': long,
                    'CAMS_Lat': lat,
                    'ozone': np.random.uniform(0.040, 0.090)  # Random values from 0.040 to 0.090 ppm
                })
        else:
            # Use existing TCEQ data
            for _, row in dataTCEQsites.head(10).iterrows():  # Use first 10 sites
                sample_data.append({
                    'CAMS_Num': row['CAMS_Num'],
                    'CAMS_Name': row['CAMS_Name'],
                    'CAMS_Long': row['CAMS_Long'],
                    'CAMS_Lat': row['CAMS_Lat'],
                    'ozone': np.random.uniform(0.040, 0.090)  # Random values from 0.040 to 0.090 ppm
                })
        
        ozone_data = pd.DataFrame(sample_data)
        print("Sample data created with range:", ozone_data['ozone'].min(), "to", ozone_data['ozone'].max())
    
    # Create output directory if it doesn't exist
    output_dir = '../Plots'
    os.makedirs(output_dir, exist_ok=True)
    
    # Create and display the map
    fig = create_ozone_map(
        ozone_data, 
        selected_date, 
        output_path=os.path.join(output_dir, f'HGB-ozone-map-{selected_date}.png')
    )
    
    plt.show()