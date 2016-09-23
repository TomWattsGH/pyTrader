import mmap
import threading

import multiprocessing as mp

from os import getpid

import numpy as np
import csv
from matplotlib import pyplot as plt
import matplotlib as mpl
import matplotlib.animation as animation
import time
import datetime
import math

from numpy.random import randn

import statsmodels.tsa.stattools as ts
from numpy import cumsum, log, polyfit, sqrt, std, subtract

##----------------------------------- Global Variables  --------------------------------------##

pink = '#ff3399'
pink2 = '#ff3385'
purple2 = '#8533ff'
purple = '#884dff'
blue = '#668cff'
blue2 ='#8533ff'
fuschia = '#ff66a3'
grey = '#595959'
red = '#FF0066'

colours = []
colours.append('#6600cc')
colours.append('#9900cc')
colours.append('#9900ff')
colours.append('#cc00cc')
colours.append('#ff00ff')
colours.append('#ff33cc')
colours.append('#ff3399')
colours.append('#ff4d94')


### 1 minute Data ##################################################################################################

### S&P500

SPX = []
SPX.append('/home/squishy/Desktop/data/1min yearly/SPX/HISTDATA_COM_MT_SPXUSD_M12010/DAT_MT_SPXUSD_M1_2010.csv')
SPX.append('/home/squishy/Desktop/data/1min yearly/SPX/HISTDATA_COM_MT_SPXUSD_M12011/DAT_MT_SPXUSD_M1_2011.csv')
SPX.append('/home/squishy/Desktop/data/1min yearly/SPX/HISTDATA_COM_MT_SPXUSD_M12012/DAT_MT_SPXUSD_M1_2012.csv')
SPX.append('/home/squishy/Desktop/data/1min yearly/SPX/HISTDATA_COM_MT_SPXUSD_M12013/DAT_MT_SPXUSD_M1_2013.csv')
SPX.append('/home/squishy/Desktop/data/1min yearly/SPX/HISTDATA_COM_MT_SPXUSD_M12014/DAT_MT_SPXUSD_M1_2014.csv')
SPX.append('/home/squishy/Desktop/data/1min yearly/SPX/HISTDATA_COM_MT_SPXUSD_M12015/DAT_MT_SPXUSD_M1_2015.csv')



SPX2010 = '/home/squishy/Desktop/data/1min yearly/HISTDATA_COM_MT_SPXUSD_M12010/DAT_MT_SPXUSD_M1_2010.csv'
SPX2011 = '/home/squishy/Desktop/data/1min yearly/HISTDATA_COM_MT_SPXUSD_M12011/DAT_MT_SPXUSD_M1_2011.csv'
SPX2012 = '/home/squishy/Desktop/data/1min yearly/HISTDATA_COM_MT_SPXUSD_M12012/DAT_MT_SPXUSD_M1_2012.csv'
SPX2013 = '/home/squishy/Desktop/data/1min yearly/HISTDATA_COM_MT_SPXUSD_M12013/DAT_MT_SPXUSD_M1_2013.csv'
SPX2014 = '/home/squishy/Desktop/data/1min yearly/HISTDATA_COM_MT_SPXUSD_M12014/DAT_MT_SPXUSD_M1_2014.csv'
SPX2015 = '/home/squishy/Desktop/data/1min yearly/HISTDATA_COM_MT_SPXUSD_M12015/DAT_MT_SPXUSD_M1_2015.csv'

### JP225
JP225 = []

JP225.append('/home/squishy/Desktop/data/1min yearly/JPX/HISTDATA_COM_MT_JPXJPY_M12010/DAT_MT_JPXJPY_M1_2010.csv')
JP225.append('/home/squishy/Desktop/data/1min yearly/JPX/HISTDATA_COM_MT_JPXJPY_M12011/DAT_MT_JPXJPY_M1_2011.csv')
JP225.append('/home/squishy/Desktop/data/1min yearly/JPX/HISTDATA_COM_MT_JPXJPY_M12012/DAT_MT_JPXJPY_M1_2012.csv')
JP225.append('/home/squishy/Desktop/data/1min yearly/JPX/HISTDATA_COM_MT_JPXJPY_M12013/DAT_MT_JPXJPY_M1_2013.csv')
JP225.append('/home/squishy/Desktop/data/1min yearly/JPX/HISTDATA_COM_MT_JPXJPY_M12014/DAT_MT_JPXJPY_M1_2014.csv')
JP225.append('/home/squishy/Desktop/data/1min yearly/JPX/HISTDATA_COM_MT_JPXJPY_M12015/DAT_MT_JPXJPY_M1_2015.csv')



### Yen
USDJPY2008 = '/home/squishy/Desktop/data/1min yearly/USDJPY/HISTDATA_COM_MT_USDJPY_M12008/DAT_MT_USDJPY_M1_2008.csv'
USDJPY2009 = '/home/squishy/Desktop/data/1min yearly/USDJPY/HISTDATA_COM_MT_USDJPY_M12009/DAT_MT_USDJPY_M1_2009.csv'
USDJPY2010 = '/home/squishy/Desktop/data/1min yearly/USDJPY/HISTDATA_COM_MT_USDJPY_M12010/DAT_MT_USDJPY_M1_2010.csv'
USDJPY2011 = '/home/squishy/Desktop/data/1min yearly/USDJPY/HISTDATA_COM_MT_USDJPY_M12011/DAT_MT_USDJPY_M1_2011.csv'
USDJPY2012 = '/home/squishy/Desktop/data/1min yearly/USDJPY/HISTDATA_COM_MT_USDJPY_M12012/DAT_MT_USDJPY_M1_2012.csv'
USDJPY2013 = '/home/squishy/Desktop/data/1min yearly/USDJPY/HISTDATA_COM_MT_USDJPY_M12013/DAT_MT_USDJPY_M1_2013.csv'
USDJPY2014 = '/home/squishy/Desktop/data/1min yearly/USDJPY/HISTDATA_COM_MT_USDJPY_M12014/DAT_MT_USDJPY_M1_2014.csv'
USDJPY2015 = '/home/squishy/Desktop/data/1min yearly/USDJPY/HISTDATA_COM_MT_USDJPY_M12015/DAT_MT_USDJPY_M1_2015.csv'

