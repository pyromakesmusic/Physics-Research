import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

import tkinter as tk

"""
GLOBAL VARIABLES
"""
ozone_sites = ['C1_2', 'C8_2', 'C15_3', 'C26_2', 'C35_1',
       'C45_1', 'C53_1', 'C78_1', 'C84_1', 'C403_3', 'C405_1', 'C406_1',
       'C408_2', 'C409_2', 'C410_1', 'C416_1', 'C603_1', 'C603_2', 'C603_3',
       'C617_1', 'C620_1', 'C1015_1', 'C1016_1', 'C1034_1']

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

def main():
    with open("config.txt") as config:
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


    site25_no2_df = pd.read_csv(site25_data_path)
    site188_no2_df = pd.read_csv(site188_data_path)
    pgn25_df = pd.read_csv(pgn25_data_path, delim_whitespace=True)
    pgnhead = header_processor(pgn25_header_path)
    moody_df = pd.read_csv(moody_surfacedata_path)

    refined_25no2_0 = site25_no2_df[site25_no2_df[' Data_quality_flag'] == 0]
    refined_25no2_10 = site25_no2_df[site25_no2_df[' Data_quality_flag'] == 10]
    refined_188no2_0 = site188_no2_df[site188_no2_df[' Data_quality_flag'] == 0]
    refined_188no2_10 = site188_no2_df[site188_no2_df[' Data_quality_flag'] == 10]

    site25no2 = pd.concat([refined_25no2_0, refined_25no2_10])
    site188no2 = pd.concat([refined_188no2_0, refined_188no2_10])

    # Should be converting the datetime to something readable
    site25no2[' Datetime'] = pd.to_datetime(site25no2[' Datetime'],unit='D', origin='2000-01-01')
    site188no2[' Datetime'] = pd.to_datetime(site188no2[' Datetime'], unit='D', origin='2000-01-01')
    #pgn25_df.columns = pgnhead
    #print(pgn25_df.columns)

    # plt.scatter(' Datetime', ' NO2_total_vertical_column', data=site25no2.loc[8000:15000], s=1)
    # plt.scatter(' Datetime', ' NO2_total_vertical_column', data=site188no2.loc[8000:15000], s=1)
    # plt.scatter(pgn25_df.iloc[:,1], pgn25_df.iloc[:,38], s=1)

    print(moody_df.columns)
    plt.scatter('dateGMT', 'NOx_NO2conc_value', data=moody_df, s=1)
    plt.show()


    # Here go the commands, may want to modularize the code somewhat
    #print("Pandonia shape: ", pgn25_df.shape)


if __name__ == "__main__":
    main()