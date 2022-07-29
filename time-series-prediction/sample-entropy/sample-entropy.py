# Example formatted from
# <https://sampen.readthedocs.io/en/stable/>
# DataSET
# <https://www.physionet.org/content/sampen/1.0.0/c/sampentest.txt>
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
