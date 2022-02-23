from pymongo import MongoClient
client = MongoClient()
db = client.Database1
collection = db.Collection1

print(collection.find_one({'name':{'$regex': '^R'}}))