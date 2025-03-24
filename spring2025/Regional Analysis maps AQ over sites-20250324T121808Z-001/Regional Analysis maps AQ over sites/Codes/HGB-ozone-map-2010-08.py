# -*- coding: utf-8 -*-
"""
Created on Fri Mar 21 14:00:15 2025

@author: brian
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Mar 21 10:08:49 2025

@author: brian
"""
# -*- coding: utf-8 -*-
"""
HGB Region Daily Ozone Map - Optimized for display with all sites visible
"""

# Imports
import numpy as np
import matplotlib.pyplot as plt
import contextily as cx
import pandas as pd
import matplotlib.colors as mcolors
import os
import re
import sys

# Add this path if needed for your imports
sys.path.append("C:/Users/brian/Documents/AQ_ Ozone and PM for HGB SOMs-20250201T165418Z-001 - Copy/AQ_ Ozone and PM for HGB SOMs/Regional Analysis maps AQ over sites/Codes/")

# Attempt to import EPIC_Graph_Function
try:
    from EPIC_Graph_Function import EPIC_Graph_Function
    print("Successfully imported EPIC_Graph_Function")
except ImportError:
    print("Error importing EPIC_Graph_Function. Check your paths.")
    sys.exit(1)

# Set up matplotlib formatting
from matplotlib import rcParams
rcParams['font.family'] = 'arial'
rcParams['font.size'] = 20

# Define styling parameters - ADJUSTED FOR SMALLER FIGURE
map_point_size = 200  # Reduced from 400 to match base map
line_width_value = 1.5  # Slightly reduced
colorscheme = 'viridis'
label_size = 20  # Slightly reduced
tick_label_size = 16  # Slightly reduced

# IMPORTANT: Match figure size to your base map
FIGURE_WIDTH = 11.6  # Match base map
FIGURE_HEIGHT = 7    # Match base map

# Parameters
target_day = 1  # Change this to visualize different days of the month
month_name = "August"
year = 2010

# Load the TCEQ site data
tceq_sites_file = '../Data/TCEQ_Site_Location_Data (version 1).csv'
if not os.path.exists(tceq_sites_file):
    tceq_sites_file = 'TCEQ_Site_Location_Data (version 1).csv'

try:
    dataTCEQsites = pd.read_csv(tceq_sites_file)
    print(f"Loaded TCEQ site data from {tceq_sites_file}")
except Exception as e:
    print(f"Error loading TCEQ site file: {e}")
    print("Creating example data instead")
    # Create example data
    data = {
        'CAMS_Num': [1, 8, 26, 35, 45, 53, 64, 78, 81, 698],
        'CAMS_Name': ['Houston East', 'Houston Aldine', 'Northwest Harris Co.', 
                     'Hou.DeerPrk2', 'Seabrook Friendship Park', 'Houston Bayland Park',
                     'Hamshire', 'Conroe Relocated', 'Houston Regional Office', 'UH WG Jones Forest'],
        'CAMS_Lat': [29.7677, 29.9014, 29.8389, 29.6706, 29.5826, 29.6989, 29.8518, 30.3503, 29.7228, 30.0391],
        'CAMS_Long': [-95.3210, -95.4250, -95.6848, -95.1285, -95.0165, -95.4990, -94.3152, -95.4258, -95.3405, -95.4277]
    }
    dataTCEQsites = pd.DataFrame(data)

# Normalize column names in TCEQ sites data
print(f"TCEQ columns before renaming: {dataTCEQsites.columns.tolist()}")

# Standardize TCEQ column names for consistent mapping
if 'CAMS Sites' in dataTCEQsites.columns:
    print("Renaming 'CAMS Sites' to 'CAMS_Name'")
    dataTCEQsites = dataTCEQsites.rename(columns={'CAMS Sites': 'CAMS_Name'})
    
if 'CAMS CODE' in dataTCEQsites.columns:
    print("Renaming 'CAMS CODE' to 'CAMS_Num'")
    dataTCEQsites = dataTCEQsites.rename(columns={'CAMS CODE': 'CAMS_Num'})
    
