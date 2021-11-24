import os
import pandas

fileLocation = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__))) #this gets the current location reliably

csvFile1 = pandas.read_csv(os.path.join(fileLocation, "supermarkets.csv"))

print(csvFile1)