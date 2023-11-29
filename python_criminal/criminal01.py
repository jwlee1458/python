import requests
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
    ip_address = '8.8.8.8'
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
        print(f"ISP: {result['isp']}")
        print(f"기관 이름: {result['org_name']}")
        print(f"AS 번호: {result['as_no']}")
        print(f"우편 코드: {result['postal_code']}")
        print(f"위도: {result['latitude']}")
        print(f"경도: {result['longitude']}")