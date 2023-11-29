#pip install requests
#pip install bs4

import requests
from bs4 import BeautifulSoup

url = "https://sports.news.naver.com/news?oid=139&aid=0002168397"
headers = {
    'User-Agent' : 'Mozilla/5.0',
    'Content-Type': 'text/html; charset-utf-8'
}
req = requests.get(url, headers=headers)

soup = BeautifulSoup(req.text, "lxml")

links = soup.find_all('a')
for link in links:
    if 'href' in link.attrs:
        href = link["href"]
        print(f"{link.text} 링크: {href}")