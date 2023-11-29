import re
import os
from collections import Counter

log_file = 'access.log'

ip_list = []

with open(os.path.join("python_criminal", log_file), 'r') as f:
    for line in f:
        match = re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", line)
        if match:
            ip_list.append(match[0])

ip_counter = Counter(ip_list)
top_10_ips = ip_counter.most_common(10)

with open(os.path.join("python_criminal", 'urls_list.txt'), 'w', encoding='utf-8') as f:
    for ip_address, count in top_10_ips:
        print(f"{ip_address} 접속 횟수 {count}")
        f.write(f"{ip_address} 접속 횟수 {count}\n")