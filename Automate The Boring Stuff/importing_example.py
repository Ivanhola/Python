import sys

print("Hello")
#sys.exit()
#print("Goodbye") #This wont execute

import pyperclip
pyperclip.copy("Hello World")
print(pyperclip.paste())