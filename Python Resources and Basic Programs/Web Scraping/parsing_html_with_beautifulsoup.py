import bs4
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
    'referer': 'https://google.com',
    }

def getAmazonPrice(amazonURL):
    res = requests.get(amazonURL, headers=headers)
    res.raise_for_status()


    soup = bs4.BeautifulSoup(res.text, "html.parser")

    elementTitle = soup.select("#productTitle")
    elementPrice = soup.select("#usedPrice")

    scrapedText = "the price for " + elementTitle[0].text.strip() + " is " + elementPrice[0].text.strip()
    return scrapedText

price = getAmazonPrice("https://www.amazon.com/Automate-Boring-Stuff-Python-Programming-dp-1593275994/dp/1593275994/")
print(price)