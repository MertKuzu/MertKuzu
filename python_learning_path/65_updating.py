import pymongo
from bson.objectid import ObjectId
myclient = pymongo.MongoClient("mongodb://localhost:27017")
mydb=myclient["node-app"]
mycollection = mydb["products"]


for i in mycollection.find():
    print(i)


mycollection.update_one(
    {"name": "iphone x"},
    {"$set": {
        "name": "samsung s7",
        "price": 6500
    }})

#update_many() same

for i in mycollection.find():
    print(i)