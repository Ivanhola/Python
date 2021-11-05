spam = 0
while spam < 5:
    print("Hello world!")
    spam = spam + 1 #in java this would be like for loops, i + 1 adds 1 until reaches 5


# Need to ender 'your name'
name = ""
while name != "your name":
    print("Please type your name.")
    name = input()
    if name == "your name":
        break #useful to break the loop here

print("Thank you!")

# Example of continue 
spom = 0 
while spom < 5:
    spom = spom + 1
    if spom == 3:
        continue #if spom is 3, when a condition is met,  it will break out of the loop and jump back to the start of the while loop.
    print("Spom is " + str(spom))