### EURUSD
EURUSD2008 = '/home/squishy/Desktop/data/1min yearly/HISTDATA_COM_MT_EURUSD_M12008/DAT_MT_EURUSD_M1_2008.csv'
EURUSD2009 = '/home/squishy/Desktop/data/1min yearly/HISTDATA_COM_MT_EURUSD_M12009/DAT_MT_EURUSD_M1_2009.csv'
EURUSD2010 = '/home/squishy/Desktop/data/1min yearly/HISTDATA_COM_MT_EURUSD_M12010/DAT_MT_EURUSD_M1_2010.csv'
EURUSD2011 = '/home/squishy/Desktop/data/1min yearly/HISTDATA_COM_MT_EURUSD_M12011/DAT_MT_EURUSD_M1_2011.csv'
EURUSD2012 = '/home/squishy/Desktop/data/1min yearly/HISTDATA_COM_MT_EURUSD_M12012/DAT_MT_EURUSD_M1_2012.csv'
EURUSD2013 = '/home/squishy/Desktop/data/1min yearly/HISTDATA_COM_MT_EURUSD_M12013/DAT_MT_EURUSD_M1_2013.csv'
EURUSD2014 = '/home/squishy/Desktop/data/1min yearly/HISTDATA_COM_MT_EURUSD_M12014/DAT_MT_EURUSD_M1_2014.csv'
EURUSD2015 = '/home/squishy/Desktop/data/1min yearly/HISTDATA_COM_MT_EURUSD_M12015/DAT_MT_EURUSD_M1_2015.csv'

### NZDUSD
NZDUSD2008 = '/home/squishy/Desktop/data/1min yearly/HISTDATA_COM_MT_NZDUSD_M12008/DAT_MT_NZDUSD_M1_2008.csv'
NZDUSD2009 = '/home/squishy/Desktop/data/1min yearly/HISTDATA_COM_MT_NZDUSD_M12009/DAT_MT_NZDUSD_M1_2009.csv'
NZDUSD2010 = '/home/squishy/Desktop/data/1min yearly/HISTDATA_COM_MT_NZDUSD_M12010/DAT_MT_NZDUSD_M1_2010.csv'
NZDUSD2011 = '/home/squishy/Desktop/data/1min yearly/HISTDATA_COM_MT_NZDUSD_M12011/DAT_MT_NZDUSD_M1_2011.csv'
NZDUSD2012 = '/home/squishy/Desktop/data/1min yearly/HISTDATA_COM_MT_NZDUSD_M12012/DAT_MT_NZDUSD_M1_2012.csv'
NZDUSD2013 = '/home/squishy/Desktop/data/1min yearly/HISTDATA_COM_MT_NZDUSD_M12013/DAT_MT_NZDUSD_M1_2013.csv'
NZDUSD2014 = '/home/squishy/Desktop/data/1min yearly/HISTDATA_COM_MT_NZDUSD_M12014/DAT_MT_NZDUSD_M1_2014.csv'
NZDUSD2015 = '/home/squishy/Desktop/data/1min yearly/HISTDATA_COM_MT_NZDUSD_M12015/DAT_MT_NZDUSD_M1_2015.csv'

EURNZD2008 = '/home/squishy/Desktop/data/1min yearly/EURNZD/HISTDATA_COM_MT_EURNZD_M12008/DAT_MT_EURNZD_M1_2008.csv'
EURNZD2009 = '/home/squishy/Desktop/data/1min yearly/EURNZD/HISTDATA_COM_MT_EURNZD_M12009/DAT_MT_EURNZD_M1_2009.csv'
EURNZD2010 = '/home/squishy/Desktop/data/1min yearly/EURNZD/HISTDATA_COM_MT_EURNZD_M12010/DAT_MT_EURNZD_M1_2010.csv'
EURNZD2011 = '/home/squishy/Desktop/data/1min yearly/EURNZD/HISTDATA_COM_MT_EURNZD_M12011/DAT_MT_EURNZD_M1_2011.csv'
EURNZD2012 = '/home/squishy/Desktop/data/1min yearly/EURNZD/HISTDATA_COM_MT_EURNZD_M12012/DAT_MT_EURNZD_M1_2012.csv'
EURNZD2013 = '/home/squishy/Desktop/data/1min yearly/EURNZD/HISTDATA_COM_MT_EURNZD_M12013/DAT_MT_EURNZD_M1_2013.csv'
EURNZD2014 = '/home/squishy/Desktop/data/1min yearly/EURNZD/HISTDATA_COM_MT_EURNZD_M12014/DAT_MT_EURNZD_M1_2014.csv'
EURNZD2015 = '/home/squishy/Desktop/data/1min yearly/EURNZD/HISTDATA_COM_MT_EURNZD_M12015/DAT_MT_EURNZD_M1_2015.csv'

GBPNZD2008 = '/home/squishy/Desktop/data/1min yearly/GBPNZD/HISTDATA_COM_MT_GBPNZD_M12008/DAT_MT_GBPNZD_M1_2008.csv'
GBPNZD2009 = '/home/squishy/Desktop/data/1min yearly/GBPNZD/HISTDATA_COM_MT_GBPNZD_M12009/DAT_MT_GBPNZD_M1_2009.csv'
GBPNZD2010 = '/home/squishy/Desktop/data/1min yearly/GBPNZD/HISTDATA_COM_MT_GBPNZD_M12010/DAT_MT_GBPNZD_M1_2010.csv'
GBPNZD2011 = '/home/squishy/Desktop/data/1min yearly/GBPNZD/HISTDATA_COM_MT_GBPNZD_M12011/DAT_MT_GBPNZD_M1_2011.csv'
GBPNZD2012 = '/home/squishy/Desktop/data/1min yearly/GBPNZD/HISTDATA_COM_MT_GBPNZD_M12012/DAT_MT_GBPNZD_M1_2012.csv'
GBPNZD2013 = '/home/squishy/Desktop/data/1min yearly/GBPNZD/HISTDATA_COM_MT_GBPNZD_M12013/DAT_MT_GBPNZD_M1_2013.csv'
GBPNZD2014 = '/home/squishy/Desktop/data/1min yearly/GBPNZD/HISTDATA_COM_MT_GBPNZD_M12014/DAT_MT_GBPNZD_M1_2014.csv'
GBPNZD2015 = '/home/squishy/Desktop/data/1min yearly/GBPNZD/HISTDATA_COM_MT_GBPNZD_M12015/DAT_MT_GBPNZD_M1_2015.csv'

### AUDNZD
AUDNZD = []

