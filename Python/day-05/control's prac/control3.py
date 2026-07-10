#Create a function named large_power() that takes two parameters named base and exponent.
#If base raised to the exponent is greater than 5000, return True, otherwise return False

def large_power(base, exponenet):
  if base ** exponenet > 5000:
    return True
  else:
    return False

print(large_power(2, 13))

print(large_power(2, 12))