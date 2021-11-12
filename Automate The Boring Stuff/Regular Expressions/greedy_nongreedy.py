import re

#This group can appear 0 or 1 times in this group using the question mark. The star will match it 0 or more times any number of times the + matches 1 or more
batRegex = re.compile(r"Bat(wo)?man")

matchedObject = batRegex.search("The adventures of Batman")
print(matchedObject.group())

matchedObject = batRegex.search("The adventures of Batwoman")

print(matchedObject.group())

matchedObject = batRegex.search("The adventures of Batwowowoman")
print(matchedObject == None)

#Phone number example

phoneRegex = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d")
phoneMO = phoneRegex.search("My phone number is 422-231-2312")

print(phoneMO.group())

#Regular expression with group
 
phoneRegex = re.compile(r"(\d\d\d-)?\d\d\d-\d\d\d\d")
print(phoneRegex.search("My phone number is 422-231-2312"))
print(phoneRegex.search("My phone number is 231-2312"))