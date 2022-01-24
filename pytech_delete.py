import collections
import pymongo
from pymongo import MongoClient

client = MongoClient ("mongodb+srv://admin:admin@cluster0.kpnte.mongodb.net/Pytech")
db= client["Pytech"]
mycol = db["Students"]
myquery = {"Student I.D": "1010", "Student FirstName":"Jade"}
x= mycol.find()
#x2= mycol.insert_one({"Student I.D": "1010", "Student FirstName":"Julia", "Student LastName":"Knightly"})
 


for x in mycol.find():
 print(x )

mycol.insert_one({"Student I.D": "1010", "Student FirstName":"Jade", "Student LastName":"Knightly"} )

mycol.find_one({"Student I.D": "1010", "Student FirstName":"Jade"})

mycol.delete_one(myquery)

for x in mycol.find():
 print(x )



#Doesn't work print(x)





