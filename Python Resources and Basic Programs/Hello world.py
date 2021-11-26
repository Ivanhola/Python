#basic hello world stuff
print('Hello world!')

print('What is your name? ') # Name to ask
myName = input()
print('It is nice to meet you ' + myName)
print('The length of your name is: ')
print(len(myName)) #Takes string value of the variable myName

print('What is your age?') #Ask for their age
myAge = input()
print('Hi ' + myName + ' You will be ' + str(int(myAge) + 1 ) + ' in a year.' ) #converts an integer value into a string with the str function