print(f"TCEQ columns after renaming: {dataTCEQsites.columns.tolist()}")

# Make sure CAMS_Num is treated as numeric (integer) for matching
if 'CAMS_Num' in dataTCEQsites.columns:
    try:
        dataTCEQsites['CAMS_Num'] = pd.to_numeric(dataTCEQsites['CAMS_Num'], errors='coerce').fillna(0).astype(int)
        print("Converted CAMS_Num to numeric for proper matching")
    except Exception as e:
        print(f"Warning: Could not convert CAMS_Num to numeric: {e}")

# Create output directory if it doesn't exist
output_dir = '../Plots'
os.makedirs(output_dir, exist_ok=True)

# Path to file containing MDA8 ozone for a month
ozone_file_path = "G:/.shortcut-targets-by-id/1WLOv_L9wwz6Q8Xn55EiDYIyuYgN2nuta/AQ  Ozone and PM for HGB SOMs/Regional Analysis maps AQ over sites/Data/MDA8_O3/HGB_MDA8-O3_201008.txt"

def read_special_format_txt(filepath):
    """Custom function to read your specific ozone data format"""
    try:
        with open(filepath, 'r') as file:
            # Read all lines
            lines = file.readlines()
            
            # The first line is the header with month/year
            month_year = lines[0].strip()
            print(f"Header from file: {month_year}")
            
            # The second line contains column headers
            headers = lines[1].strip().split(',')
            print(f"Found {len(headers)} columns: {headers}")
            
            # The rest of the lines contain data
            data = []
            for line in lines[2:]:
                line = line.strip()
                if line:  # Skip empty lines
                    values = line.split(',')
                    if len(values) == len(headers):
                        data.append(values)
                    else:
                        print(f"Warning: Line has {len(values)} values, expected {len(headers)}: {line}")
            
            # Create a DataFrame
            df = pd.DataFrame(data, columns=headers)
            
            # Convert numeric columns to float where possible
            for col in df.columns:
                if col not in ['Area', 'Monitoring_Site', 'POC', 'Flag']:
                    try:
                        df[col] = pd.to_numeric(df[col], errors='coerce')
                    except:
                        pass
            
            return df
    except Exception as e:
        print(f"Error reading file: {e}")
        return None

# Use our custom function to read the ozone data
print(f"Loading ozone data from {ozone_file_path}")
try:
    if os.path.exists(ozone_file_path):
        ozone_raw = read_special_format_txt(ozone_file_path)
        if ozone_raw is None:
            raise Exception("Failed to parse ozone data file")
        print(f"Successfully loaded ozone data with {len(ozone_raw)} rows")
    else:
        raise FileNotFoundError(f"Ozone file not found: {ozone_file_path}")
