from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/List_of_most-followed_Instagram_accounts"

connection = urlopen(url)
html = connection.read()

page = BeautifulSoup(html, "html.parser")

table = page.find("table")
content = table.find("tbody")
data = content.findAll("tr")
info_list = []

for i in range(len(data)):
    if i is 0:
        continue
    entry = tuple(
        [e.text.replace("\n", "").replace("\xa0", "")
         for e in data[i].findAll("td") if e.text != "\n"]
    )
    if(entry):
        info_list.append(entry)

# print(info_list)
for s in info_list:
    print(s)

connection.close()
