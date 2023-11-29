import smtplib
from email.header import Header
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os
import time
from dotenv import load_dotenv, find_dotenv

dotenv_path = find_dotenv(filename=".env", raise_error_if_not_found=True)
load_dotenv(dotenv_path)
SECRET_ID = os.getenv("SECRET_ID")
SECRET_PASS = os.getenv("SECRET_PASS")
MY_EMAIL = os.getenv("MY_EMAIL")
YOUR_EMAIL = os.getenv("YOUR_EMAIL")

#메일 보내기 함수
def mail_sender(file_path, line):
    smtp = smtplib.SMTP('smtp.naver.com', 587)
    smtp.ehlo()
    smtp.starttls()

    smtp.login(SECRET_ID, SECRET_PASS)

    myemail = MY_EMAIL
    youremail = YOUR_EMAIL

    subject = f"{relative_path} 파일 탐지"
    message = f"{relative_path} : {line} 정보"
    msg = MIMEText(message.encode('utf-8'), _subtype='plain', _charset='utf-8')
    msg['Subject'] = Header(subject.encode('utf-8'), 'utf-8')
    msg['From'] = myemail
    msg['To'] = youremail
    smtp.sendmail(myemail,youremail,msg.as_string())
    smtp.quit()


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DIR_WATCH = os.path.join(BASE_DIR, "static")
previous_files = set(os.listdir(DIR_WATCH))
detected_files = os.path.join("python_mail", "detected_files.txt")

while True:
    time.sleep(1)
    print("모니터리중")
    current_files = set(os.listdir(DIR_WATCH))
    new_files = current_files - previous_files
    for filename in new_files:
        file_path = os.path.join(DIR_WATCH, filename)
        relative_path = os.path.relpath(file_path, BASE_DIR)
        with open(file_path,'r', encoding='utf-8') as f:
            lines = f.readlines()
            for line in lines:
                if line.startswith("#") or line.startswith("//"):
                    print(f"{relative_path} 주석 처리된 라인 {line}")
                    #파일 저장 기능 추가
                    with open(detected_files, 'a', encoding='utf-8') as wf:
                        wf.write(f"{relative_path} 주석 처리된 라인 {line}")
                    mail_sender(file_path, line)

    previous_files = current_files