# This code was formatted from:
# <https://www.statsmodels.org/devel/examples/notebooks/generated/stationarity_detrending_adf_kpss.html>
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
