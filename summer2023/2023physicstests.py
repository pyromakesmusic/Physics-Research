import pandas as pd
import matplotlib as mpl

import tkinter as tk


def main():
    data_path = "placeholder"
    with open("config.txt") as config:
        print(config.readline().rstrip())
        data_path = config.readline().rstrip()

    with open(data_path) as no2_file:
        for i in range(46):
            print(no2_file.readline().rstrip())

        print("=========== \n BREAK BREAK BREAK BREAK BREAK \n ============")
        for line in no2_file:
            print(no2_file.readline().rstrip())


if __name__ == "__main__":
    main()