AUDNZD.append('/home/squishy/Desktop/data/1min yearly/AUDNZD/HISTDATA_COM_MT_AUDNZD_M12008/DAT_MT_AUDNZD_M1_2008.csv')
AUDNZD.append('/home/squishy/Desktop/data/1min yearly/AUDNZD/HISTDATA_COM_MT_AUDNZD_M12009/DAT_MT_AUDNZD_M1_2009.csv')
AUDNZD.append('/home/squishy/Desktop/data/1min yearly/AUDNZD/HISTDATA_COM_MT_AUDNZD_M12010/DAT_MT_AUDNZD_M1_2010.csv')
AUDNZD.append('/home/squishy/Desktop/data/1min yearly/AUDNZD/HISTDATA_COM_MT_AUDNZD_M12011/DAT_MT_AUDNZD_M1_2011.csv')
AUDNZD.append('/home/squishy/Desktop/data/1min yearly/AUDNZD/HISTDATA_COM_MT_AUDNZD_M12012/DAT_MT_AUDNZD_M1_2012.csv')
AUDNZD.append('/home/squishy/Desktop/data/1min yearly/AUDNZD/HISTDATA_COM_MT_AUDNZD_M12013/DAT_MT_AUDNZD_M1_2013.csv')
AUDNZD.append('/home/squishy/Desktop/data/1min yearly/AUDNZD/HISTDATA_COM_MT_AUDNZD_M12014/DAT_MT_AUDNZD_M1_2014.csv')
AUDNZD.append('/home/squishy/Desktop/data/1min yearly/AUDNZD/HISTDATA_COM_MT_AUDNZD_M12015/DAT_MT_AUDNZD_M1_2015.csv')



plotMin = 1
plotMax = 255000

USDJPYspread = 0.010006*2
# USDJPYspread = 0.000525
SPXspread = 0.444*2
NZDUSDspread = 0.000161903*2
EURUSDspread = 0.00008627902*2

EURNZDspread = 0.00017
# EURNZDspread = 0

##------------------------------------- Plot Config ------------------------------------------##

def plotConfig():
   mpl.rcParams['figure.facecolor'] = '#222222'
   mpl.rcParams['axes.facecolor'] = '#222222'
   mpl.rcParams['axes.edgecolor'] = '#595959'
   mpl.rcParams['grid.color'] = '595959'
   mpl.rcParams['xtick.labelsize'] = 'small'
   mpl.rcParams['ytick.labelsize'] = 'small'
   mpl.rcParams['ytick.color'] = '595959'
   mpl.rcParams['xtick.color'] = '595959'
   mpl.rcParams['legend.fontsize'] = 'small'
   mpl.rcParams['legend.borderpad'] = 0.2
   mpl.rcParams['axes.labelcolor'] = pink
   mpl.rcParams['text.color'] = 'b3b3b3'

##----------------------------------- Instrument Class  --------------------------------------##

class Instrument(object):
   def __init__(self, colour, name):

       self.colour = colour
       self.name = name
       self.fileFind = name

       self.instrumentData = 0
       self.size = -1
       self.xLength = 0
       self.xElement = 0


   def openFile(self):

       with open(self.fileFind, "r+b") as f:
           mm = mmap.mmap(f.fileno(), 0)
           reader = csv.reader(iter(mm.readline, ""))

           for row in reader:
               self.size = self.size + 1

           mm.close()


       with open(self.fileFind, "r+b") as f:
           mm = mmap.mmap(f.fileno(), 0)
           self.instrumentData = np.zeros(shape=(self.size))

           i = 0
           reader = csv.reader(iter(mm.readline, ""))
           reader.next()


           for i in range(0, self.size):
               x = reader.next()

               self.instrumentData[i] = x[5]

       mm.close()

   def plot(self):

       plt.plot(self.instrumentData[plotMin+100:self.size], color=self.colour)

       plt.xlabel('TIME')
       plt.ylabel('BID/ASK')
       plt.title(' ')
       plt.grid(True)
       plt.legend()

   def getSize(self):
       return (self.size)

   def getData(self):
       return self.instrumentData

##--------------------------------------------------------------------------------------------##

################################################################################################
######################################## Technical #############################################
################################################################################################

##-------------------------------------- Donchian --------------------------------------------##

class donchian(object):
    def __init__(self, data, size, length):

       self.data = data
       self.size = size
       self.donchian = np.zeros(shape=(self.size, 2))

       self.donchianMid = np.zeros(shape=(self.size, 1))
       self.length = length
       i = 0
       n = 0

       self.forSharpe = []

       self.tradePrice = 0
       self.tradePL = 0
       self.backTest = np.zeros(shape=(self.size, 1))
       self.numberOfTrades = 0
       self.longOrShort = 'closed'


    def process(self):
        for i in range(0, self.size):

            if (i >= self.length):

               min = 9999
               max = 0
               for n in range(i - self.length, i):
                   if (self.data[n] > max):
                       max = self.data[n]
                   if (self.data[n] < min):
                       min = self.data[n]

               self.donchian[i, 0] = min
               self.donchian[i, 1] = max
               self.donchianMid[i] = min + (max-min)/2

            if (i < self.length):
               self.donchian[i, 0] = self.data[i]
               self.donchian[i, 1] = self.data[i]


            ########### backtest ###########

            if(i > self.length):

                ###go short if price hits max
                if(self.data[i] > self.donchian[i,1] and self.data[i-1] < self.donchian[i,1] and self.longOrShort != 'short'):
                    self.tradePrice = self.data[i]
                    self.longOrShort = 'short'

                ###go long if price hits mix
                if (self.data[i] < self.donchian[i, 0] and self.data[i - 1] > self.donchian[i, 0] and self.longOrShort != 'long'):
                    self.tradePrice = self.data[i]
                    self.longOrShort = 'long'

                ### close position if price hits middle
                if(self.data[i] < self.donchianMid[i] and self.longOrShort == 'short'):
                    self.tradePL = self.tradePrice - self.data[i] - USDJPYspread
                    self.longOrShort = 'closed'
                    self.backTest[i] = self.backTest[i - 1] + self.tradePL

                    self.forSharpe.append(self.tradePL)

                    self.numberOfTrades = self.numberOfTrades  + 1

                ### close position if price hits middle
                elif (self.data[i] > self.donchianMid[i] and self.longOrShort == 'long'):
                   self.tradePL =  self.data[i] - self.tradePrice - USDJPYspread
                   self.longOrShort = 'closed'
                   self.backTest[i] = self.backTest[i - 1] + self.tradePL

                   self.numberOfTrades = self.numberOfTrades + 1

                   self.forSharpe.append(self.tradePL)

                ###stop loss for short
                elif(self.data[i] > self.tradePrice + 0.5 and self.longOrShort == 'short'):
                    self.tradePL = self.tradePrice - self.data[i] - USDJPYspread
                    self.longOrShort = 'closed'
                    self.backTest[i] = self.backTest[i - 1] + self.tradePL

                    self.numberOfTrades = self.numberOfTrades + 1
                    self.forSharpe.append(self.tradePL)

                    ###stop loss for short
                elif (self.data[i] < self.tradePrice - 0.5 and self.longOrShort == 'long'):
                    self.tradePL = self.data[i] - self.tradePrice - USDJPYspread
                    self.longOrShort = 'closed'
                    self.backTest[i] = self.backTest[i - 1] + self.tradePL

                    self.numberOfTrades = self.numberOfTrades + 1
                    self.forSharpe.append(self.tradePL)

                else:
                    self.backTest[i] = self.backTest[i - 1]

    def plot(self):

       self.ss = np.array(self.forSharpe)
       self.sharpe = np.mean(self.ss)/np.std(self.ss)

       print 'Number of trades= ', self.numberOfTrades
       print 'Sharpe Ratio: ', self.sharpe

       plt.plot(self.donchian[plotMin+100:plotMax-1, 0], color=blue2)
       plt.plot(self.donchian[plotMin+100:plotMax-1, 1], color=purple2)
       plt.plot(self.donchianMid[plotMin + 100:plotMax - 1], color=pink2)

       plt.plot(self.backTest[plotMin + 100:plotMax - 1], color=pink2)

    def getData(self):
       return self.donchian

