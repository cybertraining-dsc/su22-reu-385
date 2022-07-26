# Regression In Python

Extensive documents on Linear Regression are available at

*  <https://www.w3schools.com/python/python_ml_linear_regression.asp>

*  <https://www.youtube.com/watch?v=NUXdtN1W1FE>

 
linear regression is classified as supervised data. 
It is a statistical model that is used to forecast the relationship between
independent and dependent variables. It is divided into three categories:

* Simple linear regression
* Multiple linear regression
* Polynomial linear regression

## Simple Linear Regression

Simple linear regression deals with only the dependent and independent variables.
For example, linear regression can be used to predict the amount of food to be 
cultivated using only two variables:crop yield and rainfall, where rainfall is the 
independent variable and crop yield is the dependent variable. the simple linear 
regression basically use the formular 

$$y = mx + c$$

where, $y$ is the dependent variable, $m$ is 
the slope, $x$ is the in dependent variable , and $c$ is the intercept

### Python Example

``` python

import seaborn as sns
import matplotlib.pyplot as plt

rainfall = [1, 3, 5, 7, 9, 11]
crop_yield = [5, 12, 14, 50, 67, 20]
soil_fertility = [6, 7, 8, 9, 10, 6]
# getting the regression line
U = 0
Z = 0
L = 0
product = []
Y_pred = []
n = len(rainfall)
for cum_rain in rainfall:
    U = cum_rain * cum_rain
    U += U
    cum_rain += cum_rain

for cum_crop in crop_yield:
    Z = cum_crop * cum_crop
    Z += Z
    cum_crop += cum_crop

for num1, num2 in zip(rainfall, crop_yield):
    product.append(num1 * num2)

for pro in product:
    pro += pro

m = ((n * pro) - (cum_crop * cum_rain)) / ((n * U) - (cum_rain * cum_rain))
c = ((cum_crop * U) - (cum_rain * pro))/ ((n * U) - (cum_rain * cum_rain))
v = 0

for fall in rainfall:
    Y_pred.append((m * fall) + c)


#Rainfall as related to crop yield
sns.relplot(rainfall, crop_yield)
sns.regplot(rainfall, Y_pred)
plt.xlabel("Rain Fall")
plt.ylabel("Crop yield ")
plt.show()

```

## Multiple Linear Regression

The multiple linear regression, unlike the simple linear regression, requires 
more than two factors in the example given above. which requires only the crop
yield and the amount of rainfall, the multiple linear regressions require more 
than that, such as pest infestation, animals perking around the crops, and soil 
fertility where all these factors are independent variable to the crop yield. The 
multiple linear regression use formular 

$$y = m_1x_1 + m_2x_2 +m_3x_3 ..... + c$$

where $$y$$
is the dependent variable, $$m$$ is the slope, $$x$$ is the in dependent variable , and $$c$$
is the intercept.

### Python Example

``` python

import seaborn as sns
import matplotlib.pyplot as plt

rainfall = [1, 3, 5, 7, 9, 11]
crop_yield = [5, 12, 14, 50, 67, 20]
soil_fertility = [6, 7, 8, 9, 10, 6]

# getting the regression line
U = 0
Z = 0
L = 0
product = []
Y_pred = []
product_2 = []
Y2_pred = []
n = len(rainfall)
for cum_rain in rainfall:
    U = cum_rain * cum_rain
    U += U
    cum_rain += cum_rain

for soil in soil_fertility:
    Z = soil * soil
    Z += Z
    soil += soil

for cum_crop in crop_yield:
    Z = cum_crop * cum_crop
    Z += Z
    cum_crop += cum_crop

for num1, num2 in zip(rainfall, crop_yield):
    product.append(num1 * num2)

for num1, num2 in zip(rainfall, soil_fertility):
    product_2.append(num1 * num2)

for pro in product:
    pro += pro
for pro2 in product_2:
    pro2 += pro2

m = ((n * pro) - (cum_crop * cum_rain)) / ((n * U) - (cum_rain * cum_rain))
c = ((cum_crop * U) - (cum_rain * pro))/ ((n * U) - (cum_rain * cum_rain))

m2 = ((n * pro2) - (soil * cum_rain)) / ((n * U) - (cum_rain * cum_rain))
c2 = ((soil * U) - (cum_rain * pro2)) / ((n * U) - (cum_rain * cum_rain))

v = 0
for fall in rainfall:
    Y_pred.append((m * fall) + c)
    Y2_pred.append(m2 * fall + c2)



#Rainfall as related to crop yield
sns.relplot(rainfall, crop_yield)
sns.regplot(rainfall, Y_pred)
plt.xlabel("Rain Fall")
plt.ylabel("Crop yield ")
plt.show()

# soil fertility
sns.relplot(rainfall, soil_fertility)
sns.regplot(rainfall, Y2_pred)
plt.xlabel("Rain Fall")
plt.ylabel("soil fertility ")
plt.show()


```


## Polynomial Linear Regression

Unlike simple and multiple linear regression, which use straight lines to 
show the relationship between the dependent and independent variables, polynomial
linear regression uses a curved line to show the relationship between the two variables.

### Python Example

``` python* 
import numpy
import seaborn as sns
import matplotlib.pyplot as plt
rainfall = [1, 3, 5, 7, 9, 11]
crop_yield = [5, 12, 14, 50, 67, 20]


# Rainfall as related to crop yield
sns.relplot(x=rainfall, y=crop_yield)
mymodel = numpy.poly1d(numpy.polyfit(rainfall, crop_yield, 2))
myline = numpy.linspace(1, 20, 30)
plt.plot(myline, mymodel(myline))
plt.xlabel("Rain Fall")
plt.ylabel("Crop yield ")
plt.show()

```

## References
* [1] Machine Learning - Linear Regression <https://www.w3schools.com/python/python_ml_linear_regression.asp>

* [2] <https://www.youtube.com/watch?v=NUXdtN1W1FE>



