import pymongo
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://dbAdmin:andy1234@cluster0.au0vn.mongodb.net/IBULW?retryWrites=true&w=majority")

db = cluster["IBULW"]
collection = db["users"]

post1 = {"_id":1, "name":"testing2"}
post2 = {"_id":2, "name":"testing3"}
collection.insert_one(post)
collection.insert_many([post1, post2])

results = collection.find({"name":"testing2"})
for result in results:
    print(result)
result = collection.find_one({"_id":1})
print(result)

