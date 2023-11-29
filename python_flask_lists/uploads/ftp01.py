import ftplib
import time
import os
from dotenv import load_dotenv, find_dotenv

dotenv_path = find_dotenv(filename=".env", raise_error_if_not_found=True)
load_dotenv(dotenv_path)
FTP_HOST = os.getenv("FTP_HOST")
FTP_USER = os.getenv("FTP_USER")
FTP_PASS = os.getenv("FTP_PASS")

ftp_host = FTP_HOST
ftp_user = FTP_USER
ftp_pass = FTP_PASS

ftp = ftplib.FTP(ftp_host)
ftp.login(ftp_user, ftp_pass)

with open(os.path.join("python_rss", "1_result.xlsx"), "rb") as f:
    ftp.storbinary(f"STOR 1_result.xlsx",f)

print(f"현재 디렉터리 위치: {ftp.pwd()}")
print(f"현재 디렉터리 정보: {ftp.dir()}")