import os

dir_path = "static"

all_files = os.listdir(dir_path)

txt_files = []
print(f"전체 파일 목록")
for file in all_files:
    print(file)
    if file.endswith('.txt'):
        txt_files.append(file)

print(txt_files)

for filename in txt_files:
    file_path = os.path.join(dir_path, filename)
    with open(file_path, 'r', encoding='utf-8') as f:
        print(f"{filename}의 내용 : {f.read()}")