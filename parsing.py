import requests
import json

def get_top_hotels():
    response = requests.get('https://hotel-booking-api-xfpw.onrender.com/top-hotels/')
    if response.status_code == 200:
        return json.loads(response.text)
    else:
        return 'Ошибочка'
    

def get_all_rooms():
    response = requests.get('https://hotel-booking-api-xfpw.onrender.com/room/')
    if response.status_code == 200:
        return json.loads(response.text)
    else:
        return 'Ошибочка'


def get_all_hotels():
    response = requests.get('https://hotel-booking-api-xfpw.onrender.com/hotel/')
    if response.status_code == 200:
        return json.loads(response.text)
    else:
        return 'Ошибочка'
    

def get_hotel_name(hotel_id):
    hotels = get_all_hotels()
    for name in hotels:
        if name['id'] == hotel_id:
            hotel_name = name['name']
            return hotel_name

