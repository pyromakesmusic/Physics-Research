import pandas as pd
import matplotlib as mpl

import tkinter as tk


def main():
    data_path = "placeholder"
    with open("config.txt") as config:
        print(config.readline().rstrip())
        data_path = config.readline().rstrip()

    with open(data_path) as no2_file:
        for i in range(47):
            print(no2_file.readline().rstrip())

        print("=========== \n BREAK BREAK BREAK BREAK BREAK \n ============")
        linelists = []

        for line in no2_file.readlines():
            linelists.append(pd.Series(line))
        no2_df = pd.DataFrame(no2_file.readlines(), columns=no2_file.readline())
        print(no2_df)


if __name__ == "__main__":
    main()