except Exception as e:
    print(f"Error loading ozone file: {e}")
    print("Using backup data instead...")
    
    # Use the backup data
    raw_data = """June 2010
Area,Monitoring_Site,POC,Flag,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30
,Hamshire C64/C654,1,Reg,36,35,47,37,34,27,25,23,20,17,14,13,17,22,30,27,NV,NV,20,25,33,45,36,26,35,27,25,27,30,18
,Houston East C1/G316,2,Reg,49,35,30,42,41,33,22,29,22,19,15,15,17,23,28,34,23,26,28,37,46,51,34,54,30,36,31,29,30,13
,Houston Aldine C8/AF108/X150 ,2,Reg,65,40,35,49,52,47,32,37,27,23,17,18,22,27,38,42,28,33,41,50,63,61,NV,50,43,46,44,37,NV,21
,Northwest Harris Co. C26/A110/X154,2,Reg,61,40,39,52,48,45,36,35,30,27,24,22,24,28,33,40,27,29,39,39,59,61,47,31,42,44,42,35,36,23
,Hou.DeerPrk2 C35/235/1001/AFH139FP239,1,Reg,46,38,41,54,41,41,33,39,23,20,16,16,18,23,31,32,22,27,28,32,41,52,41,46,36,37,33,33,35,22
,Seabrook Friendship Park C45,1,Reg,40,36,44,59,38,36,35,32,21,19,15,16,19,20,29,29,19,22,23,29,36,48,38,30,38,34,31,29,31,22
,Houston Bayland Park C53/A146 ,1,Reg,43,34,37,53,43,32,28,32,22,22,16,15,18,20,24,34,20,21,28,26,34,39,34,35,30,31,31,28,40,19
,Conroe Relocated C78/A321,1,Reg,68,43,36,42,54,47,28,28,22,32,30,28,28,38,43,49,36,41,47,45,66,60,46,33,49,42,50,25,27,20
,Houston Regional Office C81,1,Reg,40,31,31,46,39,29,19,25,19,16,12,13,17,19,26,29,19,20,25,28,34,38,28,31,26,34,28,NV,29,14
,UH WG Jones Forest C698,1,Non,82,48,39,53,63,60,35,36,32,36,33,33,31,43,NV,NV,41,47,58,58,80,80,60,42,62,54,60,35,36,25"""
    
    # Parse the data using our custom approach
    lines = raw_data.strip().split('\n')
    month_year = lines[0].strip()
    headers = lines[1].strip().split(',')
    data = []
    for line in lines[2:]:
        values = line.strip().split(',')
        if len(values) == len(headers):
            data.append(values)
    
    ozone_raw = pd.DataFrame(data, columns=headers)
    
    # Convert numeric columns to float where possible
    for col in ozone_raw.columns:
        if col not in ['Area', 'Monitoring_Site', 'POC', 'Flag']:
            ozone_raw[col] = pd.to_numeric(ozone_raw[col], errors='coerce')
    
    print(f"Using backup data with {len(ozone_raw)} rows")

print(f"Available columns in ozone data: {ozone_raw.columns.tolist()}")

# Check if day_str exists in the columns
day_str = str(target_day)
if day_str not in ozone_raw.columns:
    print(f"Error: Day {day_str} not found in ozone data columns")
    sys.exit(1)

# Process the ozone data for the target day
processed_data = []

# Identify the site name column in ozone data
site_column = None
if 'Monitoring_Site' in ozone_raw.columns:
    site_column = 'Monitoring_Site'
    print(f"Using 'Monitoring_Site' column from ozone data")
elif 'CAMS_Name' in ozone_raw.columns:
    site_column = 'CAMS_Name'
    print(f"Using 'CAMS_Name' column from ozone data")
elif 'CAMS Sites' in ozone_raw.columns:
    site_column = 'CAMS Sites'
    print(f"Using 'CAMS Sites' column from ozone data")

if site_column is None:
    print(f"Error: Could not find a suitable site name column in ozone data")
    print(f"Available columns: {ozone_raw.columns.tolist()}")
    
    # Try to find a column that might contain site names
    print("Searching for a column that might contain site names...")
    for col in ozone_raw.columns:
        if ozone_raw[col].dtype == 'object':
            # Check if any value in this column contains 'C' followed by digits (CAMS pattern)
            has_cams_pattern = any(ozone_raw[col].astype(str).str.contains(r'C\d+', regex=True))
            if has_cams_pattern:
                site_column = col
                print(f"Found potential site name column: '{site_column}'")
                break
    
    if site_column is None:
        sys.exit(1)

# Define a regex pattern to extract CAMS numbers from site names
cams_pattern = r'C(\d+)'

