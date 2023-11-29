from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

@app.route('/')
def upload_file():
    return render_template('upload.html')

@app.route('/process', methods=['GET', 'POST'])
def process():
    file = request.files['file']
    df = pd.read_excel(file)
    table_html = df.to_html()
    print(table_html)
    return render_template('result.html', table_html=table_html)

if __name__ == "__main__":
    app.run(debug=True)