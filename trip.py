from playwright.sync_api import sync_playwright
import pandas as pd

url = 'https://www.tripadvisor.com.au/Attractions-g255060-Activities-oa0-Sydney_New_South_Wales.html'

with sync_playwright() as p:
    browser = p.chromium.launch(executable_path='/Applications/Brave Browser.app/Contents/MacOS/Brave Browser', headless=False)
    page = browser.new_page()
    page.goto(url, timeout=30000)
    cards = page.locator('[class="GTuVU XJlaI"]').all()

    data = []
    for card in cards: 
        info = {}
        info['Name'] = card.locator('[class="XfVdV o AIbhI"]').text_content()
        info['Description'] = card.locator('[class="alPVI eNNhq PgLKC tnGGX yzLvM"]').first.text_content()
        info['Number Reviews'] = card.locator('[class="biGQs _P pZUbB osNWb"]').text_content()

        data.append(info)


    df = pd.DataFrame(data)
    df.to_excel('./trip-xlsx/trip.xlsx')

    browser.close()