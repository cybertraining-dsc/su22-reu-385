Extensive documents on granger casualty test are available at

* <https://www.machinelearningplus.com/time-series/time-series-analysis-python/>


# Granger casualty test

The Granger causality test is used to determine whether one time 
series can be used to predict another.

## How Granger causality test works

It is predicated on the idea that if X causes Y, then forecasting Y based 
on previous values of Y AND previous values of X should outperform forecasting
Y based on previous values of Y alone. "Granger causality should not be used to 
test if a lag of Y causes Y. Instead, it is generally used on exogenous (not Y lag) 
variables only."

``` python
import pandas as pd
from statsmodels.tsa.stattools import grangercausalitytests
df = pd.read_csv('https://raw.githubusercontent.com/cybertraining-dsc/su22-reu-385/main/time-series-prediction/temp.csv', parse_dates=['date'])
df['month'] = df.date.dt.month
grangercausalitytests(df[['temperature', 'month']], maxlag=2)
```

## Reference

* <https://www.machinelearningplus.com/time-series/time-series-analysis-python/>