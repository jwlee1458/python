import re
import os

log_file = 'access.log'

ip_set = set()

with open(os.path.join("python_criminal", log_file), 'r') as f:
    for line in f:
        match = re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", line)
        if match:
            ip_set.add(match[0])

with open(os.path.join("python_criminal", 'urls.txt'), 'w', encoding='utf-8') as f:
    for ip_address in ip_set:
        print(ip_address)
        f.write(f"{ip_address}\n")