for i, row in ozone_raw.iterrows():
    site_name = row[site_column] if pd.notna(row[site_column]) else ""
    site_name = str(site_name).strip()
    
    # Extract CAMS number from site name using regex
    cams_num = None
    matches = re.findall(cams_pattern, site_name)
    if matches:
        cams_num = int(matches[0])
        print(f"Found CAMS number {cams_num} in site name: {site_name}")
    
    # Find matching TCEQ site by CAMS number
    if cams_num is not None:
        print(f"Looking for CAMS number {cams_num} in TCEQ data...")
        # First try direct numeric matching
        matching_sites = dataTCEQsites[dataTCEQsites['CAMS_Num'] == cams_num]
        
        if matching_sites.empty:
            print(f"No direct match for CAMS {cams_num}, trying string matching...")
            # Try matching as string values
            matching_sites = dataTCEQsites[dataTCEQsites['CAMS_Num'].astype(str) == str(cams_num)]
        
        if matching_sites.empty:
            print(f"No exact match for CAMS {cams_num} in TCEQ data, trying fuzzy match...")
            # Try a more flexible match based on site name
            for idx, tceq_row in dataTCEQsites.iterrows():
                tceq_site_name = str(tceq_row.get('CAMS_Name', '')).strip()
                if site_name in tceq_site_name or tceq_site_name in site_name:
                    matching_sites = dataTCEQsites.iloc[[idx]]
                    print(f"Found fuzzy match: '{site_name}' ≈ '{tceq_site_name}'")
                    break
        
        if not matching_sites.empty:
            # Get coordinates
            site_info = matching_sites.iloc[0]
            
            # Get ozone value for target day
            ozone_value = row[day_str]
            if pd.notna(ozone_value) and str(ozone_value) not in ['NA', 'NV']:
                try:
                    ozone_value = float(ozone_value)
                    
                    # Add to result data
                    processed_data.append({
                        'CAMS_Num': cams_num,
                        'CAMS_Name': site_name,
                        'CAMS_Long': site_info['CAMS_Long'],
                        'CAMS_Lat': site_info['CAMS_Lat'],
                        'ozone': ozone_value / 1000.0  # Convert ppb to ppm
                    })
                    print(f"Added data for site {site_name}: {ozone_value/1000.0:.3f} ppm")
                except (ValueError, TypeError):
                    print(f"Could not convert ozone value '{ozone_value}' to float for site {site_name}")
        else:
            print(f"No matching TCEQ site found for CAMS {cams_num}")

if not processed_data:
    print(f"No ozone data processed for day {target_day}")
    sys.exit(1)

ozone_data = pd.DataFrame(processed_data)
print(f"Processed {len(ozone_data)} sites with ozone data for day {target_day}")

# Create the map - DIRECT PLOTTING APPROACH
# Create figure with specified dimensions 
fig = plt.figure(figsize=(FIGURE_WIDTH, FIGURE_HEIGHT))
ax1 = fig.add_subplot(111)

# Get map base using EPIC function
lon_list, lat_list, df, min_lon_tx, max_lon_tx, min_lat_tx, max_lat_tx, gdf, world = EPIC_Graph_Function()
EPIC_lon_bounds = np.array(lon_list) + 0.125
EPIC_lat_bounds = np.array(lat_list) - 0.125

im2 = world.boundary.plot(ax=ax1, cmap='Greys', alpha=1)

# IMPORTANT: Slightly wider map bounds to fit all sites
ax1.set_xlim(-96.2, -93.9)  # Slightly wider longitude bounds
ax1.set_ylim(28.9, 30.4)    # Slightly wider latitude bounds

# Add basemap
try:
    cx.add_basemap(im2, crs=gdf.crs, 
                 source='https://tiles.stadiamaps.com/tiles/stamen_toner/{z}/{x}/{y}{r}.png?api_key=bc4a6e42-ab94-4a2d-8b3a-9870188a8543')
except Exception as e:
    print(f"Warning: Could not add basemap: {e}")

# Specifies tick mark locations
xticks_major = np.arange(-96, -93.95, 0.5)  # Major ticks every 0.5 degrees
xticks_minor = np.arange(-96, -93.95, 0.1)  # Minor ticks every 0.1 degrees
yticks_major = np.arange(29, 30.34, 0.5)  # Major ticks every 0.5 degrees
yticks_minor = np.arange(29, 30.34, 0.1)  # Minor ticks every 0.1 degrees

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

# Customize appearance of minor ticks
ax1.tick_params(axis='x', which='minor', length=6, color='gray')
ax1.tick_params(axis='y', which='minor', length=6, color='gray')

