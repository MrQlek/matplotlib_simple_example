#!/usr/bin/python3
"""Example to present how to draw charts using matplotlib"""

import matplotlib.pyplot as plt
from mpldatacursor import datacursor, HighlightingDataCursor

# prepere lists for all series x and y

x_series = []
linear = []
square = []


# get data from file
f = open("somedata.txt", "r")

for line in f.readlines():
    values = line.split(' ')

    try:
        x_series.append(float(values[0]))
        linear.append(float(values[1]))
        square.append(float(values[2]))
    except KeyError:
        pass

f.close()

# draw chart

FONT_SIZE = 10

# add handles to plots, they are needed to add legend
linear_func, = plt.plot(x_series, linear, label="linear function")
square_func, = plt.plot(x_series, square, label="square function")

plt.xlabel('X label', fontsize=FONT_SIZE)
plt.ylabel('Y label', fontsize=FONT_SIZE)
plt.tick_params(labelsize=FONT_SIZE)  # change size of numbers under axis
plt.legend(handles=[linear_func, square_func], fontsize=FONT_SIZE)
plt.grid()

# to use mpldatacursor you need to install matplotlib ver=3.2.2 or older

# datacursor()  # add cursor to all plots (you can specify plots using handles)
# datacursor(display='multiple', draggable=True)
# HighlightingDataCursor([linear_func, square_func])
datacursor(bbox=None, formatter='{x:.2f},{y:.2f}'.format)

plt.show()

"""If you want to create subplots in one pane go to
matplotlib.org/3.1.0/gallery/subplots_axes_and_figures/subplots_demo.html"""
