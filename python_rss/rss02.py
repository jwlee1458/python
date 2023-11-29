import feedparser
import pandas as pd
import os

with open(os.path.join("python_rss", 'rss.txt'), 'r') as file:
    rss_urls = file.readlines()

for index, url in enumerate(rss_urls):
    feed = feedparser.parse(url)
    titles = []
    links = []
    descriptions = []
    authors = []
    #pubDates = []

    for entry in feed.entries:
        titles.append(entry.title)
        links.append(entry.link)
        descriptions.append(entry.description)
        authors.append(entry.author)
        #pubDates.append(entry.published)

    data = {'Title':titles, 'Link':links, 'Description':descriptions, 'Author':authors}
    df = pd.DataFrame(data)

    df.to_excel(os.path.join("python_rss", f'{index+1}_result.xlsx'), index=False)