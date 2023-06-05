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
    data_path = "placeholder"
    with open("config.txt") as config:
        print(config.readline().rstrip())
        data_path = config.readline().rstrip()

    no2_df = pd.read_csv(data_path)
    no2_day_df = no2_df[no2_df[' Datetime'] > 7942]
    # print(no2_df)
    # print(no2_df.shape)
    # print(no2_df.columns)
    print(no2_df[' Datetime'])
    plt.scatter(' Solar_zenith', ' NO2_total_vertical_column', data=no2_df, s=2)
    plt.xlabel("Solar_zenith")
    plt.ylabel("Total vertical column NO2 in moles/m^2")
    plt.yticks()
    plt.show()
    print(no2_df.columns)


if __name__ == "__main__":
    main()