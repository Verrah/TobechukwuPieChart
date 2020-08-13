# Tobechukwu pie chart
### The web's first pie chart for confusion matrices.  Named in accordance with Stigler's law.
### Best described as True-False-False 'TFF' pie charts.


Visualises data in a typical confusion matrix to add insight about prediction or identification.  (One day I'll be able to format tables in a readme.)
0   0	  0	  0	  0	    0	  0	  0	  0	  0

0	  1	  0	  0	  0	    0	  0	  0	  0	  0

1	  1	  0	  0	  0	    0	  0	  0	  0	  0

0	  5	  0	  0	  0	    0	  1	  0	  0	  0

44	147	255	243	88	  56	44	19	22	5

103	296	839	974	541	  268	157	88	70	31

151	306	667	998	1309	790	403	288	224	160

26	40	178	167	287	  380	255	135	123	70

25	27	66	74	97	  103	115	126	99	46

7	  11	4	  32	18	  24	9	  11	19	14

2	  4	  4	  0	  4	    8	  6	  8	  6	  7

0	  0	  1	  2	  1	    0	  1	  2	  0	  0


The conventional 2x2 confusion matrix of binary results for (typically) a pregnancy test needs little explanation.  However, analysing larger confusion matrices is aided by visualisation because I consider that general summary statistics such as coefficients or residuals miss nuances that clients would benefit from.  In particular, given that the true positive values form a diagonal line from top-left to bottom-right in the matrix and that each true positive has only a single row of false positives and a single column of false negatives, the large number of all other cells containing true negatives makes it difficult to grasp nuances within the results.

Analysing this sample confusion matrix to find out how accurate account forecasts were for a given prediction range (20-25%, lower bound) provides this TFF pie chart:

![alt text][TFFpieChart20pc]
To explain each component please compare the colours and sizes of the the TFF pie chart components with the following example confusion matrix with sample coloured rows and columns.  Note that the TFF pie chart was calculated from values in the confusion matrix above, not the sample below
![alt text][colourKeyGuide]
The irrelevant true negatives are not displayed and ignored, and it is immediately clear that the true positive forecast is below 25%.  However, when the true positive segment is are added to the 'near miss' false positive segment (15-20% and 25-30% in this example) they form the majority of the positive forecasts.  The false negative ring is formed of forecasts of different profit margins with an outcome that matched the true positive forecast.

This adds 


[TFFpieChart20pc]: https://github.com/narratorjay/TobechukwuPieChart/blob/master/reports/figures/TFF20pc-demo.png
[colourKeyGuide]:  https://github.com/narratorjay/TobechukwuPieChart/blob/master/references/componentsOfTFFchart.png




