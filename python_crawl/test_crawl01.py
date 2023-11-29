from bs4 import BeautifulSoup

html_content = """
<html>
    <body>
        <a href="https://www.example.com/page1">Link 1</a>
        <a href="https://www.example.com/page2">Link 2</a>
        <a href="https://www.example.com/page3">Link 3</a>
    </body>
</html>
"""

soup = BeautifulSoup(html_content, "lxml")

links = soup.find_all('a')
for link in links:
    if 'href' in link.attrs:
        href = link["href"]
        print(f"{link.text} 링크: {href}")

for link in links:
    href_value = link.get('href')
    print(f"{href_value}")