# Customize ticks on both sides
ax1.tick_params(axis='x', which='both', direction='inout', top=True, bottom=True)
ax1.tick_params(axis='x', which='major', length=10)
ax1.tick_params(axis='x', which='minor', length=6, color='gray')
ax1.tick_params(axis='y', which='both', direction='inout', right=True, left=True)
ax1.tick_params(axis='y', which='major', length=10)
ax1.tick_params(axis='y', which='minor', length=6, color='gray')

# Plot all TCEQ sites as background
background_sites = ax1.scatter(
    dataTCEQsites['CAMS_Long'], 
    dataTCEQsites['CAMS_Lat'], 
    c='gray', 
    edgecolors='k', 
    marker='.', 
    s=map_point_size * 0.5,
    alpha=0.3,
    zorder=5
)

# Set up color scale for ozone values
vmin, vmax = 0.020, 0.120  # Fixed range for consistency
cmap = plt.cm.coolwarm  # Change to coolwarm for clearer blue-to-red gradient
norm = mcolors.Normalize(vmin=vmin, vmax=vmax)

# Create a ScalarMappable for the colorbar
sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
sm.set_array([])

# Plot ozone values with appropriate markers
scatter = ax1.scatter(
    ozone_data['CAMS_Long'], 
    ozone_data['CAMS_Lat'],
    c=ozone_data['ozone'],
    s=map_point_size * 0.5,  # Slightly reduced for small figure
    cmap=cmap,
    norm=norm,
    marker='s',  # Square markers
    edgecolors='k',
    linewidths=line_width_value,
    zorder=10
)

# Highlight sites that exceed the EPA standard
exceed_sites = ozone_data[ozone_data['ozone'] > 0.070]
if not exceed_sites.empty:
    ax1.scatter(
        exceed_sites['CAMS_Long'], 
        exceed_sites['CAMS_Lat'],
        s=map_point_size * 1.2,  # Slightly larger
        facecolors='none',
        edgecolors='red',
        linewidths=line_width_value * 1.5,
        marker='o',
        zorder=11
    )


# Modify these size parameters for better label positioning
label_font_size = 7  # Even smaller font for better fit
label_pad = 0.4      # Smaller padding in text boxes
box_alpha = 0.85     # Slightly more opaque for better visibility
distance = 0.07      # Reduced label distance to fit more

# Add site labels with ozone values
for idx, row in ozone_data.iterrows():
    # Determine text color based on exceedance
    text_color = 'red' if row['ozone'] > 0.070 else 'blue'
    
    # Format CAMS number
    cams_num = row['CAMS_Num']
   
    
   
    angle = (cams_num % 12) * 30  #More angles for better distribution
    site_distance = distance * 0.9  
        # Calculate offset using trigonometry
    x_offset = site_distance * np.cos(np.radians(angle))
    y_offset = site_distance * np.sin(np.radians(angle))
        
        # Use connection lines to clearly show which label belongs to which point
    ax1.plot([row['CAMS_Long'], row['CAMS_Long'] + x_offset], 
                 [row['CAMS_Lat'], row['CAMS_Lat'] + y_offset],
                 color='gray', linestyle='-', linewidth=0.8, alpha=0.7, zorder=11)
        
        # Create more detailed label for key sites
    site_name_short = row['CAMS_Name'].split()[0]  # Just first word of name
    label_text = f"C{cams_num}: {site_name_short}\n{row['ozone']:.3f}"
        
        # Add label with ozone value and site name
    ax1.text(
            row['CAMS_Long'] + x_offset, 
            row['CAMS_Lat'] + y_offset, 
            label_text, 
            fontsize=label_font_size + 1,  # Slightly larger for key sites
            ha='center',
            va='center',
            color=text_color,
            weight='bold',
            bbox=dict(
                facecolor='white', 
                alpha=box_alpha, 
                edgecolor=text_color,
                pad=label_pad, 
                boxstyle='round,pad=0.3'
            ),
            zorder=13
        )
