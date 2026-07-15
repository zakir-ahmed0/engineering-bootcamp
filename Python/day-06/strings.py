#strings module review
#username_generator

#defining a function and including 2 arguments
def username_generator(first_name,last_name):
  #condition if length of first argument is less than 3 , then we created a variable called user_name and assigning it to first_name argument , else user_name will contain a slice of first 3 characters
  if len(first_name) < 3:
    user_name = first_name
  else:
    user_name = first_name[0:3]
  #same as the first name condition but this time we're adding last_name argument to user_name variable if its less than 4, else contains username with first 4 characters of the string slice . then just returning the user_name variable
  if len(last_name) < 4:
    user_name += last_name
  else:
    user_name += last_name[0:4]
  return user_name

print(username_generator('abhi','shek'))

#now for the password generator

#defining the function for the password generator
def password_generator(user_name):
  #empty variable with password stirng
  password = ''
  #for loop which will go through the user_name argument , in the range from 0 to length of the username we provide it , then shift the username one time to the right and append it to the empty password string
  for i in range(0, len(user_name)):
    password += user_name[i-1]
  return password

print(password_generator('abhshek'))