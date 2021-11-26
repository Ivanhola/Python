name = "Ivan"
age = 3000 #just an int variable that can be used to replace the userInputAge

print("What is your name?")
userInputName = input()

print("What is your age?")
userInputAge = input()

if userInputName == name:
    print("Hi Ivan")
elif int(userInputAge) < 12: #Convert a string into an int with int()
    print("You are not Ivan, kiddo.")
elif int(userInputAge) > 2000:
    print("Unlike you, Ivan is not an undead zombie")
elif int(userInputAge) > 100:
    print("You are not Ivan gramps")