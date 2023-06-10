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

    site25_no2_df = pd.read_csv(site25_data_path)
    no2_day_df = site25_no2_df[site25_no2_df[' Datetime'] > 7942]
    # print(site25_no2_df)
    # print(site25_no2_df.shape)
    # print(site25_no2_df.columns)
    plt.scatter(' Solar_zenith', ' NO2_total_vertical_column', data=site25_no2_df, s=2)
    plt.xlabel("Solar_zenith")
    plt.ylabel("Total vertical column NO2 in moles/m^2")
    plt.yticks()
    plt.show()
    print(site25_no2_df.columns)


if __name__ == "__main__":
    main()