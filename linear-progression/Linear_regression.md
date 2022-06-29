## Regression in python
 
In machine learning, linear regression is classified as supervised data. It is a statistical 
model that is used to forecast the relationship between independent and dependent variables.
It is divided into three categories:

* Simple linear regression
* Multiple linear regression
* Polynomial linear regression

### Simple Linear Regression

Simple linear regression deals with only the dependent and independent variables. For example, linear
regression can be used to predict the amount of food to be cultivated using only two variables: 
crop yield and rainfall, where rainfall is the independent variable and crop yield is the dependent 
variable. the simple linear regression basically use the formular `y = mx +c`
y is the dependent variable, m is the slop, x is the in dependent variable , and c is the intercept

##### Python example
``` python
import seaborn as sns
import matplotlib.pyplot as plt
rainfall = [1, 3, 5, 7, 9, 11]
crop_yield = [5, 12, 14, 50, 67, 20]

sns.relplot(x=rainfall, y=crop_yield)
sns.regplot(x=rainfall, y=crop_yield)
plt.xlabel("Rain Fall")
plt.ylabel("Crop yield ")
plt.show()
```

### Multiple Linear Regression

The multiple linear regression, unlike the simple linear regression, requires more than two factors in the 
example given above. which requires only the crop yield and the amount of rainfall, the multiple linear regressions 
require more than that, such as pest infestation, animals perking around the crops, and soil fertility where all these factors
are independent variable to the crop yield. The multiple linear regression use formular `y = M1X1 + M2X2 +M3X3 ..... + C`
where y is the dependent variable, M is the slop, X is the in dependent variable , and C is the intercept.

#### python example

``` python
import seaborn as sns
import matplotlib.pyplot as plt
rainfall = [1, 3, 5, 7, 9, 11]
soil_fertility = [6, 7, 8, 9, 10, 6]
crop_yield = [5, 12, 14, 50, 67, 20]

# Rainfall as related to crop yield
sns.relplot(x=rainfall, y=crop_yield)
sns.regplot(x=rainfall, y=crop_yield)
plt.xlabel("Rain Fall")
plt.ylabel("Crop yield ")
plt.show()

# soil fertility as related to crop yield
sns.relplot(x=soil_fertility, y=crop_yield)
sns.regplot(x= soil_fertility, y=crop_yield)
plt.xlabel("Soil fertility")
plt.ylabel("Crop yield ")
plt.show()

```

### Polynomial Linear Regression

Unlike simple and multiple linear regression, which use straight lines to show the relationship between the dependent 
and independent variables, polynomial linear regression uses a curved line to show the relationship between the two 
variables.

#### python example

``` python
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