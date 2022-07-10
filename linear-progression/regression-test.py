
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
plt.savefig("model.svg")
plt.show()

# soil fertility
sns.relplot(rainfall, soil_fertility)
sns.regplot(rainfall, Y2_pred)
plt.xlabel("Rain Fall")
plt.ylabel("soil fertility ")
plt.savefig("models.svg")
plt.show()


