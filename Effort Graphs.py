
# coding: utf-8
# Author(s): Haley Botteron


get_ipython().magic(u'matplotlib inline')
import matplotlib.pyplot as plt
import pylab
import numpy as np
import pandas as pd
import csv
from pylab import plot, ylim, xlim, show, xlabel, ylabel, grid
from scipy.interpolate import UnivariateSpline
from __future__ import division
from pylab import plot, ylim, xlim, show, xlabel, ylabel, grid
from numpy import linspace, loadtxt, ones, convolve
from scipy import stats
import scipy as scipy


def resample_blinks(name):
    #in .25s blocks, create a fraction of how many points were spent in blink for 60fps its i =15
    filename = name+'_Effort.csv'
    with open (filename, 'rb') as datafile:
        ratings= np.genfromtxt(datafile, delimiter = ',')
        avgX = []
        avgY= []
        ratings_new = np.transpose(ratings)

        #need univariate spline because ratings are too slow and every fourth second skips a bin
        spl = UnivariateSpline(ratings_new[0], ratings_new[1])
        xs = np.linspace(.1250, 450.1250, 1800)
        spl.set_smoothing_factor(0.1)

        add = .125
        for i in range(450):
            block1 = []
            block2 = []
            block3 = []
            block4 = []
            timeblock1 = []
            timeblock2 = []
            timeblock3 = []
            timeblock4 = []
            #count1 =0.0
            #count2 =0.0
            #count3 =0.0
            #count4 =0.0
            for m in range (len(ratings)):

                if ratings[m][0]>=i and ratings[m][0] < i+.25:
                    timeblock1.append(i+.125)
                    block1.append(ratings[m][1])
                    #count1 = count1 +1.0

                if ratings[m][0] >= i+.25 and ratings[m][0]< i+.5:
                    timeblock2.append(i+.375)
                    block2.append(ratings[m][1])
                    #count2 = count2 +1.0

                if ratings[m][0] >= i+.5 and ratings[m][0]< i+.75:
                    timeblock3.append(i+.625)
                    block3.append(ratings[m][1])
                    #count3 = count3 +1.0

                if ratings[m][0] >= i+.75 and ratings[m][0]< i+1.0:
                    timeblock4.append(i+.875)
                    block4.append(ratings[m][1])
                    #count4 = count4 +1.0

            avgY.append(np.average(block1))
            avgY.append(np.average(block2))
            avgY.append(np.average(block3))
            avgY.append(np.average(block4))

            avgX.append(np.average(timeblock1))
            avgX.append(np.average(timeblock2))
            avgX.append(np.average(timeblock3))
            avgX.append(np.average(timeblock4))
        #print avgY, avgX
    ## This part corrects for the missing time value every 16 bins by averaging the value before and after
        for i in range (len(avgY)):
                if np.isnan(avgX[i])==True :
                    if avgY[i]== avgY[-1]:

                        avgX[i]= avgX[i-1]+0.25
                        avgY[i]= avgY[i-1]
                    if i ==0:
                        avgX[i]= avgX[i+1]-0.25
                        avgY[i]= avgY[i+1]
                    else:
                        avgX[i]= avgX[i-1]+0.25
                        avgY[i]= (avgY[i-1]+avgY[i+1])/2.0

                    #add = add +.25
        #print avgY, avgX
        #print block1
        trial1X1=[]
        trial2X1=[]
        trial3X1=[]
        trial4X1=[]
        trial5X1=[]
        trial1Y1=[]
        trial2Y1=[]
        trial3Y1=[]
        trial4Y1=[]
        trial5Y1=[]
        trial1Y2=[]
        trial2Y2=[]
        trial3Y2=[]
        trial4Y2=[]
        trial5Y2=[]
        time = 0;
        # NOTE: (90, 180, 270, 360, 450) include the don't-blink data. Otherwise use 60, 150, 240, 330, 420.

        for i in range (1800):
            if avgX[i] >0 and avgX[i]<=90:
                time = avgX[i]-0.0
                trial1X1.append(time)
                trial1Y1.append(avgY[i])
                trial1Y2.append(spl(avgX[i]))
            if avgX[i] >90 and avgX[i]<=180:
                time = avgX[i]-90.0
                trial2X1.append(time)
                trial2Y1.append(avgY[i])
                trial2Y2.append(spl(avgX[i]))
            if avgX[i] >180 and avgX[i]<=270:
                time =avgX[i]-180.0
                trial3X1.append(time)
                trial3Y1.append(avgY[i])
                trial3Y2.append(spl(avgX[i]))
            if avgX[i] >270 and avgX[i]<=360:
                time = avgX[i]-270.0
                trial4X1.append(time)
                trial4Y1.append(avgY[i])
                trial4Y2.append(spl(avgX[i]))
            if avgX[i] >360 and avgX[i]<=450:
                time = avgX[i]-360.0
                trial5X1.append(time)
                trial5Y1.append(avgY[i])
                trial5Y2.append(spl(avgX[i]))

        AvgXAll = []
        AvgYAll = []

        #print len(trial1X1),len(trial2X1),len(trial3X1),len(trial4X1),len(trial5X1)
        #print len(trial1Y1),len(trial2Y1),len(trial3Y1),len(trial4Y1),len(trial5Y1)
        for i in range (len(trial2Y1)):
            tot = trial1Y1[i]+trial2Y1[i]+trial3Y1[i]+trial4Y1[i]+trial5Y1[i]
            AvgYAll.append(tot/5)

        #print AvgYAll
        #print (avgX[:25])
        #print (avgY[:25])

        #points = zip(trial1X1, trial1Y1)
       # with open('ResampledEffort'+name+'_Trial1.txt', 'w') as f:
           # writer = csv.writer(f, delimiter='\t')
           # writer.writerows(points)
       # points = zip(trial2X1, trial2Y1)
       # with open('ResampledEffort'+name+'_Trial2.txt', 'w') as f:
         #   writer = csv.writer(f, delimiter='\t')
        #    writer.writerows(points)
       # points = zip(trial3X1, trial3Y1)
      #  with open('ResampledEffort'+name+'_Trial3.txt', 'w') as f:
       #     writer = csv.writer(f, delimiter='\t')
      #      writer.writerows(points)
      #  points = zip(trial4X1, trial4Y1)
       # with open('ResampledEffort'+name+'_Trial4.txt', 'w') as f:
       #     writer = csv.writer(f, delimiter='\t')
       #     writer.writerows(points)
       # points = zip(trial5X1, trial5Y1)
       # with open('ResampledEffort'+name+'_Trial5.txt', 'w') as f:
          #  writer = csv.writer(f, delimiter='\t')
          #  writer.writerows(points)
        points = zip(trial1X1,AvgYAll)
        with open('ResampledEffort'+name+'AvgTrials.txt', 'w') as f:
            writer = csv.writer(f, delimiter='\t')
            writer.writerows(points)
        #plot(trial1X1, trial1Y2 ,'--')
        #plot(trial2X1, trial2Y2 ,'--')
        #plot(trial3X1, trial3Y2 ,'--')
        #plot(trial4X1, trial4Y2 ,'--')
       # plot(trial5X1, trial5Y2 ,'--')
        plot(trial1X1, trial1Y1 ,'--',color ='0.5')
        plot(trial2X1, trial2Y1 ,'--',color = '0.5')
        plot(trial3X1, trial3Y1 ,'--',color = '0.5')
        plot(trial4X1, trial4Y1 ,'--',color = '0.5')
        plot(trial5X1, trial5Y1 ,'--',color = '0.5')
        plot(trial2X1, AvgYAll, '.', color='black', label = 'average effort')

        return trial2X1, AvgYAll


