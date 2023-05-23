import pandas as pd
import matplotlib as mpl

import tkinter as tk


def main():
    with open("config.txt") as config:
        print(config.readline().rstrip())
        data_path = config.readline().rstrip()
        print(data_path)


if __name__ == "__main__":
    main()