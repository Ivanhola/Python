for i in range(4):
    print(i)

supplies = ["pens", "staplers", "flame-throwers", "bin"]

#Takes the length of the supplies to go through it all
for i in range(len(supplies)):
    print("Index " + str(i) + " in supplies is : " + supplies[i])

#Variable swap example, you can assign variables to different things
cat = ["fat", "white", "loud"]
size, color, disposition = cat
print(size)

a = "AAA"
b = "BBB"

a, b = b, a
print("a is : " + a)
print("b is : " + b)