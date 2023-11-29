from flask import Flask, render_template, request
from flask import send_file
import os
import openpyxl
from googletrans import Translator
import time

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('upload.html')

@app.route('/process', methods=["POST"])
def process():
    file = request.files["file"]
    file.save(os.path.join("python_flask_trans", "uploads", file.filename))

    workbook = openpyxl.load_workbook(os.path.join("python_flask_trans", "uploads", file.filename))
    sheet = workbook.active

    #구글 번역
    translator = Translator()
    for row in sheet.iter_rows():
        for cell in row:
            translated_text = translator.translate(cell.value, dest='en').text
            cell.value = translated_text
        
        time.sleep(0.5)
        
    workbook.save(os.path.join("python_flask_trans", "uploads", "transrated_excel.xlsx"))

    return render_template("result.html", file_name = file.filename)

@app.route('/download_report')
def download_report():
    return send_file(os.path.join("uploads", 'transrated_excel.xlsx'), as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)