else:
        # For regular sites, use more compact labels
        # Calculate angle for better distribution - use more angles for better spacing
        angle = (cams_num % 12) * 30  # More angles for better distribution
        site_distance = distance * 0.9  # Slightly closer for regular sites
        
        # Calculate offset using trigonometry
        x_offset = site_distance * np.cos(np.radians(angle))
        y_offset = site_distance * np.sin(np.radians(angle))
        
        # Use thinner connection lines for regular sites
        ax1.plot([row['CAMS_Long'], row['CAMS_Long'] + x_offset], 
                 [row['CAMS_Lat'], row['CAMS_Lat'] + y_offset],
                 color='gray', linestyle='-', linewidth=0.5, alpha=0.5, zorder=11)
        
        # Simpler label text for regular sites
        label_text = f"C{cams_num}: {row['ozone']:.3f}"
        
        # Add label with just CAMS number and ozone value
        ax1.text(
            row['CAMS_Long'] + x_offset, 
            row['CAMS_Lat'] + y_offset, 
            label_text, 
            fontsize=label_font_size,
            ha='center',
            va='center',
            color=text_color,
            weight='normal',
            bbox=dict(
                facecolor='white', 
                alpha=box_alpha, 
                edgecolor='lightgray',
                pad=label_pad, 
                boxstyle='round,pad=0.2'
            ),
            zorder=12
        )

# Add a legend to explain the CAMS numbers and thresholds
from matplotlib.patches import Patch
from matplotlib.lines import Line2D

# Create a list of principal monitoring sites for the legend
important_sites = [
    {'cams': 8, 'name': 'Houston Aldine'},
    {'cams': 553, 'name': 'Crosby Library'},
    {'cams': 557, 'name': 'Mercer Arboretum'},
    {'cams': 561, 'name': 'Meyer Park'},
    {'cams': 698, 'name': 'UH WG Jones Forest'},
]

# Create legend elements for sites
legend_elements_sites = []
for site in important_sites:
    site_data = ozone_data[ozone_data['CAMS_Num'] == site['cams']]
    if not site_data.empty:
        color = 'red' if site_data.iloc[0]['ozone'] > 0.070 else 'blue'
        legend_elements_sites.append(
            Patch(facecolor='white', edgecolor=color,
                  label=f"C{site['cams']}: {site['name']}")
        )

# Create legend elements for thresholds
legend_elements_threshold = [
    Line2D([0], [0], marker='s', color='w', markerfacecolor='blue', 
           markeredgecolor='k', markersize=8, label='Below Threshold'),
    Line2D([0], [0], marker='s', color='w', markerfacecolor='red', 
           markeredgecolor='k', markersize=8, label='Exceeds Threshold (>0.070 ppm)'),
]

# Add the site legend in a good position
legend1 = ax1.legend(
    handles=legend_elements_sites,
    loc='lower right',
    title="Key Monitoring Sites",
    fontsize=8,
    title_fontsize=10,
    framealpha=0.85,
    facecolor='white'
)

# Add the threshold legend and keep the first legend
ax1.add_artist(legend1)
legend2 = ax1.legend(
    handles=legend_elements_threshold,
    loc='upper right',
    title="Ozone Levels",
    fontsize=8,
    title_fontsize=10,
    framealpha=0.85,
    facecolor='white'
)

# Add exceedance info to title
if not exceed_sites.empty:
    exceed_percent = (len(exceed_sites) / len(ozone_data)) * 100
    title = f'\n{exceed_percent:.1f}% of stations exceed EPA standard'

ax1.set_title(title, fontsize=label_size)

# Adjust layout and save
plt.tight_layout(pad=.5)

# Save first, then display
output_path = os.path.join(output_dir, f'HGB-ozone-map-{month_name}{target_day}-{year}.png')
plt.savefig(output_path, dpi=300, bbox_inches='tight')
print(f"Map saved to {output_path}")

# Also save to current directory for easy access
plt.savefig(output_path, dpi=300, bbox_inches='tight')
print(f"Map also saved to {os.path.abspath('ozone_map.png')}")

# Display plot - just like in your working script
plt.show()

print("Script completed successfully!")