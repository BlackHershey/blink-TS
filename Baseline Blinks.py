
# coding: utf-8
# Authors: Haley Botteron

import pylab
import numpy as np
import matplotlib.pyplot as plt
from pylab import plot, ylim, xlim, show, xlabel, ylabel, grid
from scipy.interpolate import UnivariateSpline
get_ipython().magic(u'matplotlib inline')
import csv


def blinks_baseline(name,threshold):   # Enter 'name'  as a string, i.e. in quotes
    import csv
    filename = name + '_BaseBlinks.txt'
    with open (filename, 'rb') as datafile:
        data = np.genfromtxt(datafile, delimiter = '\t', names=True,dtype=None)
    Blinks=[]
    #not every subject has exact same header so trying to call by comlumn - has an error
    data[:8,]

    for i in range (len(data['rmse'])):
        if np.any(data['rmse'][i] >= threshold or data['false_negative'][i] == 1):
            if np.any(data['false_positive'][i] == 0):
            # then we're in a blink
                Blinks.append(data['time'][i])
    #  When this finishes, Blinks is a vector in which every entry is a time point when
    #    the eyes are close

    blinksfilename = 'BaselineBlinks'+name+'.txt'
    writer = csv.writer(open(blinksfilename, 'w'), dialect='excel')
    for timevalue in Blinks:
        writer.writerow([timevalue])


def base_zeroes_ones(name, threshold):
    filename = name + '_BaseBlinks.txt'
    with open (filename, 'rb') as datafile:
        data = np.genfromtxt(datafile, delimiter = '\t', names=True,dtype=None)
    Blinks=[]
    time = []
    #not every subject has exact same header so trying to call by comlumn - has an error
    data[:8,]

    for i in range (len(data['false_positive'])):
        if np.any(data['rmse'][i] >= threshold or data['false_negative'][i] == 1):

            if np.any(data['false_positive'][i] == 0):
            # then we're in a blink
                Blinks.append(1)
                time.append(data['time'][i])
            else:
                Blinks.append(0)
                time.append(data['time'][i])
        else:
            Blinks.append(0)
            time.append(data['time'][i])
        if(np.isnan(data['time'][i]))==True:
                break




    #  When this finishes, Blinks is a vector in which every entry is a time point when
    #    the eyes are close

    points = zip(time, Blinks)
    with open('BaselineBlink-0,1'+name+'.txt', 'w') as f:
        writer = csv.writer(f)
        writer.writerows(points)


def blinkList(name):
    filename1 = 'Blinks' + name + '.txt'
    blinkList = []
    with open (filename1, 'rb') as datafile:
        blink = np.genfromtxt(datafile, delimiter = '\t')
        blinkList.append(blink[0])
        for i in range (len(blink)):
            if (blink[i] -(blink[i-1]) > .05):
                blinkList.append(blink[i])


    blinklistfilename = 'BlinkList'+name+'.txt'
    writer = csv.writer(open(blinklistfilename, 'w'), dialect='excel')
    for timevalue in blinkList:
        writer.writerow([timevalue])


def base_cheryl_rewrite(name,fps):

    filename = 'BaselineBlink-0,1'+name+'.txt'
    with open (filename, 'rb') as datafile:
        data = np.genfromtxt(datafile, delimiter = ',')
        data_new = np.transpose(data)
        filename1 = 'BaselineBlinks' + name + '.txt'
        blinkList = []
        with open (filename1, 'rb') as datafile:
            blink = np.genfromtxt(datafile, delimiter = '\t')
        blinkList.append(blink[0])
        for i in range (len(blink)):
            if (blink[i] -(blink[i-1]) > .05):
                blinkList.append(blink[i])
        count = 0
        freq = []
        timelen = 0
        timelength = []
        freqLess = []
        freqGreater = []
        timelast = 0
        timeLast = []
        stop = 0


        for i in range (0,len(data)):
                if data_new[1][i]==1:
                    while data_new[1][i]==1:
                        count = count+1
                        break
                if data_new[1][i] == 0:
                    if data_new[1][i] == 0 and data_new[1][i-1] == 1 and [i-1] != -1:
                        if i==0:
                            continue
                        else:
                            timelast = data_new[0][i]
                            timeLast.append(timelast)
                    freq.append(count)
                    count =0
                    continue
        countShort = 0
        countLong = 0
        for i in range(len(freq)):
            if freq[i] > 0:
                print 'freq here', freq[i]
                timelen = float(float(freq[i])/fps)
                print timelen
                timelength.append(timelen)

                if timelen<.5:
                    freqGreater.append(countLong)
                    freqLess.append(1 + countShort)
                    countShort = countShort+1
                if timelen>=.5:
                    freqGreater.append(1 + countLong)
                    freqLess.append(countShort)
                    countLong = countLong+1
        print freq
        print len(freq)
        print freqGreater
        print len(freqGreater)
        print freqLess
        print len(freqLess)
        print timelength
        points = zip(blinkList,timeLast,timelength,freqLess,freqGreater)

        with open('CherylRewriteBase'+name+'.txt', 'w') as f:
            writer = csv.writer(f, delimiter='\t')
            writer.writerows(points)


def baseline_blink_rate(name, fps):
    filename1 = name+'_BaseBlinks.txt'
    with open (filename1, 'rb') as datafile:
        data = np.genfromtxt(datafile, delimiter = '\t')
        filename2 = 'BaselineBlinks'+name+'.txt'
        with open (filename2, 'rb') as datafile:
            blinks = np.genfromtxt(datafile, delimiter = '\t')
            a = int (len(data)-1)
            for i in range (len(data)):
                if data['time'][i] > 9.9 or data['time'][i] < 10.1:
                    a = i
                if data['time'][i] > 69.9 or data['time'][i] < 70.1:
                    b = i
            for i in range (a, b):
                if fps == 60:
                    timeinblinks = data['time'][i]*.016667
                    blinkRate = timeinblinks/(60)
                if fps == 30:
                    timeinblinks = data['time'][i]*.033333
                    blinkRate = timeinblinks/(60)
            print blinkRate
            return blinkRate
