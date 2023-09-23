import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
from datetime import datetime
import tkinter as tk
from tkinter import ttk

"""
GLOBAL VARIABLES
"""
DATETIME_FORMAT = '%y/%m/%d %H:%M:%S'

OZONE_SITES = ['C1_2', 'C8_2', 'C15_3', 'C26_2', 'C35_1',
       'C45_1', 'C53_1', 'C78_1', 'C84_1', 'C403_3', 'C405_1', 'C406_1',
       'C408_2', 'C409_2', 'C410_1', 'C416_1', 'C603_1', 'C603_2', 'C603_3',
       'C617_1', 'C620_1', 'C1015_1', 'C1016_1', 'C1034_1']

TIME_TICKS = ['00:00:00','03:00:00', '06:00:00','09:00:00', '12:00:00','15:00:00', '18:00:00', '21:00:00']
DATE_TICKS = ['21/08/01','21/08/15','21/09/01','21/09/15','21/10/01','21/10/15','21/11/01', '21/11/15']
DATETIME_TICKS = pd.Series(['21/08/05 00:00:00', '21/08/20 00:00:00', '21/09/05 00:00:00', '21/09/20 00:00:00',
                  '21/10/05 00:00:00', '21/10/20 00:00:00', '21/11/05 00:00:00'], dtype="datetime64[ns]")

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
        print(config.readline().rstrip() + " initialized")
        site25_data_path = config.readline().rstrip()
        print(config.readline().rstrip() + " initialized")
        site188_data_path = config.readline().rstrip()
        print(config.readline().rstrip() + " initialized")
        pgn25_data_path = config.readline().rstrip()
        print(config.readline().rstrip() + " initialized")
        pgn25_header_path = config.readline().rstrip()
        print(config.readline().rstrip() + " initialized")
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

    site25dates = pd.Series(site25no2[' Datetime'])
    site188dates = pd.Series(site188no2[' Datetime'])
    moody_dates = pd.Series(moody_df['dateGMT_timeGMT'])

    # Should be converting the datetime to something readable
    # site25dates = site25dates.apply(pd.to_datetime(site25dates, unit='D', origin='2000-01-01'))
    # site188dates = site188dates.apply(pd.to_datetime(site188dates, unit='D', origin='2000-01-01'))
    # moody_dates = moody_dates.apply(pd.to_datetime(moody_dates, format=DATETIME_FORMAT))

    site25dates = site25dates.apply(pd.to_datetime, unit='D', origin='2000-01-01')
    site188dates = site188dates.apply(pd.to_datetime, unit='D', origin='2000-01-01')
    moody_dates = moody_dates.apply(pd.to_datetime, format=DATETIME_FORMAT)

    site25no2[' Datetime'] = site25dates
    site188no2[' Datetime'] = site188dates
    moody_df['dateGMT_timeGMT'] = moody_dates

    #print(site25no2[' Datetime'])

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

    site25no2, site188no2, pgnhead, pgn25_df, moody_df = dataframe_loader()

    fig, ax1 = plt.subplots()

    ax1.set_xlabel("Datetime")
    ax1.set_ylabel("NO2 Total Vertical Column")



    plt.xticks(DATETIME_TICKS, rotation=30)

    ax1.scatter(' Datetime', ' NO2_total_vertical_column', data=site25no2, s=1)
    ax1.scatter(' Datetime', ' NO2_total_vertical_column', data=site188no2, s=1)

    ax2 = ax1.twinx()
    ax2.set_ylabel("NO2 Concentration (Moody Tower)")

    ax2.scatter('dateGMT_timeGMT', 'NOx_NO2conc_value', data=moody_df, s=1)



    plt.xlabel('Datetime (GMT)')
    plt.ylabel('NO2 Concentration')
    plt.title('NO2 Concentration: Moody Tower | NO2 Total Vertical Column Pandora sites 25 and 188')
    #plt.legend()

    plt.show()
    #print(moody_df.columns)
    #window = gui_maker()

if __name__ == "__main__":
    main()