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
    print(no2_df)
    print(no2_df.shape)
    print(no2_df.columns)
    print(no2_df["Datetime"])


if __name__ == "__main__":
    main()