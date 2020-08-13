#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 17:38:04 2029
Go through confusion matrix creating pie charts of 
True Positive, False Positive (with a near miss component) and False Negative forecasts.
I hope these get called Tobechukwu plots, following Stigler’s Law.
Tobechukwu is a gender-neutral Igbo name, 
pronounced  tä be chü-(ˌ)kü, ‘To’ as in ‘top’, ‘be’ as in ‘bet’, ‘chukwu’ as in ‘cuckoo’ but with ‘ch’ as the first consonant.
Stresses are on the first and third syllables, it is a compound word.


@author: jay
"""

#%%  

import os
import pandas as pd
import numpy as np
import math
import statistics
import matplotlib.pyplot as plt; plt.rcdefaults()

os.chdir('./data/processed')
confusionDF = pd.read_csv('sampleConfusionMatrix.csv', header = None)   # check csv has forecasts as rows (y) and margins as columns (x)                                                                                                        # old run before row/col change  
os.chdir('../../reports/figures')

#%% now for multi-plots of polars

binSize = 5                                 # alter as needed to match pd.cut step size in code that created the confusion matrix
for diagonalRun in list(range(4,10,1)):     # this range is selected because extreme margins are not usually predicted, also code needs +-1 column cell to provide near miss counts
    
    thisRow, thisCol = diagonalRun, diagonalRun
    rowPercent, colPercent = thisRow * binSize - 10, thisCol * binSize - 10
    print('Plotting graph for lower bound percentages ' + str(rowPercent) + '% and ' + str(colPercent) + '% in the confusion matrix')
    
    truePositive = confusionDF[thisRow][thisCol]                                          
    falsePositive = confusionDF.sum(axis = 1)[thisRow] - truePositive
    falseNegative = confusionDF.sum(axis = 0)[thisCol] - truePositive
    nearMissFP = confusionDF[thisCol - 1][thisRow] + confusionDF[thisCol + 1][thisRow]    # subset of False Positive
    falsePositive = falsePositive - nearMissFP

    
    discArea = truePositive + falsePositive + nearMissFP                                  # geometry of disc and ring areas
    ringArea = falseNegative
    discR = math.sqrt(discArea / np.pi)
    ringR = math.sqrt(discR ** 2 + ringArea / np.pi)
    
    
    plt.figure(figsize=(7, 8))
    # update title string as needed ->
    plt.suptitle('TFF chart for ' + str(rowPercent) + '% - ' + str(rowPercent + binSize) + '% margin forecasts with  \n' + str(truePositive) + ' correctly categorised predictions')
    ax = plt.subplot(111, projection = 'polar')
    
    
    ax.set_axis_off()
    truePangle = 2 * np.pi * truePositive / discArea
    falsePangle = 2 * np.pi * falsePositive / discArea
    nearMissFPangle = 2 * np.pi * nearMissFP / discArea
    
    # learn polar plot co-ordinates:  zero angle is along 'x-axis', positive angle is anti-clockwise, segment is centred on angle (hence /2 in many lines) 
    ax.bar(np.pi / 2 - truePangle / 2, discR, width = truePangle, bottom = 0, color = '#90b5df')                                # truePositive
    ax.bar((np.pi / 2 - truePangle) - falsePangle / 2, discR, width = falsePangle, bottom = 0, color = '#10253f', alpha = 0.5)  # falsePositive
    ax.bar((np.pi / 2 + nearMissFPangle / 2), discR, width = nearMissFPangle, bottom = 0, color = '#10253f', alpha = 0.3)       # nearMissFP
    ax.bar((np.pi / 2), ringR - discR, width = np.pi * 2, bottom = discR, color = '#90b5df', alpha = 0.6)                       # falseNegative
    ax.legend(['True positive','False positive','Near miss (FP)','False negative ring'], loc = 'upper left')
    plt.show()                                                             # comment out plt.savefig when testing
    #plt.savefig('TEST-TFF' + str(colPercent) + 'pc-demo.png')        # turn off plt.show() to save, change name as required
    
   
