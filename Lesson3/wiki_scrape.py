from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/List_of_most-followed_Instagram_accounts"

connection = urlopen(url)
html = connection.read()

page = BeautifulSoup(html, "html.parser")

table = page.find("table")
content = table.find("tbody")
data = content.find_all("tr")
info_list = []

for i in range(len(data)):
    entry = [
        e.text.replace("\n", "").replace("\xa0", "")
         for e in data[i].find_all("td") if e.text != "\n"
         ]
    
    if(len(entry) != 0):
        info_list.append(entry)

for s in info_list:
    print(s)

connection.close()
