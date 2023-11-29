from flask import Flask, render_template, request, send_file
import os
from datetime import datetime
import zipfile
import re

app = Flask(__name__)

@app.route('/')
def list():
    upload_path = os.path.join("python_flask_lists", "uploads")
    files = []

    for file in os.listdir(upload_path):
        file_path = os.path.join(upload_path, file)
        #if file_path.endswith('.txt') or file_path.endswith('.py'):
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            matches = re.findall(r"[\w\.-]+@[\w\.-]+", content)
            if matches:
                email = True
            else:
                email = False

        ctime_datetime = datetime.fromtimestamp(os.path.getctime(file_path)).strftime('%Y-%m-%d %H:%M:%S')
        files.append((file, os.path.getsize(file_path), ctime_datetime, email))

    return render_template('list.html', files=files)

@app.route('/compress', methods=["POST"])
def compress():
    upload_path = os.path.join("python_flask_lists", "uploads")
    files = request.form.getlist("files")
    zip_path = os.path.join(upload_path, "compress.zip")
    with zipfile.ZipFile(zip_path, "w") as zip_file:
        for file in files:
            file_path = os.path.join(upload_path, file)
            zip_file.write(file_path, os.path.basename(file_path))

    compressed_file = "compress.zip"
    return render_template('list.html', compressed_file = compressed_file)

@app.route('/download')
def download():
    upload_path = "uploads"
    compressed_file = request.args.get("file")
    zip_path = os.path.join(upload_path, compressed_file)
    return send_file(os.path.join(zip_path), as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)