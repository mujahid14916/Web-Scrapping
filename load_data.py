import pymongo
import json

client = pymongo.MongoClient()
db = client['bda']
collection = db['coursera']
collection.drop()
with open('data.json', 'r') as f:
    doc_str = f.read()
    data = json.loads(doc_str)
collection.insert_many(documents=data)
