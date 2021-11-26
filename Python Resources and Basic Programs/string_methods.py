#Strings are imutable
spam = "Hello World!"

print(spam.upper())

print(spam)

print(spam.lower())

print(spam.startswith("H"))
print(spam.endswith("!"))

#join methods combines a list of strings into a single string by separating it with whatever string you pass

print("|".join(["cats", "rats", "bats"]))

#split method returns a list of strings from a single string

print("My name is simon".split())
print("My name is simon".split("m"))

#Replace method can replace text in a string
repExample = "Hello there!"
print(repExample.replace("Hello", "Goodbye!"))

import pyperclip
pyperclip.copy("Hello!!!!")

print(pyperclip.paste())

#Look up %s to use string formatting. Excample "Hello %s when are you coming to %s ? its at %s time" % (variable1, variable2, variable3) you can make things more readable.