#OFF PLATFORM PROJECT FROM CODECADEMY REGARDING CYPHER TEXTS AND CRYPTOGRAPHY



#TASK 1 , GIVEN A CRYPTO CYPHER MESSAGE CAESAR STYLE CYPHER DECODE IT

alphabet = "abcdefghijklmnopqrstuvwxyz"
message = "xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!"
translated_text = ""

for character in message:
    if character in alphabet:
        character_value = alphabet.find(character)
        translated_text += alphabet[(character_value + 10) % 26]
    else:
        translated_text += character

#print(translated_text)
#successfully works


#Task 2 , Is to send a message from my side encrypted so i am sending a message this time

alphabet1 = "abcdefghijklmnopqrstuvwxyz"
message2 = "hey reciever this is a plain text which i am going to convert into a caesar style cypher message"
translated_text2 = ""

for character in message2:
    if character in alphabet1:
        character_value = alphabet1.find(character)
        translated_text2 += alphabet[(character_value - 10) % 26]
    else:
        translated_text2 += character

#print(translated_text2)
#successfully works