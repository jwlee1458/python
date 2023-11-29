import feedparser
import pandas as pd
from datetime import datetime
import os
import zipfile
import ftplib
from dotenv import load_dotenv, find_dotenv

dotenv_path = find_dotenv(filename=".env", raise_error_if_not_found=True)
load_dotenv(dotenv_path)
FTP_HOST = os.getenv("FTP_HOST")
FTP_USER = os.getenv("FTP_USER")
FTP_PASS = os.getenv("FTP_PASS")

now = datetime.now().strftime("%Y-%m-%d")
dir_path = os.path.join("python_ftp", f"{now}_rss")
os.mkdir(dir_path)

def rss_crawl():
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

        df.to_excel(f'{dir_path}\\{index+1}_result.xlsx', index=False)
    
def zip_files():
    #zipfile 수행
    zip_file = zipfile.ZipFile(os.path.join("python_ftp", f"{now}.zip"), "w")

    for root, dirs, files in os.walk(dir_path):
        for file in files:
            file_path = os.path.join(root, file)
            relative_path = os.path.relpath(file_path, dir_path)
            zip_file.write(file_path, os.path.join(f"{now}_rss", relative_path))

    zip_file.close()

def ftp_sender():
    #ftp 전송
    ftp_host = FTP_HOST
    ftp_user = FTP_USER
    ftp_pass = FTP_PASS

    ftp = ftplib.FTP(ftp_host)
    ftp.login(ftp_user, ftp_pass)

    with open(os.path.join("python_ftp", f"{now}.zip"), "rb") as f:
        ftp.storbinary(f"STOR {now}.zip",f)

    print(f"현재 디렉터리 위치: {ftp.pwd()}")
    print(f"현재 디렉터리 정보: {ftp.dir()}")

if __name__ == '__main__':
    rss_crawl()
    zip_files()
    ftp_sender()