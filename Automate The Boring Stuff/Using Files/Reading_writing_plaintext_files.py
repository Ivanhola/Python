import os

fileLocation = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__))) #this gets the current location reliably
helloFile = open(os.path.join(fileLocation, "hello.txt"))

content = helloFile.read()
#contentList = helloFile.readlines() #can only read() once
#print(contentList)
print(content)

helloFile.close()

helloFile2 = open(os.path.join(fileLocation, "hello2.txt") , "w")
helloFile2.write("Hello!!!!!!!!!!!!!")
helloFile2.write("Hello!!!!!!!!!!!!!")
helloFile2.close()

#You can save lists and dictionary data into a file using the shelve module. 
import shelve

#this will save the cats list into a file "mydata"
shelfFile = shelve.open(os.path.join(fileLocation, "mydata"))
shelfFile["cats"] = ["Sophie", "zoe", "luna", "lucy"]
shelfFile["fruits"] = ["apples", "peaches", "pears", "kiwi"]
shelfFile.close()

#opening and reading the list that we saved earlier
shelfFile = shelve.open(os.path.join(fileLocation, "mydata"))

print(str(shelfFile["cats"]))
print(str(shelfFile["fruits"]))
