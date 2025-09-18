import requests
import datetime as dt
from os import environ as ev

NUT_APPID = ev.get('NUT_APPID')
NUT_KEY = ev.get('NUT_KEY')

nutri_endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'
nutri_headers = {
    'Content-Type': 'application/json',
    'x-app-id': NUT_APPID,
    'x-app-key': NUT_KEY,

}

workout_data = {
    'query': input('What did you do: '),
    'gender': 'male',
    'weight_kg': '73',
    'height_cm': '180',
    'age': '37'
}

# Swam 10 olympic pools and did 50 push-ups.

excercise_list = requests.post(url=nutri_endpoint, headers=nutri_headers, json=workout_data)
excercise_list = excercise_list.json()

SHEETY_ENDPOINT = f"https://api.sheety.co/{ev.get('SHEETY_USER')}/treningi/workouts"
sheety_headers = {
    'Content-Type': 'application/json',
    'Authorization': ev.get('SHEETY_AUTH')
}
current_time = dt.datetime.now()
print(excercise_list)
for workout in excercise_list['exercises']:
    sheety_entry = {
        'workout': {
            'date': current_time.strftime('%Y-%m-%d'),
            'time': current_time.strftime('%H:%M'),
            'exercise': workout['name'],
            'duration': workout['duration_min'],
            'calories': workout['nf_calories'],
        }
    }
    add_row_response = requests.post(url=SHEETY_ENDPOINT, json=sheety_entry, headers=sheety_headers)
    print(add_row_response.json())
