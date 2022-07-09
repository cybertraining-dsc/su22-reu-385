##  Stationary and Non-Stationary Time Series

### Stationary Time series
A stationary time series has statistical properties or moments that do not change 
over time (for example, mean and variance).

The series' statistical properties, such as mean, variance, and autocorrelation, remain 
constant over time. The auto correlation of a series is simply the correlation of the 
series with its previous values.

#### How to make a time series stationary?

You can make series stationary by:

* Differencing the Series (once or more)
* Take the log of the series
* Take the nth root of the series
* Combination of the above

The most common and convenient method 
##### Differencing the Series (once or more)

If Y_t is the value at time 't,' the first difference of Y equals Yt - Yt-1. To put it
simply, differencing the series is simply subtracting the next value from the current value.

If the first difference does not make a series stationary, the second differencing 
can be used. And so forth.

Consider the following sequence: [8, 6, 4, 10, 25].
First differencing gives: [6-8, 4-6, 10-4, 25-10] = [-2, -2, 6, 15]
Second differencing gives: [-2-(-2), 6-(-2), 15-6] = [0, 8, 9]

### Non-Stationary Time series

Data points are frequently non-stationary or have changing means, variances, and covariances. Trends,
cycles, random walks, and combinations of the three are examples of non-stationary behaviors.


Reference: https://www.machinelearningplus.com/time-series/time-series-analysis-python/
Reference: https://www.investopedia.com/articles/trading/07/stationary.asp#:~:text=Non%2DStationary%20Processes-,Non%2DStationary%20Time%20Series%20Data,cannot%20be%20modeled%20or%20forecasted.