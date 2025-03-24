# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 18:06:58 2025

@author: paulj
"""


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

import matplotlib_inline
matplotlib_inline.backend_inline.set_matplotlib_formats('png', 'jpeg')
from matplotlib import rcParams
#rcParams['font.family'] = 'serif'
rcParams['font.family'] = 'arial'
rcParams['font.size'] = 20


# Function that replaces any non-numeric values with NaNs
def convert_columns_to_float(df):
    """
    Converts columns labeled 1 to the highest numbered column (up to 31) to float,
    replacing non-numeric values with NaN.

    Args:
        df (pd.DataFrame): The DataFrame to modify.

    Returns:
        pd.DataFrame: The modified DataFrame.
    """
    max_col = 0
    for col in df.columns:
        try:
            col_int = int(col)
            if 1 <= col_int <= 31: # check if the column is within the 1-31 range.
                max_col = max(max_col, col_int) # update max_col
        except ValueError:
            pass

    for col in df.columns:
        try:
            col_int = int(col)
            if 1 <= col_int <= max_col:
                df[col] = pd.to_numeric(df[col], errors='coerce')
        except ValueError:
            pass

    return df



###############################################################################
#####################  Read in data file  #####################################
###############################################################################


data_file_path1 = "../Data/MDA8_O3/HGB_MDA8-O3_201009.txt" 

try:
  df1 = pd.read_csv(data_file_path1, skiprows=1)
  df1 = convert_columns_to_float(df1)
except ValueError as e:
  print(f"Error reading file: {e}")