def resample_disc_blinks(name):
    #in .25s blocks, create a fraction of how many points were spent in blink for 60fps its i =15
    filename1 =  name + 'Ratings.txt'

    with open (filename1, 'rb') as datafile:
        ratings = np.genfromtxt(datafile, delimiter = '\t', names=True,dtype=None)
        avgX = []
        avgY= []

        add = .125
        for i in range(450):
            block1 = []
            block2 = []
            block3 = []
            block4 = []
            timeblock1 = []
            timeblock2 = []
            timeblock3 = []
            timeblock4 = []

            for m in range (len(ratings)):
                if ratings['time'][m]>=i and ratings['time'][m] < i+.25:
                    timeblock1.append(i+.125)
                    block1.append(ratings['discomfort'][m])

                if ratings['time'][m]>= i+.25 and ratings['time'][m]< i+.5:
                    timeblock2.append(i+.375)
                    block2.append(ratings['discomfort'][m])

                if ratings['time'][m] >= i+.5 and ratings['time'][m]< i+.75:
                    timeblock3.append(i+.625)
                    block3.append(ratings['discomfort'][m])

                if ratings['time'][m] >= i+.75 and ratings['time'][m]< i+1.0:
                    timeblock4.append(i+.875)
                    block4.append(ratings['discomfort'][m])


            avgY.append(np.average(block1))
            avgY.append(np.average(block2))
            avgY.append(np.average(block3))
            avgY.append(np.average(block4))

            avgX.append(np.average(timeblock1))
            avgX.append(np.average(timeblock2))
            avgX.append(np.average(timeblock3))
            avgX.append(np.average(timeblock4))
        #print avgY, avgX
    ## This part corrects for the missing time value every 16 bins by averaging the value before and after
        for i in range (len(avgY)):
            if np.isnan(avgX[i])==True :
                    avgX[i]= avgX[i-1]+0.25
                    avgY[i]= (avgY[i-1]+avgY[i+1])/2.0

                    #add = add +.25
       # print avgY, avgX
        #print block1
        trial1X1=[]
        trial2X1=[]
        trial3X1=[]
        trial4X1=[]
        trial5X1=[]
        trial1Y1=[]
        trial2Y1=[]
        trial3Y1=[]
        trial4Y1=[]
        trial5Y1=[]
        trial1Y2=[]
        trial2Y2=[]
        trial3Y2=[]
        trial4Y2=[]
        trial5Y2=[]
        time = 0;
        # NOTE: (90, 180, 270, 360, 450) include the don't-blink data. Otherwise use 60, 150, 240, 330, 420.

        for i in range (1800):
            if avgX[i] >0 and avgX[i]<=90:
                time = avgX[i]-0.0
                trial1X1.append(time)
                trial1Y1.append(avgY[i])

            if avgX[i] >90 and avgX[i]<=180:
                time = avgX[i]-90.0
                trial2X1.append(time)
                trial2Y1.append(avgY[i])

            if avgX[i] >180 and avgX[i]<=270:
                time =avgX[i]-180.0
                trial3X1.append(time)
                trial3Y1.append(avgY[i])

            if avgX[i] >270 and avgX[i]<=360:
                time = avgX[i]-270.0
                trial4X1.append(time)
                trial4Y1.append(avgY[i])

            if avgX[i] >360 and avgX[i]<=450:
                time = avgX[i]-360.0
                trial5X1.append(time)
                trial5Y1.append(avgY[i])


        AvgXAll = []
        AvgYAll = []

        #print len(trial1X1),len(trial2X1),len(trial3X1),len(trial4X1),len(trial5X1)
        #print trial1Y1,trial2Y1,len(trial3Y1),len(trial4Y1),len(trial5Y1)
        for i in range (len(trial2Y1)):
            tot = trial1Y1[i]+trial2Y1[i]+trial3Y1[i]+trial4Y1[i]+trial5Y1[i]
            AvgYAll.append(tot/5)



        #points = zip(trial1X1, trial1Y1)
       # with open('ResampledEffort'+name+'_Trial1.txt', 'w') as f:
           # writer = csv.writer(f, delimiter='\t')
           # writer.writerows(points)
       # points = zip(trial2X1, trial2Y1)
       # with open('ResampledEffort'+name+'_Trial2.txt', 'w') as f:
         #   writer = csv.writer(f, delimiter='\t')
        #    writer.writerows(points)
       # points = zip(trial3X1, trial3Y1)
      #  with open('ResampledEffort'+name+'_Trial3.txt', 'w') as f:
       #     writer = csv.writer(f, delimiter='\t')
      #      writer.writerows(points)
      #  points = zip(trial4X1, trial4Y1)
       # with open('ResampledEffort'+name+'_Trial4.txt', 'w') as f:
       #     writer = csv.writer(f, delimiter='\t')
       #     writer.writerows(points)
       # points = zip(trial5X1, trial5Y1)
       # with open('ResampledEffort'+name+'_Trial5.txt', 'w') as f:
          #  writer = csv.writer(f, delimiter='\t')
          #  writer.writerows(points)
        points = zip(trial1X1,AvgYAll)
        with open('ResampledDiscomfort'+name+'AvgTrials.txt', 'w') as f:
            writer = csv.writer(f, delimiter='\t')
            writer.writerows(points)

        plot(trial1X1, trial1Y1 ,'--',color = '0.75')
        plot(trial2X1, trial2Y1 ,'--',color = '0.75')
        plot(trial3X1, trial3Y1 ,'--',color = '0.75')
        plot(trial4X1, trial4Y1 ,'--',color = '0.75')
        plot(trial5X1, trial5Y1 ,'--',color = '0.75')
        plot(trial2X1, AvgYAll, '.', color='blue',label = 'average discomfort')
        plt.xlabel('time')
        plt.ylabel('Discomfort/Effort Rating')

        return trial2X1, AvgYAll
def correlation(name):
    avgXE, avgYDisc = resample_disc_blinks(name)
    avgXD, avgYEffort = resample_blinks(name)
    return scipy.stats.pearsonr(avgYEffort, avgYDisc)
