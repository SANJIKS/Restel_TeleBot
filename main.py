import json
import requests
import telebot
from telebot import types

from parsing import get_all_hotels, get_all_rooms, get_hotel_name, get_top_hotels

Token = '5800386865:AAGBVsed9AcxVzA2a_opNz_Zjb7jDYzCGd8'

bot = telebot.TeleBot(token=Token)

def get_keyboard():
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton('Все отели', callback_data='all')
    button2 = types.InlineKeyboardButton('Лучшие отели', callback_data='top')
    button3 = types.InlineKeyboardButton('Все комнаты', callback_data='rooms')
    button4 = types.InlineKeyboardButton('Выйти', callback_data='quit')
    markup.add(button1, button2, button3, button4)
    return markup


@bot.message_handler(commands=['start', 'hi'])
def start(message):
    bot.send_message(message.chat.id, text='Здравствуйте! Где хотели бы заселиться?', reply_markup=get_keyboard())


@bot.callback_query_handler(func=lambda call: call.data == 'all')
def get_hotels(call):
    chat_id = call.message.chat.id
    hotels = get_all_hotels()
    
    markup = types.InlineKeyboardMarkup()

    for hotel in hotels:
        markup.add(types.InlineKeyboardButton(f'{hotel["name"]}', callback_data=f'hotel_{hotel["id"]}'))
    bot.send_message(chat_id=chat_id, text='Список всех отелей:', reply_markup=markup) 


@bot.callback_query_handler(func=lambda call: call.data.startswith('hotel_'))
def handle_hotel_callback(call):
    chat_id = call.message.chat.id
    hotel_id = int(call.data.split('_')[1])
    hotels = get_all_hotels()
    reply_mark = types.InlineKeyboardMarkup()
    booking = types.InlineKeyboardButton('Забронировать', callback_data='booking')
    reply_mark.add(booking)

    for hotel in hotels:
        if hotel['id'] == int(hotel_id):
            bot.send_message(chat_id=chat_id, text=f'Название: {hotel["name"]}\n \nЗвезды: {hotel["stars"]}\n \nОписание: {hotel["description"]}\n \nАдрес: {hotel["address"]}\n \nНравится: {hotel["likes"]} пользователям\n \nРейтинг: {hotel["rating"]}', reply_markup=reply_mark)



@bot.callback_query_handler(func=lambda call: call.data == 'booking')
def go_to_site(call):
    chat_id = call.message.chat.id
    bot.send_message(chat_id=chat_id, text='Чтобы забронировать номер, перейдите на наш сайт: https://hotel-booking-api-xfpw.onrender.com/', reply_markup=get_keyboard())





@bot.callback_query_handler(func=lambda call: call.data == 'rooms')
def get_rooms(call):
    chat_id = call.message.chat.id
    rooms = get_all_rooms()
    for item in rooms:
        hotel_name = get_hotel_name(item['id'])
        bot.send_message(chat_id=chat_id, text=f'Отель: {hotel_name}\n \nНомер комнаты: {item["room_number"]}\n \nТип комнаты: {item["room_type"]}\n \nЦена за ночь: {item["price_per_night"]}')
    bot.send_message(chat_id=chat_id, text='Дальше', reply_markup=get_keyboard())




@bot.callback_query_handler(func=lambda call: call.data =='top')
def top_hotels(call):
    chat_id = call.message.chat.id
    top_hotels = get_top_hotels()
    for item in top_hotels:
        bot.send_message(chat_id=chat_id, text=f'Название: {item["name"]}\n \nЗвезды: {item["stars"]}\n \nОписание: {item["description"]}\n \nАдрес: {item["address"]}')
    bot.send_message(chat_id=chat_id, text='Дальше', reply_markup=get_keyboard())



@bot.callback_query_handler(func=lambda call: call.data =='quit')
def byebye(call):
    chat_id = call.message.chat.id
    bot.send_message(chat_id=chat_id, text='До свидания! Если я вам еще раз понадоблюсь, нажмите /start')




bot.polling()