# Import Libraries
import pandas as pd
from statsmodels.tsa.stattools import grangercausalitytests

# Read the CSV file
df = pd.read_csv(
    'https://raw.githubusercontent.com/cybertraining-dsc/su22-reu-385/main/time-series-prediction/temp.csv',
    parse_dates=['date'])
df['month'] = df.date.dt.month
grangercausalitytests(df[['temperature', 'month']], maxlag=4)
