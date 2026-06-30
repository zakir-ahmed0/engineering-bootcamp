#Restaurant_Bill_Program

Burger = 8.50
Drink = 2.20
Dessert = 4.00

tax = 0.20

subtotal = Burger + Drink + Dessert
total_tax = subtotal * tax
total = subtotal + total_tax

print("======Restaurant Bill=======")
print("                       ")
print("Burger:", Burger)
print("Drink:", Drink)
print("Dessert:", Dessert)
print("                   ")
print("Subtotal:", subtotal)
print("Tax:", total_tax)
print("-------------------------")
print("Total:", total)