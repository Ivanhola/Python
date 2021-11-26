listOfItems = [10, 20, 30]
listOfItems[0] = "Hello" #Sets the 0 index to Hello
print(listOfItems)

listOfItems[1:3] = ["cat", "Dog", "Mouse"] #YOu can get multiple items from a list using slice, the n ew lists item start at the first index, and go up to the second, doesnt include seconds index
print(listOfItems)

listOfItems = ["cat", "bat", "rat", "elephant"]
print(listOfItems[:2])

del listOfItems[2] #deletes the 2 index RAT
print(listOfItems)

print("howdy" in ["hello", "hi", "howdy", "hey"]) #prints true because howdy is found IN the list
print("howdy" in ["hello", "hi", "hiya", "hey"]) #checks if howdy is in list, returns false
print("howdy" not in ["hello", "hi", "howdy", "hey"]) #opposite of first will return false because howdy is in it
print("howdy" not in ["hello", "hi", "hiya", "hey"]) #opposite of 2nd example