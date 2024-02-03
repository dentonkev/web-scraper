import time
from bs4 import BeautifulSoup
# import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://finviz.com/quote.ashx?t=NKE&p=d'

brave_path = '/Applications/Brave Browser.app/Contents/MacOS/Brave Browser'
brave_options = webdriver.ChromeOptions()
brave_options.binary_location = brave_path


driver = webdriver.Chrome(options=brave_options)
driver.get(url)

page = driver.page_source

driver.quit()

# response = requests.get(url)
soup = BeautifulSoup(page, 'html.parser') 

print(soup)

price = soup.find('strong', class_='quote-price_wrapper_price')

print(price)

