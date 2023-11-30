import streamlit as st
from pymongo import MongoClient
from datetime import datetime
import pandas as pd

# MongoDB에 연결
client = MongoClient('localhost', 27017)
db = client['schedule']
collection = db['events']

# Streamlit 페이지 레이아웃
st.title("일정 기록 페이지")

# 입력 폼
event_date = st.date_input("스케줄 날짜")
priority = st.selectbox("우선순위", ["낮음", "보통", "높음"])
location = st.text_input("장소")

if st.button("일정 추가"):
    # 입력한 데이터를 MongoDB에 삽입
    event_data = {
        'date': datetime.combine(event_date, datetime.min.time()),
        'priority': priority,
        'location': location,
        'timestamp': datetime.now()
    }
    collection.insert_one(event_data)
    st.success("일정이 추가되었습니다.")