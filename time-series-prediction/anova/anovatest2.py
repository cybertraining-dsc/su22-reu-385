# This formatted below code was gotten from :
# <https://www.geeksforgeeks.org/how-to-perform-a-two-way-anova-in-python/>
import numpy as np
import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols

# Create a dataframe
dataframe = pd.DataFrame({'Fertilizer': np.repeat(['daily', 'weekly'], 15),
                          'Watering': np.repeat(['daily', 'weekly'], 15),
                          'height': [14, 16, 15, 15, 16, 13, 12, 11,
                                     14, 15, 16, 16, 17, 18, 14, 13,
                                     14, 14, 14, 15, 16, 16, 17, 18,
                                     14, 13, 14, 14, 14, 15]})

# Performing two-way ANOVA
model = ols('height ~ C(Fertilizer) + C(Watering) +\
C(Fertilizer):C(Watering)',
            data=dataframe).fit()
result = sm.stats.anova_lm(model, type=2)

# Print the result
print(result)