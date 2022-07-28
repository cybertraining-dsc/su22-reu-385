# ANOVA Time Series Prediction

An extensive documentation on ANOVA Time series prediction are available at

* <https://www.statisticshowto.com/probability-and-statistics/hypothesis-testing/anova/>

* <https://medium.com/@stallonejacob/time-series-forecast-a-basic-introduction-using-python-414fcb963000>

* <https://www.geeksforgeeks.org/how-to-perform-a-two-way-anova-in-python/>

* <https://www.geeksforgeeks.org/how-to-perform-a-one-way-anova-in-python/>


An ANOVA test is used to determine whether survey or 
experiment results are significant. In other words, they 
assist you in determining whether you should reject the 
null hypothesis or accept the alternative hypothesis. it's 
categories into two namely: 

Note: A null hypothesis test predicts that there is 
no relationship between variables, whereas the alternative 
hypothesis states that your research predictions are related.

* One Way ANOVA
* Two Way ANOVA


## One Way ANOVA 

The one-way ANOVA method is used to determine whether there is 
a statistically significant difference between the mean values
of multiple groups. For example, you might be studying the 
amount of task for all the individual and given them a score
per how efficient they performed the task as shown.

Example from [4] @one-way-anova

``` python

from scipy.stats import f_oneway

# rated scores
score1 = [84, 86, 68, 98, 49]
score2 = [83, 29, 64, 89, 88]
score3 = [69, 88, 69, 73, 40]
score4 = [81, 70, 81, 92, 82]

scores_ave=  f_oneway(score1, score2, score3, score4)

print(scores_ave)
```

### Output

```

F_onewayResult(statistic=0.5410224469358347, pvalue=0.6610639388335927)

```
Note: With a P value less than 0.05, you reject the null hypothesis,
      With a P value greater than 0.05, you accept the null hypothesis 

#### Output Explanation

The statistic and p-value turn out to be equal to 0.5410 and 0.661063.
Since the p-value is greater than 0.05 hence we would accept the null 
hypothesis. This implies that we have sufficient proof to say that the
performance of the students are similar

## Two Way ANOVA

A Two Way ANOVA is an extension of the One Way ANOVA. With a 
One Way ANOVA, you have one independent variable affecting a dependent 
variable. With a Two Way ANOVA, there are two independents. Use a 
Two way ANOVA when you have one dependent variable and two independent 
variables. In other words, if your experiment has a quantitative outcome, 
and you have two independent variables, a two-way ANOVA is appropriate.
To manage a Two Way ANOVA data set two python libraries are helpful which 
are NumPy and panda. to perform the Two Way ANOVA the
statistical model is needed, known as the stats model. stats models is a
Python package that provides descriptive statistics and estimation and 
inference for statistical models. to install the python
libraries using `pip` 

Dataset Management Libraries
```
pip install numpy pandas
```

Statistical models Library
```
pip install statsmodels
```

Example from [3]  @two-way-anova

``` python
import numpy as np
import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols

# Create a dataframe
dataframe = pd.DataFrame({'shared_post': np.repeat(['daily', 'weekly'], 15),
                          'comments_likes': np.repeat(['daily', 'weekly'], 15),
                          'SocialMedia_growth': [10, 18, 16, 14, 19, 16, 18, 14,
                                                 17, 18, 17, 17, 18, 17, 19, 11,
                                                 16, 15, 15, 16, 17, 15, 16, 15,
                                                 19, 11, 18, 15, 15, 12]})

# Performing two-way ANOVA
result = sm.stats.anova_lm(ols('SocialMedia_growth ~ C(shared_post) + C(comments_likes) +\
C(shared_post):C(comments_likes)', data=dataframe).fit(), type=2)

# Print the result
print(result)
```

### Output

```
                                    df      sum_sq  ...         F    PR(>F)
C(shared_post)                     1.0   16.133333  ...  2.998230  0.094362
C(comments_likes)                  1.0    0.049552  ...  0.009209  0.924234
C(shared_post):C(comments_likes)   1.0    0.012326  ...  0.002291  0.962168
Residual                          28.0  150.666667  ...       NaN       NaN
```

### Output Explanation

Following are the p-values for each of the factors in the output:

The shared_post p-value is equal to 0.094362
The comments_likes p-value is equal to 0.924234
The shared_post * comments_likes: p-value is equal to 0.962168

The p-values for shared_post and comments_likes turn out 
to be greater than 0.05 which implies that the means of 
both the factors possess a similar effect on the user 
SocialMedia_growth. The p-value for the interaction effect 
(0.962168) is greater than 0.05 which shows the interaction 
effect between shared_post frequency and comments_likes frequency.

Test the following codes below:

* One Way ANOVA <https://github.com/cybertraining-dsc/su22-reu-385/blob/main/time-series-prediction/anova/anova-test.py>

* Two Way ANOVA <https://github.com/cybertraining-dsc/su22-reu-385/blob/main/time-series-prediction/anova/anovatest2.py>

## ANOVA Time series prediction

The ANOVA time series prediction deals with using the grand 
mean of the occurrence of past to predict the output of what 
the probable output will be in the future. the example in the TWO Way ANOVA
section that predicts a user social media growth is a perfect example of 
the predicting time series with ANOVA.

## Reference

* [1] anova-test <https://www.statisticshowto.com/probability-and-statistics/hypothesis-testing/anova/>

* [2] @time-series <https://medium.com/@stallonejacob/time-series-forecast-a-basic-introduction-using-python-414fcb963000>

* [3] @two-way-anova <https://www.geeksforgeeks.org/how-to-perform-a-two-way-anova-in-python/>

* [4] @one-way-anova <https://www.geeksforgeeks.org/how-to-perform-a-one-way-anova-in-python/>