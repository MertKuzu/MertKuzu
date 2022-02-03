import pymongo
from bson.objectid import ObjectId
myclient = pymongo.MongoClient("mongodb://localhost:27017")
mydb=myclient["node-app"]
mycollection = mydb["products"]


for i in mycollection.find():
    print(i)


result = mycollection.delete_one({"name":"iphone x"})

for i in mycollection.find():
    print(i)


#delete_many()   same thing