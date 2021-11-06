#Function
def divdeBy42(number):
    try: #tries returning
        return 42 / number
    except ZeroDivisionError: #if there is a zerodivisionerror it will do the following:
        print("You tried dividing by 0")

print(divdeBy42(2))
print(divdeBy42(22))
print(divdeBy42(0))
print(divdeBy42(1))
