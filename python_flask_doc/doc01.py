from docx import Document
from docx2pdf import convert
import os

doc = Document(os.path.join("python_flask_doc", 'test.docx'))

for paragraph in doc.paragraphs:
    if 'NAME' in paragraph.text:
        paragraph.text = paragraph.text.replace('NAME', '조정원')
    elif 'EMAIL' in paragraph.text:
        paragraph.text = paragraph.text.replace('EMAIL', 'a@a.com')
    elif 'COUNT' in paragraph.text:
        paragraph.text = paragraph.text.replace('COUNT', '200')

doc_file = 'test_01.docx'
pdf_file = 'test_01.pdf'
doc.save(os.path.join("python_flask_doc", doc_file))
convert(os.path.join("python_flask_doc", doc_file), "python_flask_doc", pdf_file)