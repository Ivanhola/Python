import os
import pandas

fileLocation = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__))) #this gets the current location reliably

csvFile1 = pandas.read_csv(os.path.join(fileLocation, "data.txt"))
print(csvFile1)
print()
print()
#Set Table header
csvFile1 = pandas.read_csv(os.path.join(fileLocation, "data.txt"), header=None)
print(csvFile1)

#Set Column names
csvFile1.columns = ["ID", "Address", "City", "Zip", "Country", "Name", "Employees"]
print()
print()
print(csvFile1)

#Get Index columns
print(csvFile1.set_index("ID")) #This doesnt save the index to the variable, so we must create a new one

csvFile2 = csvFile1.set_index("ID")
print()
print()
print("New File with index set: ")
print(csvFile2)