##------------------------------------ Parabolic SAR -----------------------------------------##

class parabolicSar(object):
   def __init__(self, colour, data, size):
        self.data = data
        self.size = size

        self.colour = colour


   def process(self, acceleration, alpha, threshold):

       self.acceleration = acceleration
       self.initAlpha = alpha
       self.alpha = alpha

       self.alphathreshold = threshold
       print self.size

       self.parabolic = np.zeros(shape=(self.size + plotMin, 1))
       self.backtestArray = np.zeros(shape=(self.size + plotMin, 1))
       self.sumBackTest = np.zeros(shape=(self.size + plotMin, 1))

       self.longOrShort = np.zeros(shape=(self.size + plotMin, 1))

       self.tradeCount = 0
       self.longShort = 'long'
       self.SIP = 0

       self.backtestTest = np.zeros(shape=(self.size + plotMin, 1))
       self.positionPrice = 0
       self.tradePL = 0

       self.continuousPL = np.zeros(shape=(self.size + plotMin, 1))
       self.trackPL = 0

       i = 0

       self.parabolic[plotMin] = self.data[plotMin]
       self.parabolic[plotMin + 1] = self.data[plotMin + 1]

       self.longOrShort[plotMin] = 0


       self.total = 0
       print self.data[plotMin]

       self.high = self.parabolic[plotMin]
       self.low = self.parabolic[plotMin]

       for i in range(plotMin + 1, plotMax - 1):

           # Set high value for current long/short
           if(self.data[i] > self.high):
               self.high = self.data[i]

               #increment alpha
               if (self.alpha < self.alphathreshold):
                   self.alpha = self.alpha + self.acceleration

           # Set low value for current long/short
           if (self.data[i] < self.low):
               self.low = self.data[i]

               # increment alpha
               if (self.alpha < self.alphathreshold):
                   self.alpha = self.alpha + self.acceleration

           # Update parabolic Sar for i + 1
           if(self.longShort == 'long'):
               self.parabolic[i] = self.parabolic[i-1] + self.alpha*(self.high - self.parabolic[i-1])

           if (self.longShort == 'short'):
               self.parabolic[i] = self.parabolic[i-1] + self.alpha*(self.low - self.parabolic[i-1])

           # switch to long if currently short and data is above parabolic sar
           if ((self.data[i] > self.parabolic[i]) and self.longShort == 'short'):
               self.parabolic[i] = self.low

               self.low = self.data[i]
               self.high = self.data[i]
               self.alpha = self.initAlpha

               self.longShort = 'long'


               self.tradePL = self.tradePL + self.positionPrice - self.data[i] - USDJPYspread
               self.positionPrice = self.data[i]

               self.tradeCount = self.tradeCount + 1

           # switch to short if currently long and data is less than parabolic sar
           if ((self.data[i] < self.parabolic[i]) and self.longShort == 'long'):
               self.parabolic[i] = self.high

               self.low = self.data[i]
               self.high = self.data[i]
               self.alpha = self.initAlpha

               self.longShort = 'short'

               self.tradePL = self.tradePL + self.data[i] - self.positionPrice - USDJPYspread
               self.positionPrice = self.data[i]

               self.tradeCount = self.tradeCount + 1

           # record long or short for backtesting //// 2000 for long, 0 for short
           if(self.longShort == 'long'):
               self.longOrShort[i] = 2000
           else:
               self.longOrShort[i] = 0

           self.backtestTest[i] = self.tradePL

           ## long long
           if(self.longOrShort[i-1] > 1900 and self.longOrShort[i] > 1900):
               self.trackPL = self.data[i] - self.data[i-1]

           ## short short
           if (self.longOrShort[i - 1] < 1900 and self.longOrShort[i] <1900):
               self.trackPL = self.data[i-1] - self.data[i]

           ## long to short
           if (self.longOrShort[i - 1] > 1900 and self.longOrShort[i] < 1900):
               self.trackPL = self.data[i] - self.data[i-1] - USDJPYspread

           ##short to long
           if (self.longOrShort[i - 1] < 1900 and self.longOrShort[i] > 1900):
               self.trackPL = self.data[i-1] - self.data[i] - USDJPYspread

           self.continuousPL[i] = self.continuousPL[i-1] + self.trackPL


   def getData(self):
       return self.parabolic

   def plot(self):

       print 'PL: ', self.backtestTest[plotMax-2] - self.data[plotMin]
       print 'Return: ', self.continuousPL[plotMax-2]

       print 'number of trades: ', self.tradeCount

       plt.plot(self.parabolic[plotMin+100:plotMax-1], '.',  color = self.colour, label='##')

       plt.plot(self.backtestTest[plotMin+100:plotMax - 2] , color=purple2, label='PL')

       plt.plot(self.continuousPL[plotMin + 100:plotMax - 2] + self.data[plotMin], color=blue2, label='PL')

   def getPL(self):
       return self.continuousPL[plotMax-2]

