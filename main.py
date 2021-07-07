import requests

API_KEY = '90110c6c5296ba96a34270bcbcee731b'
MY_LAT = 43.826069
MY_LONG = -111.789528
OWN_ENDPOINT = 'https://api.openweathermap.org/data/2.5/onecall'

weather_params = {
    'lat': MY_LAT,
    'lon': MY_LONG,
    'appid': API_KEY
}

response = requests.get(OWN_ENDPOINT, params=weather_params)
response.raise_for_status()

data = response.json()
print(data)