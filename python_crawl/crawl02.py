#pip install requests
#pip install bs4

import requests
from bs4 import BeautifulSoup

url = "http://www.boannews.com/"
headers = {
        'User-Agent': 'Mozilla/5.0',
        'Content-Type': 'text/html; charset=utf-8'
}
req = requests.get(url, headers=headers)
soup = BeautifulSoup(req.text, "lxml")

tags = soup.select('#headline2 > ul > li > p')
print(tags)
for tag in tags:
    print(tag.text)