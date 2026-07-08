#mini project given instructions
hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

total_price = 0

#looping a for loop to loop through the prices list and adding it to a new list
for i in prices:
  total_price += i
print(total_price)

#finding average price by dividing total price by prices
average_price = total_price / len(prices)
print("Average Haircut Price:", average_price)

#lessing the prices by -5 and adding them to a new list
new_prices = [ i-5 for i in prices]
print(new_prices)

#finding neew total revenue to know how much revenue was brought in last week
total_revenue = 0
for i in range(len(hairstyles)):
  total_revenue = prices[i] + last_week[i]

print("Total Revenue:", total_revenue)

#finding average daily revenue
average_daily_revenue = total_revenue / 7
print(average_daily_revenue)

#bringing in more customers by advertising the cuts which are under 30$
cuts_under_30 = [hairstyles[i] for i in range(len(new_prices)) if new_prices[i] < 30]
print(cuts_under_30)