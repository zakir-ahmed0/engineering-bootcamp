#strings module review finale

#given a list of random strings jumbled , just cleaning this string with different built in python methods step by step
highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"

#splitting the string first of ','
highlighted_poems_list = highlighted_poems.split(',')

#creating a new empty list and appending the stripped indexes of the string from the loop
highlighted_poems_stripped = []

for i in highlighted_poems_list:
  highlighted_poems_stripped.append(i.strip())

#creating a new empty list and appending the split indexes of the string from the loop , spltting from : this time
highlighted_poems_details = []

for i in highlighted_poems_stripped:
  highlighted_poems_details.append(i.split(':'))

#creating 3 new empty list variables so we can save the indexes of the strings which are in order alreday containing titles,poets,dates at their respective indexes
titles = []
poets = []
dates = []

for poem in highlighted_poems_details:
  titles.append(poem[0])
  poets.append(poem[1])
  dates.append(poem[2])

#looping through the current list again to format it better and cleaner
for i in range(0, len(highlighted_poems_details)):
  print('The poem {} was published by {} in {}'.format(titles[i], poets[i], dates[i])) 
