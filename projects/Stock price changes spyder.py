import numpy as np
import matplotlib.pyplot as plt

initial_price = 100
days = 100
#np.random.seed()

daily_changes = np.random.uniform(-0.03, 0.04, days)

prices = [initial_price]

for change in daily_changes:
    new_price = prices[-1]*(1 + change)
    prices.append(new_price)
    
prices = np.array(prices)

gain_days = 0
loss_days = 0

for i in range(1, len(prices)):
    if prices[1] > prices [i-1]:
        gain_days += 1
    else:
        loss_days += 1
        
plt.figure(figsize = (15, 15))
plt.plot(prices, marker="o", linestyle = ":", color = "green")
plt.title("S&P 500 last 100 days")
plt.xlabel("Days")
plt.ylabel("Price")
plt.grid()
plt.show()

plt.figure(figsize = (15, 15))
plt.pie([gain_days, loss_days], labels = ["Gain days", "Loss days"], autopct="%1.1f%%", colors = ["green", "red"], startangle = 90)
plt.title("Distribution of gain days vs loss days")
plt.show()