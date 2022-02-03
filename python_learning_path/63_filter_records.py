import pymongo
from bson.objectid import ObjectId

myclient = pymongo.MongoClient("mongodb://localhost:27017")

mydb=myclient["node-app"]

mycollection = mydb["products"]

filter = {"name": "iphone x"}

#result = mycollection.find(filter)

# result = mycollection.find({
#     "name": {
#         "$in" : ["iphone 7","iphone x"]
#     }
# })


# result = mycollection.find({
#     "price": {
#         "$gte": 7000
#     }
# })



result = mycollection.find({
    "name": {"$regex": "^i"}
})

for i in result:
    print(i)


# result = mycollection.find_one({"_id": ObjectId("61f8f0750d753b720b2d2b1d")})
# print(result)