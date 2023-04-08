import requests
import json

def get_top_hotels():
    response = requests.get('https://hotel-booking-api-xfpw.onrender.com/top-hotels/')
    if response.status_code == 200:
        return json.loads(response.text)['results']
    else:
        return 'Ошибочка'
    

def get_all_rooms():
    response = requests.get('https://hotel-booking-api-xfpw.onrender.com/room/')
    if response.status_code == 200:
        return json.loads(response.text)['results']
    else:
        return 'Ошибочка'


def get_all_hotels():
    response = requests.get('https://hotel-booking-api-xfpw.onrender.com/hotel/')
    if response.status_code == 200:
        return json.loads(response.text)['results']
    else:
        return 'Ошибочка'
    