import json
from TwitterAPI import TwitterAPI

def tweet():
    with open('TwitterAPI.json', 'r') as json_file:
        data = json.load(json_file)
        consumer_key = data['consumer_key']
        consumer_secret = data['consumer_secret']
        access_token_key = data['access_token_key']
        access_token_secret = data['access_token_secret']
    api = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)
    text = 'Hallo'
    r = api.request('statuses/update', {'status': text})
    return r.status_code




print(tweet())



