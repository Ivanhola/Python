import os
import pandas

print("File path is: "+ os.getcwd())
print(os.listdir())
csvFile1 = pandas.read_csv("supermarkets.csv")

print(csvFile1)