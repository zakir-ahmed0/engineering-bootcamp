# Your code below:
#creating the list of toppings in a pizza shop
toppings = ['pepperoni', 'pineapple', 'cheese', 'sausage', 'olives', 'anchovies', 'mushrooms']
#prices for each slice of pizza
prices = [2,6,1,3,2,7,2]
#counting the 2$ slices available
num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)
#finding the length of the toppings in the store
num_pizzas = len(toppings)
print('We sell', num_pizzas, 'different kinds of pizza!')
#using existing data to create a 2d list for the store
pizza_and_prices = [[2, 'pepperoni'], [6, 'pineapple'], [1, 'cheese'], [3, 'sausage'], [2, 'olives'], [7, 'anchovies'], [2, 'mushrooms']]
print(pizza_and_prices)
#sorting the 2d list in ascending order
pizza_and_prices.sort()
print(pizza_and_prices)
#storing the cheapest pizza in a variable
cheapest_pizza = pizza_and_prices[0]
#storing the costliest pizza in a variable
priciest_pizza = pizza_and_prices[-1]
#popping out the costlies slice since someone bought it and it's out of stock
pizza_and_prices.pop()
#inserting a different kind of pizza to cover for the finished pizza slice
pizza_and_prices.insert(4, [2.5, 'peppers'])
print(pizza_and_prices)
#finding the 3 cheapest pizza slices in a list
three_cheapest = pizza_and_prices[0:3]
print(three_cheapest)