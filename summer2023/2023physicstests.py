import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

import tkinter as tk

"""
CONFIGURATION
"""
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

def main():
    site25_data_path = "placeholder"
    with open("config.txt") as config:
        print(config.readline().rstrip())
        site25_data_path = config.readline().rstrip()
        print(config.readline().rstrip())
        site188_data_path = config.readline().rstrip()

    site25_no2_df = pd.read_csv(site25_data_path)
    site188_no2_df = pd.read_csv(site188_data_path)

    refined_25no2_0 = site25_no2_df[site25_no2_df[' Data_quality_flag'] == 0]
    refined_25no2_10 = site25_no2_df[site25_no2_df[' Data_quality_flag'] == 10]
    refined_188no2_0 = site188_no2_df[site188_no2_df[' Data_quality_flag'] == 0]
    refined_188no2_10 = site188_no2_df[site188_no2_df[' Data_quality_flag'] == 10]

    site25no2 = pd.concat([refined_25no2_0, refined_25no2_10])
    site188no2 = pd.concat([refined_188no2_0, refined_188no2_10])

    pd.to_datetime(site25no2[' Datetime'])
    pd.to_datetime(site188no2[' Datetime'])
    print(site25no2.dtypes)

    plt.scatter(' Datetime', ' NO2_total_vertical_column', data=site25no2.loc[1:900], s=1)
    plt.scatter(' Datetime', ' NO2_total_vertical_column', data=site188no2.loc[1:900], s=1)

    plt.show()


    # Here go the commands, may want to modularize the code somewhat

    plt.show()


if __name__ == "__main__":
    main()