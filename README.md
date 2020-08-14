# Tobechukwu pie chart
### The web's first pie chart for confusion matrices.  Named in accordance with Stigler's law.
### Best described as True-False-False 'TFF' pie charts.


These visualise data in a confusion matrix to add insight about prediction or identification.  This example is produced by the confusion_matrix package from [sklearn](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.confusion_matrix.html "scikit-learn 0.23.2")

![alt text][textCMcloseRowsDiag]

The conventional 2x2 confusion matrix of binary results for (typically) a pregnancy test needs little explanation.  However, analysing larger confusion matrices is aided by visualisation because I consider that general summary statistics such as coefficients or residuals miss nuances that clients would benefit from.  In particular, given that the true positive values form a diagonal line from top-left to bottom-right in the matrix and that each true positive has only a single row of false positives and a single column of false negatives, the large number of all other true negative cells makes it difficult to grasp nuances within the results.

Analysing this sample confusion matrix to find out how accurate account forecasts were for a given prediction range (20-25%, lower bound) provides the TFF pie chart below.  The irrelevant true negatives are not displayed and ignored, and it is immediately clear that the true positive forecast is below 25%.  However, when the true positive segment is are added to the 'near miss' false positive segment (15-20% and 25-30% in this example) they form the majority of the positive forecasts.  The false negative ring is formed of forecasts of different profit margins with an outcome that matched the true positive forecast.  The relative sizes of these coloured regions allow essentials to be grasped quickly to direct further lines of enquiry. 

![alt text][TFFpieChart20pc]

To explain each component please compare the colours and sizes of the the TFF pie chart components with the following sample figure with coloured rows and columns.  Note that the TFF pie chart was calculated from values in the confusion matrix above, not the sample below.

![alt text][colourKeyGuide]

These Tobechukwu pie charts should be used in conjunction with other graphical analyses of account data.  Combining different representations allows insights to be combined and modified:  the 'cliff' at 0% in the left-hand scatterplot below is not visible in the central violin plot which suggests it is not significant when considering a company's overall performance.  However, it is obvious in the right-hand histogram, and similar counts at 5% and 10% in the histogram reveal a predilection to record results in multiples of 5%.  Whether any action will be taken is up to the client, and TFF pie charts may help inform them to change the way forecasting is done.

![alt text][threePlots]


(Tobechukwu is a gender-neutral Igbo name, pronounced  tä be chü-(ˌ)kü;  ‘To’ as in ‘top’, ‘be’ as in ‘bet’, ‘chukwu’ as in ‘cuckoo’ but with ‘ch’ as the first consonant.  Stresses are on the first and third syllables, it is a compound word.)

[textCMcloseRowsDiag]: https://github.com/narratorjay/TobechukwuPieChart/blob/master/reports/figures/textCMcloseRowsDiag.png
[TFFpieChart20pc]: https://github.com/narratorjay/TobechukwuPieChart/blob/master/reports/figures/TFF20pc-demo.png
[colourKeyGuide]: https://github.com/narratorjay/TobechukwuPieChart/blob/master/references/componentsOfTFFchart.png
[threePlots]: https://github.com/narratorjay/TobechukwuPieChart/blob/master/reports/figures/blankLeptoViolinHistoFigures.png




