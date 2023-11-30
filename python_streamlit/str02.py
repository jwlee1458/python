import streamlit as st
from pymongo import MongoClient
from faker import Faker
import pandas as pd

client = MongoClient('mongodb://localhost:27017')
db = client['fake_database']
#collection = db['fake_collection']
collection_name = 'fake_collection'

if collection_name in db.list_collection_names():
    db[collection_name].drop()

collection = db[collection_name]

fake = Faker('ko_KR')

def generate_fake_data(num):
    for _ in range(num):
        fake_data = {
            'name' : fake.name(),
            'email' : fake.email(),
            'age': fake.random_int(min=18, max=80),
            'address': fake.address()
        }
        collection.insert_one(fake_data)

st.title("가상 데이터 생성 및 조회")
num_records = st.number_input("생성할 데이터 수를 입력하세요", min_value=1, max_value=100)

if st.button("가상 데이터 생성"):
    generate_fake_data(num_records)
    st.success(f"{num_records} 정상 데이터 생성")

#출력 파트
data_from_mongodb = collection.find()
df = pd.DataFrame(data_from_mongodb)
st.dataframe(df)