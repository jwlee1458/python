import os
import time

DIR_WATCH = "static"

previous_files = set(os.listdir(DIR_WATCH))

while True:
    time.sleep(1)
    print("모니터링중")
    current_files = set(os.listdir(DIR_WATCH))
    new_files = current_files - previous_files
    for filename in new_files:
        file_path = os.path.join(DIR_WATCH, filename)
        with open(file_path,'r', encoding='utf-8') as f:
            lines = f.readlines()
            for line in lines:
                if line.startswith("#") or line.startswith("//"):
                    print(f"새로 주석 처리된 라인 {line}")
                    
    previous_files = current_files