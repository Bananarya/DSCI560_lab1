from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

url = "https://www.cnbc.com/world/?region=world"

options = Options()
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)

driver.get(url)
while True:
    try:
        view_more_btn = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.LatestNews-button"))
        )
        view_more_btn.click()
        time.sleep(2)
    except:
        break

html = driver.page_source
soup = BeautifulSoup(html, "html.parser")
market_banner=soup.find_all("section",class_="MarketsBanner-container")
latest_news=soup.find_all("div", class_="LatestNews-isHomePage LatestNews-isIntlHomepage")
myhtml="\n".join(item.prettify() for item in market_banner)
myhtml2="\n".join(item.prettify() for item in latest_news)
with open("../data/raw_data/web_data.html","w",encoding="utf-8") as f:
    f.write(myhtml)
    f.write("\n")
    f.write(myhtml2)
