import json
mx = -180
with open('Stations.json', 'r') as json_file:
    data = json.load(json_file)
    for station in data['payload']:
        print(f"{station['namen']['lang']:25}- {station['code']:8}: {station['stationType']:1}")
        x = station['lng']
        if x > mx:
            mx = x
            MeestOost = station['namen']['lang']

print(f"\nHet meest oostelijk gelegen station is {MeestOost}")

