# Sample Entropy

Approximate entropy a technique for quantifying the amount of 
regularity and unpredictability in time-series data. so what is 
sample Entropy? "Sample Entropy is similar to approximate entropy 
but is more consistent in estimating the complexity even for smaller
time series. For example, a random time series with fewer data 
points can have a lower ‘approximate entropy’ than a more ‘regular’
time series, whereas, a longer random time series will have a higher
‘approximate entropy’."

* [Sample entropy (Python Implementation)](https://pythonmana.com/2022/130/202205101057060253.html) [@sample-entropy]

* [Time Series Analysis in Python – A Comprehensive Guide with Examples](https://www.machinelearningplus.com/time-series/time-series-analysis-python/) [@time-series-analysis-guide]

* [SampEn](https://sampen.readthedocs.io/en/stable/) [@sampen]

to use the library you will install using `pip`

```bash
$ pip install sampen
```

The following example showcase the Sample Entropy. It is copied from [@sampen]

``` python
from sampen import sampen2, normalize_data

# initialize a list
series_data = []

# open the file and read each line into the list
with open('temp3.txt', 'r') as file:
    for row in file:
        series_data.append(float(row.strip(' \t\n\r')))

# calculate the sample entropy
sampen_of_series = sampen2(normalize_data(series_data))
print(sampen_of_series)
```

## Output 

```

[(0, 2.196817997610929, 0.002684778756853663),

 (1, 2.2248168592127824, 0.004639787747652105), 
 
 (2, 2.1972245773362196, 0.007540128072706757)]
```

### Output Breakdown

``` 
# Epoch length for max epoch
  2,
  
# SampEn
  2.1972245773362196
  
# Standard Deviation
  0.007540128072706757

```
Example programs to showcase specific features are listed next:

* [Sample Entropy, sample-entropy.py](https://github.com/cybertraining-dsc/su22-reu-385/blob/main/time-series-prediction/sample-entropy/sample-entropy.py)





