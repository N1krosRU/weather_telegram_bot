#!venv/bin/python
import dotenv
import os
import telebot
from telebot import types
import weather

dotenv.load_dotenv()
BOT_API_KEY = os.getenv("BOT_API_KEY")  # Считываем ключ из переменной окружения или файла .env если он имеется
bot = telebot.TeleBot(BOT_API_KEY)


# Обработчики команд
@bot.message_handler(commands=['help'])
def command_help(message):
    bot.send_message(message.from_user.id, 'Нажимай на кнопки под областью чата и узнай погоду в любой точки мира')


@bot.message_handler(commands=['start'])
def command_start(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    buttoon_gps = types.KeyboardButton(text='Узнать погоду по GPS', request_location=True)
    buttoon_place = types.KeyboardButton('Узнать погоду в конкретном месте')
    keyboard.add(buttoon_gps, buttoon_place)
    bot.send_message(message.from_user.id, 'Нажимай на кнопки под областью чата и узнай погоду в любой точки мира',
                     reply_markup=keyboard)


@bot.message_handler(content_types=['location'])
def location(message):
    if message.location is not None:
        coordinates = f'{message.location.latitude},{message.location.longitude}'
        bot.send_message(message.from_user.id, weather.what_location(coordinates))
        bot.send_message(message.from_user.id, weather.what_weather(coordinates))


@bot.message_handler(content_types=["text"])
def weather_place(message):
    if message.text == 'Узнать погоду в конкретном месте':
        bot.send_message(message.from_user.id, 'Где узнать погоду?')
    else:
        user_place = message.text
        bot.send_message(message.from_user.id, weather.what_location(user_place))
        bot.send_message(message.from_user.id, weather.what_weather(user_place))


bot.polling(none_stop=True, interval=0)
