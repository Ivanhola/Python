import pprint
#Dictionary example
cat = {"name": "Zoey", "age": 9, "Color": "white"}

#List example
allCats = []
allCats.append({"name": "Zoey", "age": 9, "Color": "white"})
allCats.append({"name": "Pooka", "age": 5, "Color": "black"})
allCats.append({"name": "Doge", "age": 5, "Color": "gray"})

#This list of dictionaries is called a data structure.
print(allCats)

#Lets create a tic tac toe board using dictionaries

theBoard = {"top-L": " ", "top-M": " ", "top-R": " ", 
"mid-L": " ", "mid-M": " ", "mid-R": " ", 
"low-L": " ", "low-M": " ", "low-R": " ", }

pprint.pprint(theBoard)

theBoard["mid-M"] = "X"

pprint.pprint(theBoard)

#Function that prints out the different dictionary values, organized to represent current values
def printBoard(board):
    print(board["top-L"] + "|" + board["top-M"] + "|" + board["top-R"])
    print("-----")
    print(board["mid-L"] + "|" + board["mid-M"] + "|" + board["mid-R"])
    print("-----")
    print(board["low-L"] + "|" + board["low-M"] + "|" + board["low-R"])

printBoard(theBoard)

#Type allows you to see what type of variable is being used
print(type(theBoard))
print(type(theBoard["mid-M"]))