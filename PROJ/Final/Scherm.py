import json
from TwitterAPI import TwitterAPI, TwitterPager
import requests

# Haalt de locatie op
def locatie_ophalen():
    r = requests.get('https://ipapi.co/json').json()
    if 'error' in r:
        return 'Utrecht'
    locatie = r['city']
    print(locatie)
    return locatie


# Haalt weer op
def weer():
    global locatie
    Weer = requests.get(
        f'https://api.openweathermap.org/data/2.5/weather?q={locatie}&lang=nl&appid=7c28e81d42bee8d9b03d7e424fe4e8bf').json()
    Temperatuur = round(Weer['main']['temp'] - 274.15, 1)
    Gevoel = round(Weer['main']['feels_like'] - 274.15, 1)
    Bewolking = Weer['weather'][0]['description']
    text = f'{Bewolking}\nHet is {Temperatuur}℃\nHet voelt als {Gevoel}℃'
    return text

# Haalt meest recente tweet op
def get_tweet():
    for item in pager.get_iterator():
        text = item['text']
        return text


# Bepaalt wat er op het scherm komt. Is de meest recente tweet tenzij deze al op het scherm geweest is.
# Dan komt het weer op het scherm
def scherm():
    global MeestRecente
    tweet = get_tweet()
    if not tweet == MeestRecente:
        MeestRecente = tweet
        return tweet
    elif tweet == MeestRecente:
        return weer()


# Haalt de gegevens voor de twitterAPI uit een json bestand
with open("TwitterAPI.json") as json_file:
    data = json.load(json_file)
    consumer_key = data['consumer_key']
    consumer_secret = data['consumer_secret']
    access_token_key = data['access_token_key']
    access_token_secret = data['access_token_secret']

TwitterApi = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)
SCREEN_NAME = 'rhaxeyar'

# Haalt 1 twitter van het twitter account
pager = TwitterPager(TwitterApi, 'statuses/user_timeline', {'screen_name': SCREEN_NAME, 'count': 1})
MeestRecente = str
locatie = locatie_ophalen()

