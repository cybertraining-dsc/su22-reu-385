# from scipy.stats import f_oneway
#
# # test scores
# score1 = [89, 89, 88, 78, 79]
# score2 = [93, 92, 94, 89, 88]
# score3 = [89, 88, 89, 93, 90]
# score4 = [81, 78, 81, 92, 82]
#
# print(f_oneway(score1, score2, score3, score4))
#
# import pandas as pd
# import pingouin as pg
#
# data = "https://vincentarelbundock.github.io/Rdatasets/csv/datasets/PlantGrowth.csv"
#
# df = pd.read_csv(data, index_col=0)
#
# aov = pg.anova(data=df, dv='weight', between='group', detailed=True)
# print(aov)

# import pandas as pd
#
# datafile = "PlantGrowth.csv"
# data = pd.read_csv(datafile)
#
# #Create a boxplot
# data.boxplot('weight', by='group', figsize=(12, 8))
#
# ctrl = data['weight'][data.group == 'ctrl']
#
# grps = pd.unique(data.group.values)
# d_data = {grp:data['weight'][data.group == grp] for grp in grps}
#
# k = len(pd.unique(data.group))  # number of conditions
# N = len(data.values)  # conditions times participants
# n = data.groupby('group').size()[0] #Participants in each condition

# # Importing libraries
# import numpy as np
# import pandas as pd
# import statsmodels.api as sm
# from statsmodels.formula.api import ols
#
# # Create a dataframe
# dataframe = pd.DataFrame({'Fertilizer': np.repeat(['daily', 'weekly'], 15),
#                           'Watering': np.repeat(['daily', 'weekly'], 15),
#                           'height': [14, 16, 15, 15, 16, 13, 12, 11,
#                                      14, 15, 16, 16, 17, 18, 14, 13,
#                                      14, 14, 14, 15, 16, 16, 17, 18,
#                                      14, 13, 14, 14, 14, 15]})
#
# # Performing two-way ANOVA
# model = ols('height ~ C(Fertilizer) + C(Watering) +\
# C(Fertilizer):C(Watering)',
#             data=dataframe).fit()
# result = sm.stats.anova_lm(model, type=2)
#
# # Print the result
# print(result)
