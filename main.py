import requests
from twilio.rest import Client

API_KEY = 'Your OpenWeather API key'
MY_LAT = 43.826069 # Yours
MY_LONG = -111.789528 # Yours
OWN_ENDPOINT = 'https://api.openweathermap.org/data/2.5/onecall'
ACCOUNT_SID = 'Your Twilio account sid'
AUTH_TOKEN = 'Your Twilio auth token'

weather_params = {
    'lat': MY_LAT,
    'lon': MY_LONG,
    'appid': API_KEY,
    'exclude': 'current,minutely,daily'
}

response = requests.get(OWN_ENDPOINT, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data['hourly'][:12] 

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data['weather'][0]['id']
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    message = client.messages \
                .create(
                body="It's going to rain or snow today. Remember to bring an unmbrella",
                from_='Your Twilio phone number',
                to='Your actual phone number'
                 )
    print(message.status)