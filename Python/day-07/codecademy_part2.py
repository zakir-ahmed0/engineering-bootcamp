#Continuation of the off-platform project

#So , writing a function to autonomize the caesar cypher with just 2 arguments now which are message and offset...
#Task 3

alphabet = "abcdefghijklmnopqrstuvwxyz"

def caesar_decode(message,offset):
    decoded_message = ""

    for character in message:
        if character in alphabet:
            character_value = alphabet.find(character)
            decoded_message += alphabet[(character_value + offset) % 26 ]
        else:
            decoded_message += character

    return decoded_message

message1 = "jxu evviuj veh jxu iusedt cuiiqwu yi vekhjuud"
message2 = "bqdradyuzs ygxfubxq omqemd oubtqde fa oapq kagd yqeemsqe ue qhqz yadq eqogdq!"
print(caesar_decode(message4,14))

def caesar_encode(message, offset):
  encoded_message = ""

  for character in message:
    if character in alphabet:
      character_value = alphabet.find(character)
      encoded_message += alphabet[(character_value - offset) % 26]
    else:
      encoded_message += character

  return encoded_message

message3 = "hey this is going to be an encoded message for caesar let's see how it works"
print(caesar_encode(message3,14))