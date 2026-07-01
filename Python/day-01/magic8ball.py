import random

name = "magician"
question = "is earth flat?"

randomNumber = random.randint(1,9)

if randomNumber == 1:
  eightBall = "Yes - definitely"
elif randomNumber == 2:
  eightBall = "It is decidedly so"
elif randomNumber == 3:
  eightBall = "Without a doubt"
elif randomNumber == 4:
  eightBall = "Reply hazy, try again"
elif randomNumber == 5:
  eightBall = "Ask again later"
elif randomNumber == 6:
  eightBall = "Better not tell you now"
elif randomNumber == 7:
  eightBall = "My sources say no"
elif randomNumber == 8:
  eightBall = "Outlook not so good"
elif randomNumber == 9:
  eightBall = "Very doubtful"
else:
  eightBall = "Error"


if name == "":
    print("Question:", question)
else:
    print(f"{name} asks: {question}")

# Print the answer
print("Magic 8-Ball's answer:", eightBall)