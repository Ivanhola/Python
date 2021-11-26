import os
import pandas

fileLocation = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__))) #this gets the current location reliably

csvFile1 = pandas.read_csv(os.path.join(fileLocation, "supermarkets.csv"))
jsonFile1 = pandas.read_json(os.path.join(fileLocation, "supermarkets.json"))
excelFile1 = pandas.read_excel(os.path.join(fileLocation, "supermarkets.xlsx"), sheet_name=0)
txtFile1 = pandas.read_csv(os.path.join(fileLocation, "supermarkets-commas.txt"))
#Text file has semi colons as seperators, need to add an argument to be able to read it
txtFile2 = pandas.read_csv(os.path.join(fileLocation, "supermarkets-semi-colons.txt"), sep=";")


print("Loading the CSV File: ")
print(csvFile1)
print()
print()
print("Loading the JSON File: ")
print(jsonFile1)
print()
print()
print("Loading the Excel File: ")
print(excelFile1)
print()
print()
print("Loading the TXT File: ")
print(txtFile1)
print()
print()
print("Loading the TXT File: ")
print(txtFile2)