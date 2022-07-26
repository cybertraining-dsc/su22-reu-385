Extensive documents on granger casualty test are available at

* <https://www.machinelearningplus.com/time-series/time-series-analysis-python/>

* <http://www.scholarpedia.org/article/Granger_causality#:~:text=Granger%20causality%20is%20a%20statistical,values%20of%20X2%20alone.>

# Granger casualty test

The Granger causality test is used to determine whether one time 
series can be used to predict another. "Granger causality is a statistical
concept of causality that is based on prediction. According to Granger causality,
if a signal $$X_1$$ "Granger-causes" (or "G-causes") a signal $$X_2$$, then past values of 
$$X_1$$ should contain information that helps predict $$X_2$$ above and beyond the 
information contained in past values of $$X_2$$ alone."

Example formatted From [1]

``` python
# Import Libaries 
import pandas as pd
from statsmodels.tsa.stattools import grangercausalitytests

# Read the CSV file
df = pd.read_csv('https://raw.githubusercontent.com/cybertraining-dsc/su22-reu-385/main/time-series-prediction/temp.csv', parse_dates=['date'])
df['month'] = df.date.dt.month
grangercausalitytests(df[['temperature', 'month']], maxlag=2)
```

The Max lag value give the granger causality test for the time 
period apart which in these case its (2). so the code above check 
if the previous time period which is (1)then use it to predict the 
next time period which is (2) it keeps going like that depending on 
the  max lag value

## Output
```
Granger Causality
number of lags (no zero) 1
ssr based F test:         F=2.7089  , p=0.1237  , df_denom=13, df_num=1
ssr based chi2 test:   chi2=3.3340  , p=0.0679  , df=1
likelihood ratio test: chi2=3.0285  , p=0.0818  , df=1
parameter F test:         F=2.7089  , p=0.1237  , df_denom=13, df_num=1

Granger Causality
number of lags (no zero) 2
ssr based F test:         F=1.4529  , p=0.2793  , df_denom=10, df_num=2
ssr based chi2 test:   chi2=4.3588  , p=0.1131  , df=2
likelihood ratio test: chi2=3.8265  , p=0.1476  , df=2
parameter F test:         F=1.4529  , p=0.2793  , df_denom=10, df_num=2
```

Test the following codes below:

* <https://github.com/cybertraining-dsc/su22-reu-385/blob/main/time-series-prediction/granger/granger.py>

## Reference

* [1] <https://www.machinelearningplus.com/time-series/time-series-analysis-python/>

* [2] <http://www.scholarpedia.org/article/Granger_causality#:~:text=Granger%20causality%20is%20a%20statistical,values%20of%20X2%20alone.>
