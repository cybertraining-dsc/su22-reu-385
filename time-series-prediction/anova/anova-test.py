# This formatted below code was gotten from :
# <https://www.geeksforgeeks.org/how-to-perform-a-one-way-anova-in-python/>
from scipy.stats import f_oneway

# test scores
score1 = [89, 89, 88, 78, 79]
score2 = [93, 92, 94, 89, 88]
score3 = [89, 88, 89, 93, 90]
score4 = [81, 78, 81, 92, 82]

print(f_oneway(score1, score2, score3, score4))

