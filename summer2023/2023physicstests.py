import pandas as pd
import matplotlib as mpl

import tkinter as tk


def main():
    data_path = "placeholder"
    with open("config.txt") as config:
        print(config.readline().rstrip())
        data_path = config.readline().rstrip()

    no2_df = pd.read_csv(data_path)
    print(no2_df)


if __name__ == "__main__":
    main()