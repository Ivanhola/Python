import requests
from requests.models import HTTPError

#Returns a response object
responseObject = requests.get("https://automatetheboringstuff.com/files/rj.txt")
print(responseObject.status_code)

responseObject.raise_for_status()

print(responseObject.text[:200])

#Will throw exemption for this bad request example
try:
    badRes = requests.get("http://automatetheboringstuff.com/dsad")
    badRes.raise_for_status()
except HTTPError:
    print("error")

#In order to save the file into a txt, you will need to open it in a write binary mode in order to maintain the unicode coding of this text
playFile = open("RomeoAndJuliet.txt", "wb")
for chunk in responseObject.iter_content(100000):
    #print(type(chunk))
    #print(type(responseObject.iter_content()))
    playFile.write(chunk)

playFile.close()