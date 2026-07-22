#coming after a break of 3 days.. juggling work , university and side practice!!
#.strip() examples
# Python provides a great method for cleaning strings: .strip() Preview: Docs Removes leading and trailing whitespace or specified characters from a string
#Stripping a string removes all whitespace characters from the beginning and end. 

#have a list of a poem with a space between them so we are trying to clean the data 
love_maybe_lines = ['Always    ', '     in the middle of our bloodiest battles  ', 'you lay down your arms', '           like flowering mines    ','\n' ,'   to conquer me home.    ']

#assigning an empty list to a variable
love_maybe_lines_stripped = []

#looping in the already provided list and for everysingle index appending it to a new variable, then stripping the empty space for every single index
for i in love_maybe_lines:
  love_maybe_lines_stripped.append(i.strip())

#new variable which holds all the cleaned poem by using .join() on new lines
love_maybe_full = '\n'.join(love_maybe_lines_stripped)

#printing
print(love_maybe_full)