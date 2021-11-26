import numpy
#Can have 1 2 or 3 dimensions

n = numpy.arange(27)
print(n)
print()
#Convert into a 2 dimensional array
n2 = n.reshape(3,9) #3 times 9 is 27

print(n2)
print()
#Convert into 3 dimensional array
n3 = n.reshape(3,3,3)

print(n3)

#You can convert a regular python list into a numpy array using numpy.asarrange