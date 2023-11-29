from flask import Flask, render_template, request
import re
from collections import Counter
import requests
import time
import os
from dotenv import load_dotenv, find_dotenv

dotenv_path = find_dotenv(filename=".env", raise_error_if_not_found=True)
load_dotenv(dotenv_path)
API_KEY = os.getenv("API_KEY")

app = Flask(__name__)

def get_criminalip_info(ip_address):
    url = f"https://api.criminalip.io/v1/asset/ip/summary?ip={ip_address}"
    payload={}
    headers = {
        "x-api-key": API_KEY
    }

    response = requests.get(url, headers=headers, data=payload)
    if response.status_code == 200:
        return response.json()
    else:
        return None

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']
    
        with open(os.path.join("python_flask_criminal","access.log"), "wb") as f:
            f.write(file.read())

        with open(os.path.join("python_flask_criminal","access.log"), "r", encoding="utf-8") as f:
            log_content = f.read()

        ip_list = re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", log_content)
        ip_counter = Counter(ip_list)
        top_10_ips = ip_counter.most_common(10)

        results = []
        for ip_address, count in top_10_ips:
            time.sleep(2)
            result = get_criminalip_info(ip_address)
            if result:
                results.append({
                    'ip_address': result['ip'],
                    'inbound_score': result['score']['inbound'],
                    'outbound_score': result['score']['outbound'],
                    'country': result['country'],
                    'country_code': result['country_code'],
                    'region': result['region'],
                    'city': result['city'],
                    'latitude': result['latitude'],
                    'longitude': result['longitude']
                })

        return render_template('index.html', results=results)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)