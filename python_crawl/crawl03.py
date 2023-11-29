#pip install requests
#pip install bs4

import requests
from bs4 import BeautifulSoup

url = "https://www.malware-traffic-analysis.net/2023/index.html"
headers = {
        'User-Agent': 'Mozilla/5.0',
        'Content-Type': 'text/html; charset=utf-8'
}
req = requests.get(url, headers=headers)
soup = BeautifulSoup(req.text, "lxml")

tags = soup.select('#main_content > div.content > ul > li > a.main_menu')
print(tags)
for tag in tags:
    print(tag.text)
    print(f"https://www.malware-traffic-analysis.net/2023/{tag['href']}")