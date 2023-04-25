import requests,bs4
url = r"https://finance.yahoo.co.jp/quote/8267.T"
open=requests.get(url)
soup=bs4.BeautifulSoup(open.content,"html.parser")
price=soup.select('._1mwPgJ2S > span:nth-child(1) > span:nth-child(1)')
print(price[0].contents[0])