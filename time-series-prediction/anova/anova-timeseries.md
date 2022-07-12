An extensive documentation on ANOVA Time series prediction is Available at
*  <https://www.statisticshowto.com/probability-and-statistics/hypothesis-testing/anova/>
*  <https://medium.com/@stallonejacob/time-series-forecast-a-basic-introduction-using-python-414fcb963000>
*  <https://www.geeksforgeeks.org/how-to-perform-a-two-way-anova-in-python/>
*  <https://www.geeksforgeeks.org/how-to-perform-a-one-way-anova-in-python/>

## ANOVA Time Series Prediction

An ANOVA test is used to determine whether survey or 
experiment results are significant. In other words, they 
assist you in determining whether you should reject the 
null hypothesis or accept the alternate hypothesis. it 
is categories into two namely:

* One Way ANOVA
* Two Way ANOVA


#### One Way ANOVA 

A one way ANOVA is used to compare two means from two 
independent (unrelated) groups using the F-distribution. 
The null hypothesis for the test is that the two means are 
equal. Therefore, a significant result means that the two 
means are unequal. a situation when these can be used is when 
a group of individuals randomly split into smaller groups and 
completing different tasks. For example, you might be studying 
the effects of tea on weight loss and form three groups: green tea, 
black tea, and no tea.

This example idea gotten from[4]

``` python

from scipy.stats import f_oneway

# test scores
score1 = [84, 86, 68, 98, 49]
score2 = [83, 29, 64, 89, 88]
score3 = [69, 88, 69, 73, 40]
score4 = [81, 70, 81, 92, 82]

print(f_oneway(score1, score2, score3, score4))
```

#### Two Way ANOVA

A Two Way ANOVA is an extension of the One Way ANOVA. With a 
One Way, you have one independent variable affecting a dependent 
variable. With a Two Way ANOVA, there are two independents. Use a 
Two way ANOVA when you have one measurement variable  and two nominal 
variables. In other words, if your experiment has a quantitative outcome, 
and you have two categorical explanatory variables, a two-way ANOVA is
appropriate.

This example idea gotten from[3]

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

### Time series prediction

Time series prediction is basically the machine learning 
modeling for Time Series data (years, days, hours…etc.)
for predicting future values using Time Series modeling .
This helps if your data in serially correlated.


### ANOVA Time series prediction

The ANOVA time series prediction deals with using the grand 
mean of the occurrence of past to predict the output of what 
the probable output will be in the future. the example below 
predict of a plant in a TWO way ANOVA.

This example is formatted from[3]

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

The example above gives a prediction of a person social media growth 
using two independent variables the users shared posts and comments and like,
and it predicts how these activities can affect user social media growth.


### ReferenceS

* [1] <https://www.statisticshowto.com/probability-and-statistics/hypothesis-testing/anova/>
* [2] <https://medium.com/@stallonejacob/time-series-forecast-a-basic-introduction-using-python-414fcb963000>
* [3] <https://www.geeksforgeeks.org/how-to-perform-a-two-way-anova-in-python/>
* [4] <https://www.geeksforgeeks.org/how-to-perform-a-one-way-anova-in-python/>