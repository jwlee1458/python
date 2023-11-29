import re
from collections import Counter
import requests
import time
import os
from dotenv import load_dotenv, find_dotenv

dotenv_path = find_dotenv(filename=".env", raise_error_if_not_found=True)
load_dotenv(dotenv_path)
API_KEY = os.getenv("API_KEY")

def get_criminalip_info(ip_address):
    url = f"https://api.criminalip.io/v1/asset/ip/summary?ip={ip_address}"

    payload={}
    headers = {
    "x-api-key": API_KEY
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    if response.status_code == 200:
        return response.json()
    else:
        print("접속 오류 발생")
        
if __name__ == "__main__":
    
    log_file = 'access.log'
    ip_list = []

    with open(os.path.join("python_criminal", log_file), 'r') as f:
        for line in f:
            match = re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", line)
            if match:
                ip_list.append(match[0])

    ip_counter = Counter(ip_list)
    top_10_ips = ip_counter.most_common(10)

    #저장용
    with open(os.path.join("python_criminal", 'urls_list.txt'), 'w', encoding='utf-8') as f:
        for ip_address, count in top_10_ips:
            print(f"{ip_address}: 접속횟수 {count}")
            f.write(f"{ip_address}: 접속횟수 {count}")
    
    for ip_address, count in top_10_ips:
        time.sleep(0.5)
        result = get_criminalip_info(ip_address)
        if result:
            print("IP 정보:")
            print(f"IP 주소: {result['ip']}")
            print(f"점수 (수신): {result['score']['inbound']}")
            print(f"점수 (발신): {result['score']['outbound']}")
            print(f"국가: {result['country']}")
            print(f"국가 코드: {result['country_code']}")
            print(f"지역: {result['region']}")
            print(f"도시: {result['city']}")
            print(f"위도: {result['latitude']}")
            print(f"경도: {result['longitude']}")