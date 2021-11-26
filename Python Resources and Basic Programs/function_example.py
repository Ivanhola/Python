#Defining the function
def hello():
    print("Howdy!")
    print("Howdy!!!")
    print("Howdy There !!!!")

hello()
hello()
hello()

#Passing in a string
def hi(name):
    print("Hello " + name)

hi("Alice")
hi("Bob")

#Functions with return values
# In java this would be written like: public int plusOne(int number){ return number + 1; } <- this is returning an integar
def plusOne(number):
    return number + 1

newNum = plusOne(4) #function is called here 
print(newNum)