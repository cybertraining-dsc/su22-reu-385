# # https://en.wikipedia.org/wiki/Approximate_entropy
# import numpy as np
# import pandas as pd
# from sampen import sampen2
#
# df = [i ** 4.0 for i in range(10, 50)]
# #initialize a list
# series_data = []
# for row in df:
#     series_data.append(row)
#
# print((series_data))
# # # calculate the sample entropy
# # sampen_of_series = sampen2(series_data)

# from sampen import sampen2, normalize_data
#
# # initialize a list
# series_data = []
#
# # open the file and read each line into the list
# with open('sample-entropy/temp3.txt', 'r') as file:
#     for row in file:
#         series_data.append(float(row.strip(' \t\n\r')))
#
# # calculate the sample entropy
# print(series_data)
# sampen_of_series = sampen2(normalize_data(series_data))
# # print(sampen_of_series)
# import pandas as pd
# from statsmodels.tsa.stattools import grangercausalitytests
# df = pd.read_csv('https://raw.githubusercontent.com/cybertraining-dsc/su22-reu-385/main/time-series-prediction/temp.csv', parse_dates=['date'])
# df['month'] = df.date.dt.month
# grangercausalitytests(df[['temperature', 'month']], maxlag=2)

from sampen import sampen2, normalize_data

# initialize a list
series_data = []

# open the file and read each line into the list
with open('sample-entropy/temp3.txt', 'r') as file:
    for row in file:
        series_data.append(float(row.strip(' \t\n\r')))

# calculate the sample entropy
sampen_of_series = sampen2(series_data)
