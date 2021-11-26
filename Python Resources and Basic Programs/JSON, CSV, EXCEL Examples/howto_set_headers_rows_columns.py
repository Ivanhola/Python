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


#Retrieving specific Data from this DataFrame, Index 1 through 3, City to Country
print(csvFile2.loc["1":"3", "City":"Country"])
print()

#More common way to get data, by filtering through rows and columns using iloc Row:Column position based
print(csvFile2.iloc[0:4,0:3])

#Deleting Rows 1 is columns, 0 is rows
print(csvFile2.drop("City",1))

#Can delete using positions as well
print(csvFile2.drop(csvFile2.columns[0:3], 1)) #Colmuns
print(csvFile2.drop(csvFile2.index[0:3], 0)) #Rows