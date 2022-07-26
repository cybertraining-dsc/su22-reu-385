# Stationary and Non-Stationary Time Series

Extensive documents on stationary and Non-Stationary Time Series are available at

* <https://www.machinelearningplus.com/time-series/time-series-analysis-python/>

* <https://www.investopedia.com/articles/trading/07/stationary.asp#:~:text=Non%2DStationary%20Processes-,Non%2DStationary%20Time%20Series%20Data,cannot%20be%20modeled%20or%20forecasted.>

* <https://www.analyticsvidhya.com/blog/2018/09/non-stationary-time-series-python/>

* <https://www.geeksforgeeks.org/how-to-check-if-time-series-data-is-stationary-with-python/>

* <https://www.statsmodels.org/devel/examples/notebooks/generated/stationarity_detrending_adf_kpss.html>


## Stationary Time series

A stationary time series has statistical properties or moments 
that do not change over time (for example, mean and variance).

The series' statistical properties, such as mean, variance, and 
auto correlation, remain constant over time. The auto correlation
of a series is simply the correlation of the series with its 
previous values.


### How to make a time series stationary?

You can make series stationary by:

* Differencing the Series (once or more)
* Take the log of the series
* Take the nth root of the series
* Combination of the above

The most common and convenient method is Differencing the series

#### Differencing the Series (once or more)

If $$y_t$$ is the value at time '$$t$$,' the first difference of $$y$$ equals
$$y_t - y_{t-1}$$. To put it simply, differencing the series is simply subtracting
the next value from the current value.

If the first difference does not make a series stationary, the second 
differencing can be used. And so forth.

* Consider the following sequence: `[8, 6, 4, 10, 25]`.
* First differencing gives: `[6-8, 4-6, 10-4, 25-10] = [-2, -2, 6, 15]`
* Second differencing gives: `[-2-(-2), 6-(-2), 15-6] = [0, 8, 9]`
## Non-Stationary Time series

Data points are frequently non-stationary or have changing means,
variances, and covariances. Trends, cycles, random walks, and combinations 
of the three are examples of non-stationary behaviors.

While forecasting, it is recommended to convert a non-stationary series to a 
stationary series because autoregressive forecasting models are essentially linear
regression models that use the lag(s) of the series itself as predictors.


## How to test for stationary?

A method for determining whether a given series is stationary. This 
is possible with statistical tests known as 'Unit Root Tests.' There 
are several variants of this in which the tests determine whether a 
time series is non-stationary and has a unit root.

Unit Root tests are implemented in a variety of ways, which includes:

* Visual Test
* Statistical test
* Kwiatkowski-Phillips-Schmidt-Shin – KPSS test (trend stationary)


### Visual Test

simply by looking at each plot, being able to identify the series in which 
the mean and variance changed over time Similarly, we can plot the data to 
see if the properties of the series change over time.



``` python
from pandas import read_csv
from matplotlib import pyplot
data = read_csv('https://raw.githubusercontent.com/cybertraining-dsc/su22-reu-385/main/time-series-prediction/temperature2.csv', header=0, index_col=0)
data.plot()

pyplot.show()
```

![TODO CAPTION MISSING](images/stationary-img.png)

### Statistical test

Statistical tests such as the unit root stationary tests can be used. The 
presence of a unit root indicates that the statistical properties of a given
series are not constant over time, which is required for stationary time series.
The following is a mathematical explanation:

Suppose we have a time series

$$y_t = a*y_{t-1} + \epsilon_t$$

where yt is the value at the time instant $$t$$ and $$\epsilon_t$$ is the error term. In order to
calculate yt we need the value of $$y_{t-1}$$, which is

$$y_{t-1} = a*y_{t-2} + \epsilon_{t-1}$$

If we do that for all observations, the value of y_t will come out to be:

$$y_t = a^n \times y_{t-n} + \sum \epsilon_t-i \times a^i$$

### Augmented Dickey Fuller test (ADH Test)

The Dickey-Fuller test is a well-known statistical test. It can be used to determine 
whether a series contains a unit root, and thus whether the series is stationary.
This test's null and alternate hypotheses are as follows:

Example Formatted from [4]

```python
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
```

* Null Hypothesis: The series has a unit root (value of `a=1`)

* Alternate Hypothesis: The series has no unit root.

### Kwiatkowski-Phillips-Schmidt-Shin – KPSS test 

KPSS is yet another test for determining a time series' stationarity (slightly less 
popular than the Dickey-Fuller test). The null and alternate hypotheses for the KPSS 
test are the inverse of those for the ADF test, which frequently leads to confusion.
The KPSS test's authors defined the null hypothesis as the process being trend stationary,
as opposed to an alternate hypothesis of a unit root series.

Example Formatted from [5]

```python
import pandas as pd
from statsmodels.tsa.stattools import kpss

data = pd.read_csv(
    "https://raw.githubusercontent.com/cybertraining-dsc/su22-reu-385/main/time-series-prediction/temperature2.csv",
    header=0, index_col=0)
print("Results of KPSS Test:")
kpsstest = kpss(data, regression="c", nlags="auto")
kpss_output = pd.Series(
    kpsstest[0:3], index=["Test Statistic", "p-value", "Lags Used"]
)
for num, test in kpsstest[3].items():
    kpss_output["Critical Value (%s)" % num] = test
print(kpss_output)

```

* Null Hypothesis: The process is trend stationary.

* Alternate Hypothesis: The series has a unit root (series is not stationary).

## Types of Stationary Time series

### Strict Stationary

A series that has no unit root but exhibits a trend is referred to as a trend stationary 
series. Once the trend is removed, the resulting series will be strict stationary. The KPSS 
test classifies a series as stationary on the absence of unit root. This means that the 
series can be strict stationary or trend stationary.

### Trend Stationary

A trend stationary series is one that does not have a unit root but exhibits a trend. The
resulting series will be strictly stationary once the trend is removed. The KPSS test determines
whether a series is stationary based on the absence of a unit root. As a result, the series can be
either strict stationary or trend stationary.

### Difference Stationary

A difference stationary time series is one that can be made strict stationary by differencing.
ADF tests are also referred to as difference Stationary tests.

Test the following code below:

* Augmented Dickey Fuller test (ADH Test) <https://github.com/cybertraining-dsc/su22-reu-385/blob/main/time-series-prediction/stationary-and-nonstationary-timeseries/adh-test.py>

* Visual Test <https://github.com/cybertraining-dsc/su22-reu-385/blob/main/time-series-prediction/stationary-and-nonstationary-timeseries/visual.py>

* Kwiatkowski-Phillips-Schmidt-Shin – KPSS test <https://github.com/cybertraining-dsc/su22-reu-385/blob/main/time-series-prediction/stationary-and-nonstationary-timeseries/kpss.py>

## References

* [1] Time Series Analysis in Python <https://www.machinelearningplus.com/time-series/time-series-analysis-python/>

* [2] Intro to Stationary and Non-Stationary Processes <https://www.investopedia.com/articles/trading/07/stationary.asp#:~:text=Non%2DStationary%20Processes-,Non%2DStationary%20Time%20Series%20Data,cannot%20be%20modeled%20or%20forecasted.>

* [3] Methods to Check Stationary <https://www.analyticsvidhya.com/blog/2018/09/non-stationary-time-series-python/>

* [4] How to Check if Time Series Data is Stationary with Python? <https://www.geeksforgeeks.org/how-to-check-if-time-series-data-is-stationary-with-python/>

* [5] Stationarity and detrending (ADF/KPSS) <https://www.statsmodels.org/devel/examples/notebooks/generated/stationarity_detrending_adf_kpss.html>
