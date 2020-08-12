#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 17:38:04 2029
Go through confusion matrix creating pie charts
I hope they get called Tobechukwu plots, following Stigler’s Law.
Tobechukwu is a gender-neutral Igbo name, 
pronounced  tä be chü-(ˌ)kü, ‘To’ as in ‘top’, ‘be’ as in ‘bet’, ‘chukwu’ as in ‘cuckoo’ but with ‘ch’ as the first consonant.
Stresses are on the first and third syllables, it is a compound word.)


@author: jay
"""

#%%    # outer ring is correct thickness, now for near misses

import os
import pandas as pd
import numpy as np
import math
import statistics
import matplotlib.pyplot as plt; plt.rcdefaults()

os.chdir('/home/jay/sdsv/dissertation/2submit/data-processed')
#confusionDF = pd.read_csv('marginRowsTargetCols-TopLeftOrigin-mgrPred.csv', header = None)           # managers' predictions, change selection as required
#confusionDF = pd.read_csv('marginRowsTargetCols-TopLeftOrigin-CatBoostPred.csv', header = None)      # CatBoost

confusionDF = pd.read_csv('marginRowsTargetCols-TopLeftOrigin-RFonCatPred.csv', header = None)   # Random Forest check this dataframe in console to find sensible run limits                                                                                                        # old run before row/col change  


os.chdir('/home/jay/sdsv/dissertation/2submit/visualisation/TFFcharts')
#%% now for multi-plots of polars

binSize = 5                                 # has to be 5 to match pd.cut step size in previous code
for diagonalRun in list(range(4,10,1)):     # this range is selected because extreme margins are not usually predicted, also code needs +-1 row cell to count near miss
    
    thisRow, thisCol = diagonalRun, diagonalRun
    rowPercent, colPercent = thisRow * binSize - 20, thisCol * binSize - 20
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
    plt.suptitle('TFF chart for ' + str(rowPercent) + '% - ' + str(rowPercent + binSize) + '% margin forecasts with  \n' + str(truePositive) + ' correct categorised Random Forest predictions')
    ax = plt.subplot(111, projection = 'polar')
    #ax.set(suptitle = 'Suptitle')
    
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
    #plt.savefig('TEST-TFF' + str(colPercent) + 'pc-RandomForestFakeCat.png')        # turn off plt.show() to save, change name according to input file
   

