Extensive documents on Detrend of Time Series are available at

* <https://www.statology.org/detrend-data/>

# Detrend a Time Series

Detrending time series data means removing an underlying trend 
from the data. The main reason for doing so is to make seasonal
or cyclical subtrends in the data more visible.

Time series data can be detrended using two methods:

* Detrend by Differencing

* Detrend by Model Fitting

## Detrend by Differencing

This method of Detrend time series that  deals with deal with finding 
the difference between the observation the inputting it into a new data set.
Example:
observation = [10, 16, 18, 21, 28, 34]

To get the detrend data set values you will do :

detrend_dataset = [16-10, 18-16, 21-18, 28-21, 34-28]

detrend_dataset = [6, 2, 3, 7, 6]

## Detrend by Model Fitting

The detrend by model Fitting is Fitting a regression model to the data and then 
calculating the difference between the observed and predicted values from the model.
Example:

observation = [10, 16, 18, 21, 28, 34]

predicted_observation = [9, 17, 20, 26, 32, 38 ]

Detrend_dataset = observation - predicted_observation

detrend_dataset = [10-9, 16-17, 18-20, 21-26, 28-32, 34-38]

detrend_dataset = [1, -1, -2, -5, -4, -4]


## Reference

* <https://www.statology.org/detrend-data/>
