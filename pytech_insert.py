import collections
import pymongo
from pymongo import MongoClient

 
client = MongoClient ("mongodb+srv://admin:admin@cluster0.kpnte.mongodb.net/Pytech")
print(client.list_database_names())

db= client.Pytech

collection = db.Students


entry = db.Students

entry.insert_many( [{"Student I.D": "1008"}, {"Student I.D": "1009"}]  )

print(db.list_collection_names())














#cluster = MongoClient("mongodb+srv://admin:admin@cluster0.kpnte.mongodb.net/Pytech")
#db = cluster["Pytech"]
#collections = db ["Pytech"]

