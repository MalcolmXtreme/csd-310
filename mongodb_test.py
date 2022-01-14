#import collections
import pymongo 
from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.kpnte.mongodb.net/Pytech"

client = MongoClient ("mongodb+srv://admin:admin@cluster0.kpnte.mongodb.net/Pytech")

db = client.Pytech

print(db.list_collection_names)









#cluster = MongoClient("mongodb+srv://admin:admin@cluster0.kpnte.mongodb.net/Pytech")
#db = cluster["Pytech"]
#collections = db ["Pytech"]