##################### gradient  stuff
# length = 50
# gradient = np.zeros(shape=(length, 2))
#
#
#
# plotConfig()
# ins = Instrument(pink, USDJPY2008)
# ins.openFile()
# insp = parabolicSar(grey, ins.getData(), ins.getSize() )
#
# alpha = 0.5
# theta = .25
#
# insp.process(0.001, alpha, 1)
# gradient[0,0] = insp.getPL()
# gradient[0,1] = .7
#
# change  = 99
# i = 1
#
# while(abs(change) > 0.001 or i > (length-1)):
#     insp.process(0.0001, alpha, 1)
#     gradient[i,1] = alpha
#     print alpha
#
#     gradient[i,0] = insp.getPL()
#
#     if(gradient[i,0] - gradient[i-1,0] > 0):
#         alpha = alpha*theta
#     if(gradient[i,0] - gradient[i-1,0] < 0):
#         alpha = alpha - alpha*theta
#
#     change = (gradient[i,0] - gradient[i-1,0])
#     print 'change: ', change
#     i = i+1
#
# i = 0
# max = 0
# maxPL = 0
# for i in range(0, length-1):
#     if(gradient[i,0] > max):
#         max = gradient[i,1]
#         maxPL = gradient[i,0]
#
# print 'max= ', max
# print 'maxPL= ', maxPL
#
# plt.plot(gradient[0:length,0], color=blue2, label='PL')
# plt.plot(gradient[0:length,1], color=pink2, label='PL')
# plt.show()
#
# ins.plot()
# insp.plot()
# plt.show()




# # #################### normal stuff

# plotConfig()
# ins = Instrument(pink, USDJPY1hour)
# ins.openFile()
# ins.plot()
#
#
# insp = parabolicSar(grey, ins.getData(), ins.getSize() )
# insp.process(0.00025, 0.00025, .2)
# insp.plot()
#
# plt.show()

#############################


##------------------------------------ Moving Average ----------------------------------------##

class movingAverage(object):
   def __init__(self, data, size, length):

       self.data = data
       self.size = size
       self.length = length
       self.movingAverage = np.zeros(shape=(self.size))
       i = 0

   def process(self):
       for i in range(0, self.size):

           if (i >= self.length):
               sum = 0
               for n in range(i - self.length, i):
                   sum = sum + self.data[n]

               self.movingAverage[i] = sum / self.length

           if (i < self.length):
               self.movingAverage[i] = self.data[i]

   def plot(self):
       plt.plot(self.movingAverage[0:20000], color=purple)

##---------------------------------- Hidden Markov Model -------------------------------------##

# class hmm(object):
#    def __init__(self, data, size, threshold):
#        self.data = data
#        self.size = size
#        self.threshold = threshold
#        self.hmm = np.zeros(shape=(self.size))
#
#    def process(self):
#
#        self.pos = 0
#        self.posCount = 0
#        self.neg = 0
#        self.negCount = 0
#        self.posNeg = 0
#        self.posNegCount = 0
#        self.negPos = 0
#        self.negPosCount = 0
#
#        for i in range(1, self.size):
#            if (self.data[i - 1] > self.threshold and self.data[i] > self.threshold):
#                self.pos += 1
#                self.posCount += 1
#
#            if (self.data[i - 1] > self.threshold and self.data[i] < self.threshold):
#                self.posNeg += 1
#                self.posNegCount += 1
#
#            if (self.data[i - 1] < self.threshold and self.data[i] < self.threshold):
#                self.neg += 1
#                self.negCount += 1
#
#            if (self.data[i - 1] < self.threshold and self.data[i] > self.threshold):
#                self.negPos += 1
#                self.negPosCount += 1
#
#         self.posProb = (float(self.pos) / (self.posCount + self.posNegCount))
#         self.negProb = (float(self.negPos) / (self.negPosCount + self.negCount))
#
#        for i in range(0, self.size):
#            if (self.data[i] > self.threshold):
#                self.hmm[i] = self.posProb
#            else:
#                self.hmm[i] = self.negProb
#
#    def getData(self):
#        return self.hmm
#
#    def plot(self):
#        plt.plot(self.hmm[0:200000], color=pink)

##-------------------------------------- Kalman Filter ---------------------------------------##

class kalmanFilter(object):
   def __init__(self, data, size, n):
       self.data = data
       self.size = size
       self.length = n

       self.i = 0
       self.error = 0

       self.kalmanGain = np.zeros(shape=(self.size))
       self.prediction = np.zeros(shape=(self.size))

       self.prediction[0] = 1

   def process(self):

       for i in range(1, self.size):

           self.error = abs(prediction[i-1] - self.data[i])


##-------------------------------------- Volatility ------------------------------------------##

class volatility(object):
   def __init__(self, data, size):
       self.data = data
       self.size = size
       self.volatility = np.zeros(shape=(self.size))
       i = 0

   def process(self):
       for i in range(1, self.size):
           self.volatility[i] = abs(self.data[i] - self.data[i - 1])

   def getData(self):
       return self.volatility

   def plot(self):
       plt.plot(self.volatility[0:200000], color=grey)

##------------------------------------- Hurst Exponent ---------------------------------------##

def hurst(ts):

   """Returns the Hurst Exponent of the time series vector ts"""
   # Create the range of lag values
   lags = range(2, 100)

   # Calculate the array of the variances of the lagged differences
   tau = [sqrt(std(subtract(ts[lag:], ts[:-lag]))) for lag in lags]

   # Use a linear fit to estimate the Hurst Exponent
   poly = polyfit(log(lags), log(tau), 1)

   # Return the Hurst exponent from the polyfit output
   return poly[0] * 2.0

## ------------------------------- Fuzzy WubbaWubba system -----------------------------------##

class movingHurst(object):
    def __init__(self, data, size):
        self.data = data
        self.size = size

        self.movingHurst = np.zeros(shape=(self.size, 1))
        self.periodN = 1000
        self.n = 0
    def process(self):

        for i in range(1, self.size):
            self.n = self.n+1

            if(n == 500):
                n = 0
                self.movingHurst[i] = self.hurst(self.data[(i-500):i])

            else:
                self.movingHurst[i] = self.movingHurst[i-1]

    def hurst(self, ts):

        """Returns the Hurst Exponent of the time series vector ts"""
        # Create the range of lag values
        lags = range(2, 100)

        # Calculate the array of the variances of the lagged differences
        tau = [sqrt(std(subtract(ts[lag:], ts[:-lag]))) for lag in lags]

        # Use a linear fit to estimate the Hurst Exponent
        poly = polyfit(log(lags), log(tau), 1)

        # Return the Hurst exponent from the polyfit output
        return poly[0] * 2.0


