from flask import Flask, render_template, request, send_file
import feedparser
import openpyxl
import pandas as pd
import time
from googletrans import Translator
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/rss', methods=['GET', 'POST'])
def rss():
    #rss 정보 가져오기
    rss_url = request.form['rss_url']
    feed = feedparser.parse(rss_url)
    titles = []
    links = []
    descriptions = []
    authors = []

    for entry in feed.entries:
        titles.append(entry.title)
        links.append(entry.link)
        descriptions.append(entry.description)

    data = {'Title':titles, 'Link':links, 'Description':descriptions}
    df = pd.DataFrame(data)

    df.to_excel(os.path.join("python_flask_rss", 'rss_result.xlsx'), index=False)

    #번역 시작
    workbook = openpyxl.load_workbook(os.path.join("python_flask_rss", "rss_result.xlsx"))
    sheet = workbook.active

    #구글 번역
    translator = Translator()
    for row in sheet.iter_rows():
        for cell in row:
            translated_text = translator.translate(cell.value, dest='en').text
            cell.value = translated_text
        
        time.sleep(0.5)
        
    workbook.save(os.path.join("python_flask_rss", "transrated_rss.xlsx"))

    return render_template('rss.html', feed=feed)


@app.route('/download_report')
def download_report():
    return send_file(os.path.join('transrated_rss.xlsx'), as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)