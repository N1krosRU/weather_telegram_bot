#!venv/bin/python
import dotenv
import os
import telebot
from telebot import types
import gismeteo

# Считываем ключ из переменной окружения или файла .env если он имеется
dotenv.load_dotenv()
BOT_API_KEY = os.getenv("BOT_API_KEY")
bot = telebot.TeleBot(BOT_API_KEY)


# Обработчики команд
@bot.message_handler(commands=['start'])
def command_start(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    buttoon_gps = types.KeyboardButton(
        text='Узнать погоду по метке геопозиции', request_location=True)
    keyboard.add(buttoon_gps)
    bot.send_message(message.from_user.id, 'Нажимай на кнопку под областью чата и узнай погоду в любой точке мира',
                     reply_markup=keyboard)


@bot.message_handler(content_types=['location'])
def location(message):
    if message.location is not None:
        coordinates = f'{message.location.latitude}, {message.location.longitude}'
        bot.send_message(message.from_user.id,
                         f"Ваши координаты: {coordinates}")
        bot.send_message(message.from_user.id,
                         gismeteo.get_cur_weather_by_geo(latitude=message.location.latitude, longitude=message.location.longitude))
        bot.send_message(message.from_user.id,
                         gismeteo.get_1d_weather_by_geo(latitude=message.location.latitude, longitude=message.location.longitude))


@bot.message_handler(content_types=["text"])
def print_message(message):
    bot.send_message(message.from_user.id,
                     f"Привет {message.from_user.username}, отправь мне свою геопозицию и узнай погоду")


bot.polling(none_stop=True, interval=0)
