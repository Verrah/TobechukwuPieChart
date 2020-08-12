#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  7 14:01:01 2027

Changed approach and started to use bins
for profit margins: -20% to -15%, -15% to -10% ... 35% to 40%
to produce a confusion matrix


@author: narratorjay
"""

#%% libraries and locations

import os
import numpy as np
import pandas as pd
from sklearn.metrics import confusion_matrix

os.chdir('.data/raw')
thisDF = pd.read_csv('targets-n-profits.csv')
originalRows = len(thisDF)
print('Dataframe from original raw csv has provided', originalRows, 'rows.')

#%% select margin extremities and trim
minNeg, maxPos, binWidth = -20, 40, 5
maxPosRange = maxPos + binWidth

thisDF = thisDF[['target_profit', 'actual_margin']]
thisDF = thisDF.loc[((thisDF['target_profit'] > minNeg) & (thisDF['target_profit'] < maxPos)) & ((thisDF['actual_margin'] > minNeg) & (thisDF['actual_margin'] < maxPos))]
thisDF = thisDF.reset_index(drop = True)
rowsWithinMinMax = len(thisDF)
print('Selected ' + str(rowsWithinMinMax) + ' projects with margins between ' + str(minNeg) + '% and ' + str(maxPos) + '%, losing ' +
      str(int(100* (1- (rowsWithinMinMax/originalRows)))) + '% of the original records.')

# I found pd.cut straightforward to use to create bins, output needed tidying
thisDF['actual_margin'] = pd.cut(thisDF['actual_margin'], list(range(minNeg, maxPosRange, binWidth)), right = False)
thisDF['target_profit'] = pd.cut(thisDF['target_profit'], list(range(minNeg, maxPosRange, binWidth)), right = False)

# use an integer for the confusion matrix using the lower categorical bound with  thisDF.margin[row].left
# tried a string but '5' came after '30'
for row in range(len(thisDF)):
    thisDF.intMargin[row] = thisDF.actual_margin[row].left
    thisDF.intTarget[row] = thisDF.target_profit[row].left


# because it seems confusion matrices do not work with categorical datatypes
thisDF['intMargin'] = np.nan 
thisDF['intTarget'] = np.nan
thisDF.intMargin = pd.to_numeric(thisDF.intMargin, downcast = 'integer')
thisDF.intTarget = pd.to_numeric(thisDF.intTarget, downcast = 'integer')    
thisDF['intTarget'].value_counts()   	# check distribution looks ok, went squiffy one evening 
thisDF['intMargin'].value_counts()

# all the preparation has led to this single transforming line
arrayCM = confusion_matrix(thisDF['intTarget'], thisDF['intMargin'])

# print and save
print(arrayCM)
os.chdir('.data/processed')
np.savetxt('sampleConfusionMatrix-TEST.csv', arrayCM, fmt = "%d", delimiter = ",")    # no column headings
print('Saved csv file.')