class meanReversion(object):
    def __init__(self, data, size,colour):
        self.data = data
        self.size = size
        self.colour = colour
        self.movingHurst = np.zeros(shape=(self.size, 1))
        self.n = 0
        self.longOrShort = 'closed'
        self.forSharpe = []

    def bollinger(self, n):
        self.bUpper = np.zeros(shape=(self.size, 1))
        self.bLower = np.zeros(shape=(self.size, 1))
        self.ma = np.zeros(shape=(self.size, 1))
        self.timePeriod = 250
        self.sigma = np.zeros(shape=(self.size, 1))

        self.PLreturn = np.zeros(shape=(self.size, 1))

        self.n = n

        self.sd = 0
        self.upperSL = 1.02
        self.lowerSL = 0.98
        self.tradePrice = 0
        self.tradePl = 0
        self.backTest = np.zeros(shape=(self.size, 1))


        self.numberOfTrades = 0

        for i in range(self.timePeriod, self.size):

            if(i > self.timePeriod):
                self.sigma[i] = np.std(self.data[i-self.timePeriod:i])
                self.ma[i] = np.mean(self.data[i-self.timePeriod:i])
                self.bUpper[i] = self.ma[i] + self.sigma[i]
                self.bLower[i] = self.ma[i] - self.sigma[i]
                ################## back test

                ### go short
                if(self.longOrShort == 'closed'):
                    if(self.data[i] > self.bUpper[i] and self.data[i-1] < self.bUpper[i]):
                        self.longOrShort = 'short'
                        self.tradePrice = self.data[i]
                        #print 'open short'

                #### go long
                if (self.longOrShort == 'closed'):
                    if(self.data[i] < self.bLower[i] and self.data[i-1] > self.bLower[i]):
                        self.longOrShort = 'long'
                        self.tradePrice = self.data[i]
                        #print 'open long'

                ### close short
                if(self.longOrShort == 'short' and self.data[i] < self.ma[i]):
                    self.longOrShort = 'closed'
                    self.tradePl = self.tradePrice - self.data[i] - EURNZDspread
                    self.backTest[i] = self.backTest[i-1] + self.tradePl
                    self.numberOfTrades = self.numberOfTrades + 1
                    #print 'short closed with TP'
                    self.forSharpe.append(self.tradePl)

                elif(self.longOrShort == 'short' and self.data[i] > self.tradePrice*self.upperSL):
                    self.longOrShort = 'closed'
                    self.tradePl = self.tradePrice - self.data[i] - EURNZDspread
                    self.backTest[i] = self.backTest[i - 1] + self.tradePl
                    self.numberOfTrades = self.numberOfTrades + 1
                    #print 'short closed with SL'
                    self.forSharpe.append(self.tradePl)

                #### close long
                elif(self.longOrShort == 'long' and self.data[i] > self.ma[i]):
                    self.longOrShort = 'closed'
                    self.tradePl = self.data[i] - self.tradePrice - EURNZDspread
                    self.backTest[i] = self.backTest[i-1] + self.tradePl
                    self.numberOfTrades = self.numberOfTrades + 1
                    #print 'long closed with TP'
                    self.forSharpe.append(self.tradePl)

                elif(self.longOrShort == 'long' and self.data[i] < self.tradePrice *self.lowerSL):
                    self.longOrShort = 'closed'
                    self.tradePl =self.data[i] - self.tradePrice - EURNZDspread
                    self.backTest[i] = self.backTest[i - 1] + self.tradePl
                    self.numberOfTrades = self.numberOfTrades + 1
                    #print 'long closed with SL'
                    self.forSharpe.append(self.tradePl)

                else:
                    self.backTest[i] = self.backTest[i-1]

            self.PLreturn[i] = self.backTest[i]/self.data[1]


        print 'return is: ', self.backTest[self.size-2]/self.data[1], 'n: ', self.n
        print 'hurst is: ', hurst(self.data)
        return self.PLreturn

    def plot(self):

        self.ss = np.array(self.forSharpe)
        # plt.plot(self.ma[plotMin+self.timePeriod:self.size], color=purple)
        plt.plot(self.bUpper[plotMin + self.timePeriod:self.size], color=purple2)
        plt.plot(self.bLower[plotMin + self.timePeriod:self.size], color=pink2)
        plt.plot(self.backTest[plotMin + self.timePeriod:self.size], color=pink2)

##---------------------------------------- data shuffler ------------------------------------------##

class dataShuffler(object):
    def __init__(self, data, size):
        self.data = data
        self.size = size

        self.shuffled = np.diff(self.data)
        np.random.shuffle(self.shuffled)

        self.newArray = np.zeros(shape=(self.size, 1))
        self.newArray[0] =  self.data[0]
        i = 0

    def process(self):
        for i in range(1, self.size-1):
            self.newArray[i] = self.newArray[i - 1] + self.shuffled[i]

    def plot(self):
        plt.plot(self.newArray[plotMin+100:self.size-1], color=pink2)

    def getData(self):
        return self.newArray


#################### multithreaded tester ##############################

tic = time.clock()

plotConfig()
insData = []
insProcess = []

dataShuffled = []

data = SPX

for i in range(0, len(data)):
    insData.append(Instrument(grey, data[i]))
    insData[i].openFile()
    insProcess.append(meanReversion(insData[i].getData(), insData[i].getSize(), pink))


####testing shuffled
# for i in range(0, len(data)):
#     insData.append(Instrument(grey, data[i]))
#     insData[i].openFile()
#
#     dataShuffled.append(dataShuffler(insData[i].getData(), insData[i].getSize()))
#     dataShuffled[i].process()
#
#     insProcess.append(meanReversion(dataShuffled[i].getData(), insData[i].getSize()-1, pink))

def tester(i):
    n = i

    return insProcess[i].bollinger(n)


pool = mp.Pool(processes = 8)
results =  pool.map(tester, range(len(insData)))

pool.close()
pool.join()

for i in range(0, len(insData)):
    # insData[i].plot()
    plt.plot(results[i], color=colours[i])


toc = time.clock()
print(tic - toc)
print 'tic: ', tic
print 'toc: ', toc

plt.show()



# ##------------------------------------------ Main --------------------------------------------##


##--------------------------------------- Live Plot ------------------------------------------##

