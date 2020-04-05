"""
CO370
Group 37 Project
tool.py
Example usage:
python tool.py --p="bracket.png star.png"
"""

# from scipy import misc -> DEPRECATED :C
import argparse
import csv
import imageio
import numpy as np

# Command-line argument setup
parser = argparse.ArgumentParser(description='Processes patterns for files.')
parser.add_argument('--p', help='Space-separated list of file names')
args = parser.parse_args()

file_list = [file for file in args.p.split(' ')]

# Example on how the imageio module works:
# arr = imageio.imread('bracket.png')
# arr[20, 30] produces a 4-vector for a pixel ie: (R,G,B,a)
# We ignore a (transparency alpha) for now.

# RGB to grayscale conversions
# We use a standard linear luma transform approximation
# to get a grayscale value
# Y' = 0.299R' + 0.587G' + 0.114B'
# 0 is black, 255 is white
def RGB_to_grayscale(rgb):
    rgb_list = list(rgb)
    R = rgb_list[0]
    G = rgb_list[1]
    B = rgb_list[2]
    grayscale =  0.2989*R + 0.5870*G + 0.1140*B
    return grayscale

def get_avg(prev_avg, x, n):
    return ((prev_avg * n + x) / (n + 1))

def process_image(arr):
    avg = 0
    n = 0
    g_arr = [[0]*len(r) for r in arr]
    for i in range(len(arr)):
        for v in range(len(arr[0])):
            g_arr[i][v] = RGB_to_grayscale(arr[i, v])
            avg = get_avg(avg, g_arr[i][v], n)
            n += 1
    return g_arr, avg

# Write to pattern file
with open("patterns.csv", mode="w") as pattern_f:
    f_writer = csv.writer(pattern_f)
    # (x,y) is coord of pixel
    # v is 1 or 0 if it is to be cut or not
    # p is (filename) which pattern it belongs to
    f_writer.writerow(["x", "y", "v", "p"])
    for f in file_list:
        arr = imageio.imread(f)
        g_arr, g_avg = process_image(arr)
        for i in range(len(arr)):
            for j in range(len(arr[0])):
                if g_arr[i][j] <= g_avg:
                    f_writer.writerow([i,j,1,f])
print("finished")