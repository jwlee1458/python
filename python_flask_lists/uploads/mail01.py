import smtplib
from email.header import Header
from email.mime.text import MIMEText
import os
from dotenv import load_dotenv, find_dotenv

dotenv_path = find_dotenv(filename=".env", raise_error_if_not_found=True)
load_dotenv(dotenv_path)
SECRET_ID = os.getenv("SECRET_ID")
SECRET_PASS = os.getenv("SECRET_PASS")
MY_EMAIL = os.getenv("MY_EMAIL")
YOUR_EMAIL = os.getenv("YOUR_EMAIL")

smtp = smtplib.SMTP('smtp.naver.com', 587)
smtp.ehlo()
smtp.starttls()

smtp.login(SECRET_ID, SECRET_PASS)

myemail = MY_EMAIL
youremail = YOUR_EMAIL

subject = '파이썬을 이용한 자동화 업무'
message = '파이썬을 이용한 테스트'
msg = MIMEText(message.encode('utf-8'), _subtype='plain', _charset='utf-8')
msg['Subject'] = Header(subject.encode('utf-8'), 'utf-8')
msg['From'] = myemail
msg['To'] = youremail
smtp.sendmail(myemail,youremail,msg.as_string())
smtp.quit()