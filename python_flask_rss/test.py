import requests
from bs4 import BeautifulSoup
import re

url = "https://sports.news.naver.com/news?oid=139&aid=0002168397"

headers = {
        'User-Agent': 'Mozilla/5.0',
        'Content-Type': 'text/html; charset=utf-8'
}

req = requests.get(url, headers=headers)

results = re.search(r"[\w\.-]+@[\w\.-]+", req.text)[0]
print(results)

matches = re.findall(r"[\w\.-]+@[\w\.-]+", req.text)
print(set(matches))