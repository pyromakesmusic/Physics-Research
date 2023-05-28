import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

import tkinter as tk


def main():
    data_path = "placeholder"
    with open("config.txt") as config:
        print(config.readline().rstrip())
        data_path = config.readline().rstrip()

    no2_df = pd.read_csv(data_path)
    print(no2_df)
    print(no2_df.shape)
    print(no2_df.columns)
    plt.plot(no2_df['N02_total_vertical_column'])


if __name__ == "__main__":
    main()