import requests
from datetime import datetime

MY_LAT = 52.302160  # Your latitude
MY_LONG = 17.090470  # Your longitude


def is_iss_overhead(lat, lng):
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    return abs(lat-iss_latitude) <= 5 and abs(lng-iss_longitude) <= 5


def is_dark_now(sset, srise):
    time_now = datetime.now()
    return time_now.hour > sset or time_now.hour < srise


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}
response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

if is_iss_overhead(MY_LAT, MY_LONG) and is_dark_now(sunset, sunrise):
    #  send an email
    pass