class livePlot(object):

   def process(self):

       mt4File = '/home/squishy/.wine/drive_c/Program Files (x86)/MetaTrader 4/MQL4/Files/liveData.csv'

       dataLength = 100

       USDJPY = np.zeros(shape=(dataLength, 2))
       SPX500 = np.zeros(shape=(dataLength, 2))
       J225 = np.zeros(shape=(dataLength, 2))
       EURUSD = np.zeros(shape=(dataLength, 2))

       fig = plt.figure()
       ax1 = fig.add_subplot(1, 4, 1)
       ax2 = fig.add_subplot(1, 4, 2)
       ax3 = fig.add_subplot(1, 4, 3)
       ax4 = fig.add_subplot(1, 4, 4)

       def animate(t):
           i = 0
           n = 0

           with open(mt4File, "r+b") as f:
               mm = mmap.mmap(f.fileno(), 0)
               reader = csv.reader(iter(mm.readline, ""))

               USDJPYin = reader.next()
               SPX500in = reader.next()
               J225in = reader.next()
               EURUSDin = reader.next()

               mm.close()

               for i in range(0, dataLength - 1):
                   USDJPY[i, 0] = USDJPY[i + 1, 0]
                   USDJPY[i, 1] = USDJPY[i + 1, 1]

                   SPX500[i, 0] = SPX500[i + 1, 0]
                   SPX500[i, 1] = SPX500[i + 1, 1]

                   J225[i, 0] = J225[i + 1, 0]
                   J225[i, 1] = J225[i + 1, 1]

                   EURUSD[i, 0] = EURUSD[i + 1, 0]
                   EURUSD[i, 1] = EURUSD[i + 1, 1]

               USDJPY[99, 0] = USDJPYin[0]
               USDJPY[99, 1] = USDJPYin[1]

               J225[99, 0] = J225in[0]
               J225[99, 1] = J225in[1]

               SPX500[99, 0] = SPX500in[0]
               SPX500[99, 1] = SPX500in[1]

               EURUSD[99, 0] = EURUSDin[0]
               EURUSD[99, 1] = EURUSDin[1]

           ax1.clear()
           ax1.plot(USDJPY[0:99, 0], color=pink)
           ax1.plot(USDJPY[0:99, 1], color=purple)
           ax1.set_title('USDJPY')

           ax2.clear()
           ax2.plot(SPX500[0:99, 0], color=pink)
           ax2.plot(SPX500[0:99, 1], color=purple)
           ax2.set_title('SPX500')

           ax3.clear()
           ax3.plot(EURUSD[0:99, 0], color=pink)
           ax3.plot(EURUSD[0:99, 1], color=purple)
           ax3.set_title('EURUSD')

           ax4.clear()
           ax4.plot(J225[0:99, 0], color=pink)
           ax4.plot(J225[0:99, 1], color=purple)
           ax4.set_title('J225')


       ani = animation.FuncAnimation(fig, animate, interval=1000)
       plt.show()


# newLivePlot = livePlot()
# newLivePlot.process()

##----------------------------------- Parabolic Live -----------------------------------------##


class parabolicInstrument(object):
   def __init__(self):

       # self.instrumentIn = 0
       self.longShort = 'long'
       self.high = 0
       self.low = 0
       self.startCount = 0
       self.alpha = 0.01
       self.aplhaInit = 0.01
       self.acceleration = .01

       self.startThreshold = 1
       self.max = 0
       self.min = 999

       self.i = 0
       self.dataLength = 50
       self.instrument = np.zeros(shape=(self.dataLength, 2))
       self.parabolic = np.zeros(shape=(self.dataLength, 1))
       self.atStart = True

   def getInstrumentData(self):
       return self.instrument

   def getInstrumentParabolic(self):
       return self.parabolic

   def getMin(self):
       return self.min

   def getMax(self):
       return self.max

   def process(self, data):
       self.instrumentIn = data
       ### tell to wait on Init
       if (self.startCount < self.startThreshold):
           f = open(
               '/home/squishy/.wine/drive_c/Program Files (x86)/MetaTrader 4 Client Terminal/MQL4/Files/orders',
               'w')
           f.write('wait')
           f.close()
           print('waiting..')

       for i in range(0, self.dataLength - 1):
           self.instrument[i, 0] = self.instrument[i + 1, 0]
           self.instrument[i, 1] = self.instrument[i + 1, 1]

           if (self.instrument[i, 1] > self.max and self.instrument[i, 1] != 0):
               self.max = self.instrument[i, 1]
           if (self.instrument[i, 0] < self.min and self.instrument[i, 0] != 0):
               self.min = self.instrument[i, 0]

           if (self.parabolic[i] > self.max and self.parabolic[i] != 0):
               self.max = self.parabolic[i]
           if (self.parabolic[i] < self.min and self.parabolic[i] != 0):
               self.min = self.parabolic[i]

       self.instrument[self.dataLength - 1, 0] = self.instrumentIn[0]
       self.instrument[self.dataLength - 1, 1] = self.instrumentIn[1]

       # process live parabolic --------------------------------

       # initialisation
       if (self.atStart == True):
           self.atStart = False
           self.parabolic[self.dataLength - 1] = self.instrument[self.dataLength - 1, 1]
           self.high = self.parabolic[self.dataLength - 1]
           self.low = self.parabolic[self.dataLength - 1]

       else:
           # shuffle past values
           for i in range(0, self.dataLength - 1):
               self.parabolic[i] = self.parabolic[i + 1]

           if (self.instrument[self.dataLength - 1, 1] > self.high):
               self.high = self.instrument[self.dataLength - 1, 1]
               if (self.alpha < .2):
                   self.alpha = self.alpha + self.acceleration

           if (self.instrument[self.dataLength - 1, 1] < self.low and self.instrument[
                   self.dataLength - 1, 1] != 0):
               self.low = self.instrument[self.dataLength - 1, 1]
               if (self.alpha < .2):
                   self.alpha = self.alpha + self.acceleration

           if (self.longShort == 'long'):
               self.parabolic[self.dataLength - 1] = self.parabolic[self.dataLength - 2] + self.alpha * (
                   self.high - self.parabolic[self.dataLength - 2])

           if (self.longShort == 'short'):
               self.parabolic[self.dataLength - 1] = self.parabolic[self.dataLength - 2] + self.alpha * (
                   self.low - self.parabolic[self.dataLength - 2])

           # switch to long if conditions met
           if ((self.instrument[self.dataLength - 1, 1] > self.parabolic[
                   self.dataLength - 1]) and self.longShort == 'short'):
               self.parabolic[self.dataLength - 1] = self.low

               self.low = self.instrument[self.dataLength - 1, 1]
               self.high = self.instrument[self.dataLength - 1, 1]
               self.alpha = self.aplhaInit
               self.longShort = 'long'

               self.startCount += 1

               # send order to mt4
               if (self.startCount < self.startThreshold):
                   f = open(
                       '/home/squishy/.wine/drive_c/Program Files (x86)/MetaTrader 4 Client Terminal/MQL4/Files/orders',
                       'w')
                   f.write('wait')
                   f.close()
                   print('waiting..')

               if (self.startCount > self.startThreshold):
                   print('BTFD')
                   f = open(
                       '/home/squishy/.wine/drive_c/Program Files (x86)/MetaTrader 4 Client Terminal/MQL4/Files/orders',
                       'w')
                   f.write('BTFD')
                   f.close()
                   print('buy')

           # switch to short if conditions met
           if ((self.instrument[self.dataLength - 1, 1] < self.parabolic[
                   self.dataLength - 1]) and self.longShort == 'long'):
               self.parabolic[self.dataLength - 1] = self.high

               self.low = self.instrument[self.dataLength - 1, 1]
               self.high = self.instrument[self.dataLength - 1, 1]
               self.alpha = self.aplhaInit
               self.longShort = 'short'

               self.startCount += 1

               # send order to mt4
               if (self.startCount < self.startThreshold):
                   f = open(
                       '/home/squishy/.wine/drive_c/Program Files (x86)/MetaTrader 4 Client Terminal/MQL4/Files/orders',
                       'w')
                   f.write('wait')
                   f.close()
                   print('waiting..')

               if (self.startCount > self.startThreshold):
                   f = open(
                       '/home/squishy/.wine/drive_c/Program Files (x86)/MetaTrader 4 Client Terminal/MQL4/Files/orders',
                       'w')
                   f.write('SELL')
                   f.close()
                   print('open sell')

