from bs4 import BeautifulSoup
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options

url = "https://www.cnbc.com/world/?region=world"

options = Options()
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)

driver.get(url)
time.sleep(5)

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
