# This formatted below code was gotten from :
# <https://www.geeksforgeeks.org/how-to-perform-a-two-way-anova-in-python/>
import numpy as np
import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols

# Create a dataframe
dataframe = pd.DataFrame({'shared_post': np.repeat(['daily', 'weekly'], 15),
                          'comments_likes': np.repeat(['daily', 'weekly'], 15),
                          'SocialMedia_growth': [10, 18, 16, 14, 19, 16, 18, 14,
                                                 17, 18, 17, 17, 18, 17, 19, 11,
                                                 16, 15, 15, 16, 17, 15, 16, 15,
                                                 19, 11, 18, 15, 15, 12]})

# Performing two-way ANOVA
result = sm.stats.anova_lm(ols('SocialMedia_growth ~ C(shared_post) + C(comments_likes) +\
C(shared_post):C(comments_likes)', data=dataframe).fit(), type=2)

# Print the result
print(result)