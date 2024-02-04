from bs4 import BeautifulSoup
from selenium import webdriver

stock = input('Choose a stock: ')
stock = stock.upper()

url = f'https://finviz.com/quote.ashx?t={stock}&p=d'

brave_path = '/Applications/Brave Browser.app/Contents/MacOS/Brave Browser'
option = webdriver.ChromeOptions()
option.binary_location = brave_path
# option.add_argument('--headless')

driver = webdriver.Chrome(options=option)
driver.get(url)

page = driver.page_source

driver.quit()

soup = BeautifulSoup(page, 'html.parser') 

price = soup.find('strong', class_='quote-price_wrapper_price').text

print(f'The current price of {stock} is ${price} per share')
