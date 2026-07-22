#splitting strings program
#given a string with all the author names saved in a variable called authors
authors = "Audre Lorde,Gabriela Mistral,Jean Toomer,An Qi,Walt Whitman,Shel Silverstein,Carmen Boullosa,Kamala Suraiyya,Langston Hughes,Adrienne Rich,Nikki Giovanni"

#arranging the list by splitting each author from the ',' by using split method
author_names = authors.split(',')
print(author_names)

#now for this specific problem we only need the last names of the authors , so we use a empty list variable with a for loop to loop through
#the sorted author_names variable which contains the correct formated author data , loop through it then append the looped indices to the empty list
#then splitting it again with index -1 which will select the last name of the author and adding it back to our empty list
author_last_names = []
for i in author_names:
  author_last_names.append(i.split()[-1])

print(author_last_names)