# This code was copied from:
# <https://machinelearningmastery.com/decompose-time-series-data-trend-seasonality/#:~:text=The%20statsmodels%20library%20provides%20an,model%20is%20additive%20or%20multiplicative.>
# Published By : Jason BrownLee

from random import randrange
from matplotlib import pyplot
from statsmodels.tsa.seasonal import seasonal_decompose
data = [i+randrange(15) for i in range(5,90)]
result = seasonal_decompose(data, model='additive', period=3)
result.plot()
pyplot.show()