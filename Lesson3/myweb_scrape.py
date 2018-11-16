from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://talk-93dae.firebaseapp.com/"

connection = urlopen(url)
html = connection.read()

page = BeautifulSoup(html, "html.parser")

content = page.find("h1")

print(content.text)

connection.close()