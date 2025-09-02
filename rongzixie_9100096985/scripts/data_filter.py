import numpy as np
import pandas as pd
from bs4 import BeautifulSoup

print("reading data from html")
with open("../data/raw_data/web_data.html","r", encoding="utf-8") as f:
    soup=BeautifulSoup(f,"html.parser")
cond1=["MarketCard-symbol","MarketCard-stockPosition","MarketCard-changesPct"]
cond2=["LatestNews-timestamp","LatestNews-headline","link"]
output=[]

print("filtering market data")
for cond in cond1:
    items=soup.find_all("span",class_=cond)
    items=[item.get_text(strip=True) for item in items]
    output.append(items)
print(output)
output=np.array(output).T

print("storing market data")
df_1=pd.DataFrame(output, columns=["symbol","stockPosition","changesPct"])
df_1.to_csv("../data/processed_data/market_data.csv")

print("filtering news data")
times=[time.get_text(strip=True) for time in soup.find_all("time",class_=cond2[0])]
infos=soup.find_all("a",class_=cond2[1])
links=[link.get("href") for link in infos]
titles=[title.get("title") for title in infos]

print("storing news_data")
df_2=pd.DataFrame(np.array([titles,times,links]).T,columns=["titles","timestamp","link"])
df_2.to_csv("../data/processed_data/news_data.csv")
print("success!!!")
