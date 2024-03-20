import requests
from os import environ as evar
from twilio.rest import Client

weather_params = {
    "lat": 32.321457,
    "lon": 34.853195,
    "appid": evar.get('OWM_KEY'),
    "units": 'metric',
    "cnt": 4
}
weather_data = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=weather_params)
weather_data.raise_for_status()
weather_data = weather_data.json()
print(weather_data)
# for i in range(4):
#     if weather_data["list"][i]["weather"][0]["id"] < 700:
# this is hideous, much nicer version below:
rain_expected = False
for hourly_data in weather_data["list"]:
    if hourly_data["weather"][0]["id"] < 700:
        rain_expected = True

if rain_expected:
    twilio_acc = evar.get('TW_ID')
    twilio_tok = evar.get('TW_KEYs')

    twilio_client = Client(twilio_acc,twilio_tok)
    message = twilio_client.messages.\
        create(body="Dzisiaj bedzie padac", from_="+17867723341", to="+48501434708")
    print(message.status)