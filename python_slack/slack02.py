from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import os
from dotenv import load_dotenv, find_dotenv

dotenv_path = find_dotenv(filename=".env", raise_error_if_not_found=True)
load_dotenv(dotenv_path)
SLACK_API_TOKEN = os.getenv("SLACK_API_TOKEN")

# Slack channel to send the message to
def sendSlackWebhook(file_path):
    client = WebClient(token=SLACK_API_TOKEN)
    try:
        response = client.files_upload(
            channels="#python_test",
            file=file_path,
            title=f"테스트입니다."
        )
        print(f"정상적으로 보냄")
    except SlackApiError as e:
        print(f"오류 발생 {e}")

output_path = os.path.join("python_rss", "result.xlsx")
sendSlackWebhook(output_path)