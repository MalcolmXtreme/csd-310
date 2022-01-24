import collections
import pymongo
from pymongo import MongoClient

client = MongoClient ("mongodb+srv://admin:admin@cluster0.kpnte.mongodb.net/Pytech")
db= client["Pytech"]
mycol = db["Students"]



mycol.update_one({"Student FirstName":"Chase"},
  {"$set": {
    "Student FirstName":"Steven"
  }
})

#mycol.update_one({"Student FirstName":"Chase"},
#{
  #"$set": {
 #   "Student Name":"Steven"
  #}
#})

x2 = mycol.find_one()
print(x2)
#print("--DISPLAYING STUDENT DOCUMENTS--")
#for x in mycol.find():
 #print(x )




#print(client.list_database_names())
#print(db.list_collection_names())


