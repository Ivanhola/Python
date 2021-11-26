spam = ["hello", "hi", "howdy", "hey"]

#index is a method used by the .
print(spam.index("hello"))

#adds to the list
spam = ["cat", "dog", "bat"]
spam.append("moose")
print(spam)

#inserts into the 1 index
spam = ["cat", "dog", "bat"]
spam.insert(1, "chicken")
print(spam)

#remove method
spam = ["cat", "dog", "bat" , "elephant"]
spam.remove("bat")
print(spam)

#This is different from the delete function which specifies the index

del spam[0]
print(spam)

#sort method does it in order
listOfNums = [2, 3, 6, 0, 9, 42]
listOfNums.sort()
print(listOfNums)

listOfNames = ["zebra", "animal", "dog"]
listOfNames.sort()
print(listOfNames)

#Methods are functions that are "called on" values
#The index() list method returns the index of an item in a list
#The append() method adds a value to the END of a list
#The insert() list method adds a value to any index specified in the list
#The remove() list method removes an item, specified by the value from the lsit
#sort() list method sorts the items in a list
#can use reverse=True to reverse the list order
#Sorting happens in ASCII-betical order, meaning that capital Letters will be sorted first, can be bypassed by making all strings lowercase with key=str.lower