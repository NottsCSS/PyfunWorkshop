from urllib.parse import quote
from urllib.request import urlopen
from bs4 import BeautifulSoup

textToSearch = 'hello world'
query = quote(textToSearch)
url = "https://www.youtube.com/results?search_query=" + query
response = urlopen(url)
html = response.read()
soup = BeautifulSoup(html, features="html.parser")
for vid in soup.findAll(attrs={'class': 'yt-uix-tile-link'}):
    print(vid)
    if not vid['href'].startswith("https://googleads.g.doubleclick.net/"):
        print('https://www.youtube.com' + vid['href'])
