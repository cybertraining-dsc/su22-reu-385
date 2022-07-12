# This formatted below code was gotten from :
# <https://www.geeksforgeeks.org/how-to-perform-a-one-way-anova-in-python/>
from scipy.stats import f_oneway

# test scores
score1 = [84, 86, 68, 98, 49]
score2 = [83, 29, 64, 89, 88]
score3 = [69, 88, 69, 73, 40]
score4 = [81, 70, 81, 92, 82]

print(f_oneway(score1, score2, score3, score4))

