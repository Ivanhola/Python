#Using Pandas Module will help reading data files like Excel, and others
import pandas

#Creatng a simple table
df1 = pandas.DataFrame([[1,2,3],[4,5,6],[7,8,9]])
print(df1)
df1.columns=["Price", "age", "value"]
print(df1)
#Probably don't want to mess with the index naming
df1.index=["First Row", "Second Row", "Third Row"]
print(df1)

#Works with dictionaries as well
df2 = pandas.DataFrame([{"Name":"Ivan", "Last Name":"Doe"},{"Name":"Jack","Last Name":"Tree"}])
print(df2)
