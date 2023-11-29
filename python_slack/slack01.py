import requests
import json
import os
from dotenv import load_dotenv, find_dotenv

dotenv_path = find_dotenv(filename=".env", raise_error_if_not_found=True)
load_dotenv(dotenv_path)
SLACK_URL = os.getenv("SLACK_URL")

slack_url = SLACK_URL

def sendSlackWebhook(strText):
    headers = {"Content-type":"application/json"}
    data = {"text":strText}

    response = requests.post(slack_url, headers=headers, data=json.dumps(data))
    
    if response.status_code == 200:
        return "잘 보냈습니다."
    else:
        return "오류 발생"

print(sendSlackWebhook("테스트입니다."))