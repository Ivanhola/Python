#! python 3

import pyperclip
import re


# Create a regex for phone numbers

phoneRegex = re.compile(r""" 
# 415-444-0000, 555-000, (415) 555-0000, 555-000 ext 12345, ext.12345, x12345
(
((\d\d\d)|(\(\d\d\d\)))?                # Area code (optional)
(\s|-)                # first separator
\d\d\d                # first 3 digits
-                # seperator
\d\d\d\d                # last 4 digits
(((ext(\.)?\s)|x)              # extension word part(optional)
(\d{2,5}))?               #extension number-part(optional)
)

""", re.VERBOSE)
# create regex for email addresses

emailRegex = re.compile(r"""
#some.+_thing@something.com

[a-zA-Z0-9_.+]+         #name part
@                       #@ symbol
[a-zA-Z0-9_.+]+         #domain name part


""", re.VERBOSE)

# Get the text off the clipboard
text = pyperclip.paste()
# extract the email /phone from this text

extractedPhoneNums = phoneRegex.findall(text) #returns a list of found regex strings (phone numbers)
extractedEmail = emailRegex.findall(text) #returns a list of found


allPhoneNumbers = []

for phoneNumber in extractedPhoneNums:
    
    allPhoneNumbers.append(phoneNumber[0]) #This gets the first tuple of the extractedPhoneNums group. Which returns an entire phone number

#print(allPhoneNumbers)
#print(extractedPhoneNums)
#print(extractedEmail)


# Copy the extracted email/phone to the clipboard

results = "\n".join(allPhoneNumbers) + "\n"+ "\n".join(extractedEmail)
pyperclip.copy(results)