import pprint
#Lets make a program that counts how many letters are repeating in the message using dictionaries


message = "It was a bright cold day in april, and the clocks were striking thirteen"

#Empty dictionary 
count = {}

#Beacuse a string acts like a list of characters, we can iterate through it using a for loop and assigning each letter to a variable (character)
for character in message.upper(): 
    #if you dont have an I (because the message starts with I), set it to 0
    count.setdefault(character, 0)

    count[character] = count[character] + 1

#This loop finds if a character letter exists, if it doesnt, sets it to 0, and then adds 1 after. 
pprint.pprint(count)