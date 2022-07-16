# This code was formatted from:
# <https://machinelearningmastery.com/moving-average-smoothing-for-time-series-forecasting-python/#:~:text=Smoothing%20is%20a%20technique%20applied,of%20the%20underlying%20causal%20processes.>
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from statsmodels.nonparametric.smoothers_lowess import lowess

plt.rcParams.update({'xtick.bottom': False, 'axes.titlepad': 5})

# Import
df_orig = pd.read_csv(
    'https://raw.githubusercontent.com/cybertraining-dsc/su22-reu-385/main/time-series-prediction/temperature2.csv',
    parse_dates=['Month'], index_col='Month')

# 1. Moving Average
df_ma = df_orig.Temperature.rolling(3, center=True, closed='both').mean()

# 2. Loess Smoothing (5%)
df_loess_5 = pd.DataFrame(lowess(df_orig.Temperature, np.arange(len(df_orig.Temperature)), frac=0.05)[:, 1],
                          index=df_orig.index, columns=['Temperature'])

# Plot
fig, axes = plt.subplots(3, 1, figsize=(7, 7), sharex=True, dpi=120)
df_orig['Temperature'].plot(ax=axes[0], color='k', title='Original Series')
df_loess_5['Temperature'].plot(ax=axes[1], title='Loess Smoothed 5%')
df_ma.plot(ax=axes[2], title='Moving Average (3)')
fig.suptitle('How to Smoothen a Time Series', y=0.95, fontsize=14)
plt.show()
