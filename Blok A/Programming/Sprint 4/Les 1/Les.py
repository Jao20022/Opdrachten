import json

result = 9.0
names = ['John', 'Frank']
results = [
    {
        'name' : 'John',
        'result' : 7.0
    },{
        'name' : 'Frank',
        'result' : 7.0
    }
]

with open('result.json', 'w') as json_file:
    json.dump(results, json_file, indent=4)