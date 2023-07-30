import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
from datetime import datetime
import tkinter as tk
from tkinter import ttk

"""
GLOBAL VARIABLES
"""
OZONE_SITES = ['C1_2', 'C8_2', 'C15_3', 'C26_2', 'C35_1',
       'C45_1', 'C53_1', 'C78_1', 'C84_1', 'C403_3', 'C405_1', 'C406_1',
       'C408_2', 'C409_2', 'C410_1', 'C416_1', 'C603_1', 'C603_2', 'C603_3',
       'C617_1', 'C620_1', 'C1015_1', 'C1016_1', 'C1034_1']

TIME_TICKS = ['00:00:00','03:00:00', '06:00:00','09:00:00', '12:00:00','15:00:00', '18:00:00', '21:00:00']
DATE_TICKS = ['21/08/01','21/08/15','21/09/01','21/09/15','21/10/01','21/10/15','21/11/01', '21/11/15']
DATETIME_TICKS = ['21/08/01 00:00:00', '21/08/02 00:00:00', '21/08/03 00:00:00', '21/08/04 00:00:00',
                  '21/08/05 00:00:00', '21/08/06 00:00:00', '21/08/07 00:00:00', '21/08/08 00:00:00',
                  '21/08/09 00:00:00', '21/08/10 00:00:00', '21/08/11 00:00:00', '21/08/12 00:00:00',
                  '21/08/13 00:00:00', '21/08/14 00:00:00', '21/08/15 00:00:00', '21/08/16 00:00:00',
                  '21/08/17 00:00:00', '21/08/18 00:00:00', '21/08/19 00:00:00', '21/08/20 00:00:00',
                  '21/08/21 00:00:00', '21/08/22 00:00:00', '21/08/23 00:00:00', '21/08/24 00:00:00',
                  '21/08/25 00:00:00', '21/08/26 00:00:00', '21/08/27 00:00:00', '21/08/28 00:00:00',
                  '21/08/29 00:00:00', '21/08/30 00:00:00', '21/08/31 00:00:00', '21/09/01 00:00:00',
                  '21/09/03 00:00:00', '21/09/04 00:00:00', '21/09/05 00:00:00', '21/09/06 00:00:00',
                  '21/09/07 00:00:00', '21/09/08 00:00:00', '21/09/09 00:00:00', '21/09/10 00:00:00',
                  '21/09/11 00:00:00', '21/09/12 00:00:00', '21/09/13 00:00:00', '21/09/14 00:00:00',
                  '21/09/15 00:00:00', '21/09/16 00:00:00', '21/09/17 00:00:00', '21/09/18 00:00:00',
                  '21/09/19 00:00:00', '21/09/20 00:00:00', '21/09/21 00:00:00', '21/09/22 00:00:00',
                  '21/09/23 00:00:00', '21/09/24 00:00:00', '21/09/25 00:00:00', '21/09/26 00:00:00',
                  '21/09/27 00:00:00', '21/09/28 00:00:00', '21/09/29 00:00:00', '21/09/30 00:00:00',
                  '21/10/01 00:00:00', '21/10/02 00:00:00', '21/10/03 00:00:00', '21/10/04 00:00:00',
                  '21/10/05 00:00:00', '21/10/06 00:00:00', '21/10/07 00:00:00', '21/10/08 00:00:00',
                  '21/10/09 00:00:00', '21/10/10 00:00:00', '21/10/11 00:00:00', '21/10/12 00:00:00',
                  '21/10/13 00:00:00', '21/10/14 00:00:00', '21/10/15 00:00:00', '21/10/16 00:00:00',
                  '21/10/17 00:00:00', '21/10/18 00:00:00', '21/10/19 00:00:00', '21/10/20 00:00:00',
                  '21/10/21 00:00:00', '21/10/22 00:00:00', '21/10/23 00:00:00', '21/10/24 00:00:00',
                  '21/10/25 00:00:00', '21/10/26 00:00:00', '21/10/27 00:00:00', '21/10/28 00:00:00',
                  '21/10/29 00:00:00', '21/10/30 00:00:00', '21/10/31 00:00:00', '21/11/01 00:00:00']

