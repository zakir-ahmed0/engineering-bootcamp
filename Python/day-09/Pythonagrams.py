#codecademy project for dictionaries
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 2, 2, 2, 1, 3, 3, 3, 1, 4, 3, 1, 2, 3, 1, 3, 5, 1, 1, 1, 2, 3, 3, 4, 3, 5]

letter_to_points = {key:value for key, value in zip(letters, points) }
#print(letter_to_points)

def score_word(word):
  point_total = 0
  for i in word:
    point_total += letter_to_points.get(i,0)
  return point_total

brownie_points = score_word("BROWNIE")
#print(brownie_points)

#dictionary that contains the names of each player along with the words he or she has played
player_to_words = {"player1":["BLUE","TENNIS","EXIT"],"wordNerd":["EARTH","EYES","MACHINE"],"Lexi Con":["ERASER","BELLY","HUSKY"],"Prof Reader":["ZAP","COMA","PERIOD"]}

#creating a new dictionary that will eventually hold each player's point total thus far
players_to_points = {}

#populating the players_to_points dictionary
for player,words in player_to_words.items():
  player_points = 0
  for eachWord in words:
    player_points += score_word(eachWord)
  players_to_points[player] = player_points

#printing the players_to_points dictionary to make sure it's right
print(players_to_points)

#populating the players_to_points dictionary
for player,words in player_to_words.items():
  player_points = 0
  for eachWord in words:
    player_points += score_word(eachWord)
  players_to_points[player] = player_points

#printing the players_to_points dictionary to make sure it's right
print(players_to_points)

#adds a word to a player's played words list
def play_word(player,word):
  player_to_words.get(player).append(word)

#turning the above nested for loops code into a function
def update_point_totals():
  for player,words in player_to_words.items():
    player_points = 0
    for eachWord in words:
      player_points += score_word(eachWord)
    players_to_points[player] = player_points