#Continuation of the off-platform project
#Task 4 , is brute forcing the offset to find exactly which offset is the working one without knowing the actual offset for the encoded message

alphabet = "abcdefghijklmnopqrstuvwxyz"
brute_force_message = "vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl tl hulhexmx. px'ee atox mh kxteer lmxi ni hnk ztfx by px ptgm mh dxxi hnk fxlltzxl ltyx."

def caesar_decode(message,offset):
    decoded_message = ""

    for character in message:
        if character in alphabet:
            character_value = alphabet.find(character)
            decoded_message += alphabet[(character_value + offset) % 26 ]
        else:
            decoded_message += character

    return decoded_message



for i in range(1, 26):
  print("Offset: {}".format(i))
  print("\t {}".format(caesar_decode(brute_force_message, i)))

#after executing and bruteforcing the cypher texts we found the offset to be "7" which proves our program is working correctly!