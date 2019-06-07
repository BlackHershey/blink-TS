
# coding: utf-8
# Author(s): Haley Botteron


import numpy as np
get_ipython().magic(u'matplotlib inline')
import matplotlib.pyplot as plt
import pylab
from pylab import plot, ylim, xlim, show, xlabel, ylabel, grid
import csv

def zscore(name):
    filename=  name + 'Ratings.txt'
    with open (filename, 'rb') as datafile:
        Urge = []

        ratings = np.genfromtxt(datafile, delimiter = '\t', names=True,dtype=None)
        for i in range (len(ratings['block'])-1):
                Urge.append(ratings['discomfort'][i])
        SD = np.std(Urge)
        print SD
        Avg = np.average(Urge)
        z = []
        for i in range (len(ratings['block'])):
                zScore = ((ratings['discomfort'][i]) - Avg)/ SD
                z.append(zScore)
    print SD, Avg

    points = zip(ratings['time'], z)
    with open('zscore'+name+'.txt', 'w') as f:
        writer = csv.writer(f)
        writer.writerows(points)

    #plot to visualize
    plot((ratings['time']), ratings['discomfort'])
    plot((ratings['time']), z)
