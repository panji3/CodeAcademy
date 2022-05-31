hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

#Total Price
total_price = 0

for price in prices:
  total_price += price
print("Total Price :",total_price)

#Avg Price
sum_price = len(prices)
average_price = total_price/sum_price
print("Average Haircut Price :",average_price)

#New Prices
new_prices = [x-5 for x in prices]
print("The New Prices :", new_prices)

#Total Revenue
total_revenue = 0
sum_hairstyle = len(hairstyles)

for i in range(len(hairstyles)):
  total_revenue += prices[i] * last_week[i]

print("Total Revenue :", total_revenue)

#Avg Daily Revenue
average_daily_revenue = total_revenue/7
print("Avg Daily Revenue :",average_daily_revenue)

#Find haircuts that are under 30 dollars
cuts_under_30 = [prices[i] for i in range(len(hairstyles)) if prices[i] < 30]

print("haircuts that are under 30 dollars :",cuts_under_30)
 
