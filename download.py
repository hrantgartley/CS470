import sys, os
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def download(url, filename):
    cmd = "curl -o %s %s" % (filename, url)
    os.system(cmd)


def parse_args():
    if len(sys.argv) != 3:
        print("Usage: python download.py <url> <filename>")
        sys.exit(1)
    url = sys.argv[1]
    filename = sys.argv[2]
    return url, filename


def pandas_parse(filename):
    data = pd.read_csv(filename, usecols=[0, 1])
    return data


def main():
    url, filename = parse_args()
    download(url, filename)
    data = pandas_parse(filename)
    # instead of printing data use plt.plot to plot the data
    plt.plot(data)
