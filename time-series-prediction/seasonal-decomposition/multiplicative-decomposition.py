# This code was copied from:
# <https://machinelearningmastery.com/decompose-time-series-data-trend-seasonality/#:~:text=The%20statsmodels%20library%20provides%20an,model%20is%20additive%20or%20multiplicative.>
# Published By : Jason BrownLee
from matplotlib import pyplot
from statsmodels.tsa.seasonal import seasonal_decompose

series = [i**2.0 for i in range(1,100)]
result = seasonal_decompose(series, model='multiplicative', period=1)
result.plot()
pyplot.show()