"""
CONFIGURATION
"""
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)


"""
FUNCTION DEFINITIONS
"""
def header_processor(header_file):
    """
    Given a filepath returns a dataframe of header info
    """
    with open(header_file) as file_obj:
        for i in range(22):
            #print(file_obj.readline().rstrip())
            file_obj.readline().rstrip()
        header_info = file_obj.readlines()
        header_df = pd.Series(header_info)
        #print(header_df)
        return header_df

def dataframe_loader():
    with open("config.txt") as config:
        # Reading in the file locations
        print(config.readline().rstrip())
        site25_data_path = config.readline().rstrip()
        print(config.readline().rstrip())
        site188_data_path = config.readline().rstrip()
        print(config.readline().rstrip())
        pgn25_data_path = config.readline().rstrip()
        print(config.readline().rstrip())
        pgn25_header_path = config.readline().rstrip()
        print(config.readline().rstrip())
        moody_surfacedata_path = config.readline().rstrip()

    # Dataframe creation
    site25_no2_df = pd.read_csv(site25_data_path)
    site188_no2_df = pd.read_csv(site188_data_path)
    pgn25_df = pd.read_csv(pgn25_data_path, delim_whitespace=True)
    pgnhead = header_processor(pgn25_header_path)
    moody_df = pd.read_csv(moody_surfacedata_path, parse_dates=[['dateGMT', 'timeGMT']], date_format='%y%m%d', keep_date_col=True) # Can I use this to parse the datetime?

    refined_25no2_0 = site25_no2_df[site25_no2_df[' Data_quality_flag'] == 0]
    refined_25no2_10 = site25_no2_df[site25_no2_df[' Data_quality_flag'] == 10]
    refined_188no2_0 = site188_no2_df[site188_no2_df[' Data_quality_flag'] == 0]
    refined_188no2_10 = site188_no2_df[site188_no2_df[' Data_quality_flag'] == 10]

    # Adds the 0 flagged data points to the 10 flagged data points
    site25no2 = pd.concat([refined_25no2_0, refined_25no2_10])
    site188no2 = pd.concat([refined_188no2_0, refined_188no2_10])

    # Should be converting the datetime to something readable
    site25no2[' Datetime'] = pd.to_datetime(site25no2[' Datetime'],unit='D', origin='2000-01-01')
    site188no2[' Datetime'] = pd.to_datetime(site188no2[' Datetime'], unit='D', origin='2000-01-01')

    return site25no2, site188no2, pgnhead, pgn25_df, moody_df


def graph_plotter(df, x, y):
    # Takes a dataframe and x and y variable names and graphs it over the time period
    plt.scatter(x, y, data=df, s=1, cmap='hsv')
    plt.title('Houston Atmospheric Measurement Data')
    plt.xticks(rotation=45)
    if x == 'dateGMT':
        plt.xlabel('Date')
    elif x == 'timeGMT':
        plt.xlabel('Time')
    else:
        plt.xlabel(x)

    plt.ylabel(y)
    plt.show()
    return

def gui_maker():
    root = tk.Tk()
    frame = ttk.Frame(master=root,padding=10)
    frame.grid()
    ttk.Button(frame, text="Plot", command=root.destroy).grid(column=1, row=0)
    ttk.Combobox(frame).grid(column=2, row=0)
    root.mainloop()


def main():
    plt.rcParams["figure.figsize"] = (12,8)

    site25no2, site188no2, pgnhead, pgn25_df, moody_df = dataframe_loader()
    plt.scatter('dateGMT_timeGMT', 'O3_O3conc_value', data=moody_df, s=1)
    plt.xticks(DATETIME_TICKS, rotation=45)
    plt.xlabel('DateTime (GMT)')
    plt.ylabel('Ozone Concentration')
    plt.show()
    #print(moody_df.columns)
    #window = gui_maker()

if __name__ == "__main__":
    main()