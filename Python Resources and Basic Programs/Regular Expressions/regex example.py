import re

#Looking for a digit in the raw string with \d
phoneNumRegex = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d")

matchedObject = phoneNumRegex.search("Call me at 213-512-4000 tomorrow or at 212-231-4122")

#group method returns string of found regex
print(matchedObject.group())

print(matchedObject)

#Returns a list of strings with the findall method
print(phoneNumRegex.findall("Call me at 213-512-4000 tomorrow or at 212-231-4122"))

