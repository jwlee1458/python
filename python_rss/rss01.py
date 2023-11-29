#pip install feedparser
#pip install pandas

import feedparser
import pandas as pd
import os

url = "https://www.dailysecu.com/rss/allArticle.xml"

feed = feedparser.parse(url)

titles = []
links = []
descriptions = []
authors = []
pubDates = []

for entry in feed.entries:
    titles.append(entry.title)
    links.append(entry.link)
    descriptions.append(entry.description)
    authors.append(entry.author)
    pubDates.append(entry.published)

data = {'Title':titles, 'Link':links, 'Description':descriptions, 'Author':authors, 'Published':pubDates}
df = pd.DataFrame(data)

df.to_excel(os.path.join("python_rss", 'result.xlsx'), index=False)