#Larger list
#Here are the steps you need to complete this code challenge:
#Define a function that accepts two parameters for our two lists of numbers.
#Check if the length of the first list is greater than or equal to the length of the second list.
#If true, then return the last element from the first list. Otherwise, return the last element from the second list.

def larger_list(my_list1,my_list2):
  if len(my_list1) >= len(my_list2):
    return my_list1[-1]
  else:
    return my_list2[-1]

# Uncomment the line below when your function is done
print(larger_list([4, 10, 2, 5], [-10, 2, 5, 10]))