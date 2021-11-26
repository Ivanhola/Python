from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

s = Service("C:\\Program Files\\Google\\Chrome\\Application\\Chromedriver.exe")
browser = webdriver.Chrome(service=s)
delay = 3
browser.get("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
browser.maximize_window()
try: 
        myElem = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.XPATH , '//*[@id="buttons"]/ytd-button-renderer')))
       
        myElem.click()
        
except TimeoutException:
    print("Loading took to long")

#Input search 
try: 
        myElem = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.CSS_SELECTOR , '#identifierId')))
       
        myElem.send_keys("testing@gmail.com")
        
        
except TimeoutException:
    print("Loading took to long")

browser.quit()   