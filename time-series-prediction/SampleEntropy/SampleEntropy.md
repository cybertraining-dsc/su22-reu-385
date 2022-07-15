Extensive documents on Sample Entropy are available at

* <https://pythonmana.com/2022/130/202205101057060253.html>

* <https://www.machinelearningplus.com/time-series/time-series-analysis-python/>

* <https://sampen.readthedocs.io/en/stable/>

# Sample Entropy

Approximate entropy a technique for quantifying the amount of 
regularity and unpredictability in time-series data. so what is 
sample Entropy ?"Sample Entropy is similar to approximate entropy 
but is more consistent in estimating the complexity even for smaller
time series. For example, a random time series with fewer data points
can have a lower ‘approximate entropy’ than a more ‘regular’ time series, 
whereas, a longer random time series will have a higher ‘approximate entropy’."

to use the library you will install using `pip`

```bash
$ pip install sampen
```

``` python
from sampen import sampen2, normalize_data

# initialize a list
series_data = []

# open the file and read each line into the list
with open('temp3.txt', 'r') as file:
    for row in file:
        series_data.append(float(row.strip(' \t\n\r')))

# calculate the sample entropy
print(series_data)
sampen_of_series = sampen2(normalize_data(series_data))
print(sampen_of_series)
```

## Reference

* <https://pythonmana.com/2022/130/202205101057060253.html>

* <https://www.machinelearningplus.com/time-series/time-series-analysis-python/>

* <https://sampen.readthedocs.io/en/stable/>

### Dataset:
* <https://www.physionet.org/content/sampen/1.0.0/c/sampentest.txt>


