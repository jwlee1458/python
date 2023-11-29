import zipfile
import os

dir_path = os.path.join("python_sk", "static")
zip_file = zipfile.ZipFile(os.path.join("python_ftp", "static_folder.zip"), "w")

#os.walk로 출력
for root, dirs, files in os.walk(dir_path):
    for file in files:
        file_path = os.path.join(root, file)
        relative_path = os.path.relpath(file_path, dir_path)
        zip_file.write(file_path, os.path.join("static", relative_path))

zip_file.close()