#Dictionaries are like hashmaps, has a key and a value 
myCat = {"size": "fat", "color": "gray", "disposition": "loud"}

print(myCat["size"])

print("My cat has " + myCat["color"] + " fur.")

#Keys and values can be any type of variable 
example = {12345: "The red car", 23: "The white car"}
print(example[12345])

#Unlike lists, the order doesnt matter, take this list for example that will return false
print([1, 2, 3] == [3, 2, 1])

anotherExample = {"name": "zophie", "species": "cat", "age": 8}

exampleAnother = {"species": "cat", "age": 8, "name": "zophie"}
# Dictionaries will equal to each other if values are the same regardless of order
print(anotherExample == exampleAnother)

print()
#Lets return a list value of the different methods in these dictionaries
print("The keys for anotherExample are: " + str(list(anotherExample.keys())))
print("The values for anotherExample are: " + str(list(anotherExample.values())))
print("The items for anotherExample are: "+ str(list(anotherExample.items())))
print()
# For loop example 

#Assigns the keys to the variable
for k in anotherExample.keys():
    print(k)
print()
#Assigns the value to the variable v
for v in anotherExample.values():
    print(v)
print()
# You can assign the keys and values to both variables
for k, v in anotherExample.items():
    print(k,v)

print()
#Will print out the last assigned value in the for loop age 8
print(k, v)
print()
#Or you can assign it to a single variable

for i in anotherExample.items():
    print(i)

print()

#Get method allows us to retrieve a value without causing an error if the key doesnt exist

#If the key age doesnt exist, fall back to 0 being the value
print(anotherExample.get("age", 0))
#Since there is no color key, returns blank
print(anotherExample.get("color", ""))



#The setdefault method will allow us to set a key value pair if the value isnt there aka the get value doesnt return a value
anotherExample.setdefault("color", "black")
print(anotherExample)
#This does nothing because color already exists
anotherExample.setdefault("color", "orange")