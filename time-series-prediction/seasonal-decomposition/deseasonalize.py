# Example idea gotten from
# https://www.machinelearningplus.com/time-series/time-series-analysis-python/
from matplotlib import pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose

df = [i ** 4.0 for i in range(10, 1000)]

# Time Series Decomposition
result_mul = seasonal_decompose(df, model='multiplicative', period=60)

# Deseasonalize
deseasonalized = df / result_mul.seasonal

# Plot
plt.plot(deseasonalized)
plt.title('Data Deseasonalized', fontsize=15)
plt.show()
