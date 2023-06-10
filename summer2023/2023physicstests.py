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

    print(site25_no2_df.dtypes)
    # Here go the commands, may want to modularize the code somewhat

    plt.show()


if __name__ == "__main__":
    main()