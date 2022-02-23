from pymongo import MongoClient
client = MongoClient()
db = client.Database1
collection = db.Collection1
data = collection.find(projection={'_id': False, 'price.selling_price': True})
list = []
for post in data:
    list.append(post['price']['selling_price'])

gemiddelde = sum(list)/len(list)
print('Gemiddelde is:', gemiddelde)
