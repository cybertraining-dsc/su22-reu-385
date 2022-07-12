# This code was formatted from:
# <https://www.geeksforgeeks.org/how-to-check-if-time-series-data-is-stationary-with-python/>

# import python pandas package
import pandas as pd

# import the adfuller function from statsmodel
# package to perform ADF test
from statsmodels.tsa.stattools import adfuller

# read the dataset using pandas read_csv() function
data = pd.read_csv(
    "https://raw.githubusercontent.com/cybertraining-dsc/su22-reu-385/main/time-series-prediction/temperature2.csv",
    header=0, index_col=0)

# extracting only the passengers count using values function
value = data.values

# passing the extracted passengers count to adfuller function.
# result of adfuller function is stored in a res variable
res = adfuller(value)

# Printing the statistical result of the adfuller test
print('Augmneted Dickey_fuller Statistic: %f' % res[0])
print('p-value: %f' % res[1])

# printing the critical values at different alpha levels.
print('critical values at different levels:')
for l, m in res[4].items():
    print('\t%s: %.3f' % (l, m))
