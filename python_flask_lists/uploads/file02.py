import os

dir_path = "static"

all_files = os.listdir(dir_path)
print(f"=====전체 파일 {all_files}=====")

txt_files = []
for file in all_files:
    if file.endswith('.txt') or file.endswith('html'):
        txt_files.append(file)

print(f"=====TEXT파일 {txt_files}======")

for filename in txt_files:
    file_path = os.path.join(dir_path, filename)
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            if line.startswith("#") or line.startswith("//"):
                print(f"주석 처리된 라인 {line}")