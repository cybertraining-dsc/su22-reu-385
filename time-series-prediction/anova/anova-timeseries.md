
# Time Series Prediction

## ANOVA

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

``` python
from scipy.stats import f_oneway

# test scores
score1 = [89, 89, 88, 78, 79]
score2 = [93, 92, 94, 89, 88]
score3 = [89, 88, 89, 93, 90]
score4 = [81, 78, 81, 92, 82]

print(f_oneway(score1, score2, score3, score4))
```

#### Two Way ANOVA

A Two Way ANOVA is an extension of the One Way ANOVA. With a 
One Way, you have one independent variable affecting a dependent 
variable. With a Two Way ANOVA, there are two independents. Use a 
Two way ANOVA when you have one measurement variable  and two nominal 
variables. In other words, if your experiment has a quantitative outcome 
and you have two categorical explanatory variables, a two way ANOVA is
appropriate.

``` python
import numpy as np
import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols

# Create a dataframe
dataframe = pd.DataFrame({'Fertilizer': np.repeat(['daily', 'weekly'], 15),
                          'Watering': np.repeat(['daily', 'weekly'], 15),
                          'height': [14, 16, 15, 15, 16, 13, 12, 11,
                                     14, 15, 16, 16, 17, 18, 14, 13,
                                     14, 14, 14, 15, 16, 16, 17, 18,
                                     14, 13, 14, 14, 14, 15]})

# Performing two-way ANOVA
model = ols('height ~ C(Fertilizer) + C(Watering) +\
C(Fertilizer):C(Watering)',
            data=dataframe).fit()
result = sm.stats.anova_lm(model, type=2)

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

``` python
import numpy as np
import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols

# Create a dataframe
dataframe = pd.DataFrame({'Fertilizer': np.repeat(['daily', 'weekly'], 15),
                          'Watering': np.repeat(['daily', 'weekly'], 15),
                          'height': [14, 16, 15, 15, 16, 13, 12, 11,
                                     14, 15, 16, 16, 17, 18, 14, 13,
                                     14, 14, 14, 15, 16, 16, 17, 18,
                                     14, 13, 14, 14, 14, 15]})

# Performing two-way ANOVA
model = ols('height ~ C(Fertilizer) + C(Watering) +\
C(Fertilizer):C(Watering)',
            data=dataframe).fit()
result = sm.stats.anova_lm(model, type=2)

# Print the result
print(result)
```

This is an example of the of a time series prediction which
predict the result of a tree grown after





### Reference:

* <https://www.statisticshowto.com/probability-and-statistics/hypothesis-testing/anova/>
* <https://medium.com/@stallonejacob/time-series-forecast-a-basic-introduction-using-python-414fcb963000>
* <https://arxiv.org/abs/1912.09363>