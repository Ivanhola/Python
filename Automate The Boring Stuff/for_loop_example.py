#Prints the print class 5 times starting from 0 
print("My name is")
for i in range(5):
    print("Jimmy Five times " + str(i))

#Adds the sum of each number 100 times starting from 0 
total = 0

# Range function can be called with 2, example: for num in range(50, 101): starts at 50 ends at 101, upto 100 not including 101
# Range function can also use 3 arguments called the step argument, which dictates how much it jumps over each iteration. for num in range(50 , 101, 2): would increase in 2s
for num in range(101):
    total = total + num

print(total)