import streamlit as st
from docx import Document
from docx2pdf import convert
from datetime import datetime
import pythoncom
from pymongo import MongoClient
import pandas as pd
import os

pythoncom.CoInitialize()

# MongoDB에 연결
client = MongoClient('localhost', 27017)
db = client['education']
collection = db['results']

st.title("수료증 발급 서비스")

name = st.text_input("이름을 입력하세요")
course = st.selectbox("과정 선택", ["파이썬 입문 과정", "웹해킹분석", "포렌식분석"])
date = st.text_input("날짜를 선택하세요. ex) 2023년 12월 1일")

if st.button("수료증 생성"):

    #수료증 발급 DB 저장
    result_data = {
        'name': name,
        'course': course,
        'date': date,
        'timestamp': datetime.now()
    }
    collection.insert_one(result_data)
    
    doc = Document(os.path.join("python_streamlit", 'templates.docx'))

    for paragraph in doc.paragraphs:
        if 'NAME' in paragraph.text:
            paragraph.text = paragraph.text.replace('NAME', name)
        elif 'COURSE' in paragraph.text:
            paragraph.text = paragraph.text.replace('COURSE', course)
        elif 'DATE' in paragraph.text:
            paragraph.text = paragraph.text.replace('DATE', date)
    
    doc_file = f'{name}_{course}_수료증.docx'
    pdf_file = f'{name}_{course}_수료증.pdf'
    doc.save(os.path.join("python_streamlit", doc_file))
    convert(os.path.join("python_streamlit", doc_file), "python_streamlit", pdf_file)

    st.success("수료증 생성이 완료되었습니다. 아래 버튼으로 다운로드 받으세요.")

    with open(os.path.join("python_streamlit", pdf_file), 'rb') as f:
        pdf_bytes = f.read()
    
    st.download_button(label="수료증 다운로드", data=pdf_bytes, file_name=pdf_file)

#후에는 수료증을 요청한 사용자들의 기록을 mongodb에 기록

st.title("발급 목록")
data_from_mongodb = collection.find()
df = pd.DataFrame(data_from_mongodb, columns=['name', 'course', 'date'])
st.dataframe(df)