# USDJPY = parabolicInstrument()
# NZDUSD = parabolicInstrument()


class parabolicLive(object):
   def __init__(self):
       self.exit = False

       self.mt4File = '/home/squishy/.wine/drive_c/Program Files (x86)/MetaTrader 4 Client Terminal/MQL4/Files/liveData.csv'

       self.dataSaveOpen = False
       self.dataSaveFile = '..'

       self.USDJPYin = 0
       self.SPXin = 0
       self.J225in = 0
       self.EURUSDin = 0
       self.NZDUSDin = 0
       self.dataLen = 50

       self.fig = plt.figure()
       self.ax1 = self.fig.add_subplot(2, 1, 1)
       self.ax2 = self.fig.add_subplot(2, 2, 1)

       self.isActivaed = False

       def getLength():
           return self.dataLen

       #####################################################################
   def updataData(self):
       # get raw data from mt4 in
       with open(self.mt4File, "r+b") as f:
           mm = mmap.mmap(f.fileno(), 0)
           reader = csv.reader(iter(mm.readline, ""))

           self.USDJPYin = reader.next()
           self.SPXin = reader.next()
           self.J225in = reader.next()
           self.EURUSDin = reader.next()
           self.NZDUSDin = reader.next()

           mm.close()



       # export data to csv #################################
       currentTime = (datetime.datetime.now().today())
       currentTime = str(currentTime.replace(microsecond=0))
       print (currentTime)

       if (self.dataSaveOpen == False):
           self.dataSaveFile = currentTime
           self.dataSaveOpen = True
       else:

           f = open('/home/squishy/Desktop/data/liveData saved/' + self.dataSaveFile + '.csv', 'a')
           f.write(currentTime
                   + ',' + self.USDJPYin[0] + ',' + self.USDJPYin[1]
                   + ',' + self.SPXin[0] + ',' + self.SPXin[1]
                   + ',' + self.J225in[0] + ',' + self.J225in[1]
                   + ',' + self.EURUSDin[0] + ',' + self.EURUSDin[1]
                   + ',' + self.NZDUSDin[0] + ',' + self.NZDUSDin[1]
                   + "\n")
           f.close()



        ############################################
   def animate(self,t):
       self.updataData()

       USDJPY.process(self.USDJPYin)
       NZDUSD.process(self.NZDUSDin)

       self.ax1.clear()

       self.ax1.set_ylim([USDJPY.getMin() * .99999, USDJPY.getMax() * 1.00001])
       self.ax1.plot(USDJPY.getInstrumentParabolic()[0:self.dataLen - 1, 0], '.', color=grey)
       self.ax1.plot(USDJPY.getInstrumentData()[0:self.dataLen - 1, 0],  color=pink2)
       self.ax1.plot(USDJPY.getInstrumentData()[0:self.dataLen - 1, 1],  color=purple2)

       self.ax2.clear()

       self.ax2.set_ylim([NZDUSD.getMin() * .99999, NZDUSD.getMax() * 1.00001])
       self.ax2.plot(NZDUSD.getInstrumentParabolic()[0:self.dataLen - 1, 0], '.', color=grey)
       self.ax2.plot(NZDUSD.getInstrumentData()[0:self.dataLen - 1, 0],  color=pink2)
       self.ax2.plot(NZDUSD.getInstrumentData()[0:self.dataLen - 1, 1],  color=purple2)



       ###########################################################################



           # plot live stuff
           # self.ax1.clear()
           # self.ax1.set_ylim([102 * .99999, 103 * 1.00001])
           # self.ax1.plot(USDJPY.getInstrumentParabolic()[0:self.dataLen-1, 0], '.', color=grey)
           # self.ax1.plot(USDJPY.getInstrumentData()[0:self.dataLen-1, 0],  color=pink2)
           # self.ax1.plot(USDJPY.getInstrumentData()[0:self.dataLen-1, 1], color=purple2)





           # infinite iteration






   def process(self):


       ani = animation.FuncAnimation(self.fig, self.animate, interval=1000)
       plt.show()

# plotConfig()
# parL = parabolicLive()
# parL.process()


class dataScraper(object):
   def __init__(self):
       self.exit = False

       self.mt4File = '/home/squishy/.wine/drive_c/Program Files (x86)/MetaTrader 4 Client Terminal/MQL4/Files/liveData.csv'

       self.dataSaveOpen = False
       #self.dataSaveFile = '..'

       self.USDJPYin = 0
       self.SPXin = 0
       self.J225in = 0
       self.EURUSDin = 0
       self.NZDUSDin = 0
       self.dataLen = 50


       #####################################################################
   def updataData(self):
       # get raw data from mt4 in
       with open(self.mt4File, "r+b") as ff:
           mm = mmap.mmap(ff.fileno(), 0)
           reader = csv.reader(iter(mm.readline, ""))

           self.USDJPYin = reader.next()
           self.SPXin = reader.next()
           self.J225in = reader.next()
           self.EURUSDin = reader.next()
           self.NZDUSDin = reader.next()

           mm.close()

   def save(self):

       # export data to csv #################################
       currentTime = (datetime.datetime.now().today())
       currentTime = str(currentTime.replace(microsecond=0))

       f = open('/home/squishy/Desktop/data/liveData saved/' + currentTime + '.csv', 'a')

       i = 0
       while(i != 2):
           self.updataData()

           f.write(currentTime
                   + ',' + self.USDJPYin[0] + ',' + self.USDJPYin[1]
                   + ',' + self.SPXin[0] + ',' + self.SPXin[1]
                   + ',' + self.J225in[0] + ',' + self.J225in[1]
                   + ',' + self.EURUSDin[0] + ',' + self.EURUSDin[1]
                   + ',' + self.NZDUSDin[0] + ',' + self.NZDUSDin[1]
                   + "\n")


           time.sleep(1)

# newIn = dataScraper()
# newIn.save()
#

