# This example was formatted from:
# https://machinelearningmastery.com/arima-for-time-series-forecasting-with-python/
# Published By : Jason BrownLee

from datetime import datetime
from pandas import read_csv
from pandas import DataFrame
from statsmodels.tsa.arima.model import ARIMA
from matplotlib import pyplot, pyplot as plt


# load dataset
def parser(x):
    return datetime.strptime('200' + x, '%Y-%m')


series = read_csv('https://raw.githubusercontent.com/cybertraining-dsc/su22-reu-385/main/time-series-prediction/temperature2.csv', header=0, index_col=0, parse_dates=True, squeeze=True, date_parser=parser)
series.index = series.index.to_period('M')
# fit model
model = ARIMA(series, order=(5, 1, 0))
model_fit = model.fit()
# summary of fit model
print(model_fit.summary())
# line plot of residuals
residuals = DataFrame(model_fit.resid)
residuals.plot()
pyplot.show()
# density plot of residuals
residuals.plot(kind='kde')
plt.savefig("model.svg")
pyplot.show()
# summary stats of residuals
print(residuals.describe())
