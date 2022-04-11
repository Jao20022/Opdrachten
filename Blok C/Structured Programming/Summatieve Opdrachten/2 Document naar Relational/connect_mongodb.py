from pymongo import MongoClient
client = MongoClient()
db = client.[database]
mongo_profiles = db.[profile collection]
mongo_sessions = db.[sessions collection]
mongo_products = db.[products collection]
