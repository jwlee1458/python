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

for _ in range(100):
    fake_data = {
        'name' : fake.name(),
        'email' : fake.email(),
        'age': fake.random_int(min=18, max=80),
        'address': fake.address()
    }
    collection.insert_one(fake_data)

data_from_mongodb = collection.find()
df = pd.DataFrame(data_from_mongodb)
print(df)