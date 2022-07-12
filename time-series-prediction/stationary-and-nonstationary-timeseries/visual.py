from pandas import read_csv
from matplotlib import pyplot
data = read_csv('https://raw.githubusercontent.com/cybertraining-dsc/su22-reu-385/main/time-series-prediction/temperature2.csv', header=0, index_col=0)
data.plot()
pyplot.show()