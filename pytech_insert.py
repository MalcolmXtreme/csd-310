
import pymongo
import collections
from pymongo import MongoClient


client = MongoClient ("mongodb+srv://admin:admin@cluster0.kpnte.mongodb.net/Pytech")

db = client.Pytech
Student_ID = {"I.D":"1007"}
Student_ID2 = {"I.D":"1008"}
Student_ID3 = {"I.D":"1009"}

db.students.insert_one(Student_ID)

db_studentID = db.students.insert_one(Student_ID)
db_studentID = db.students.insert_one(Student_ID2)
db_studentID = db.students.insert_one(Student_ID3)
print(Student_ID, Student_ID2, Student_ID3)


    
                      
   
  







