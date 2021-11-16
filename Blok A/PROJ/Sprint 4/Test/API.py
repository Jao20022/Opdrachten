import requests
r = requests.get('https://ipapi.co/json').json()
print(r)
locatie = r['city']
print(locatie)