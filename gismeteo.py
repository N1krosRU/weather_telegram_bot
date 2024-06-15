import json
import dotenv
import os
import requests

# Считываем ключ из переменной окружения или файла .env если он имеется
dotenv.load_dotenv()
GISMETEO_TOKEN = os.getenv("GISMETEO_TOKEN")


def get_cur_weather_by_geo(latitude, longitude):
    headers = {"X-Gismeteo-Token": GISMETEO_TOKEN,
               "Accept-Encoding": "gzip, deflate"}
    params = {"latitude": latitude, "longitude": longitude}
    response = requests.get(
        "https://api.gismeteo.net/v2/weather/current/", params=params, headers=headers)
    # трансформируем ответ в виде json в словарь python'a
    response_dict = response.json()
    # response_date = response_dict["response"]["date"]["local"]
    response_description = response_dict["response"]["description"]["full"]
    response_temp_air = response_dict["response"]["temperature"]["air"]["C"]
    response_temp_comfort = response_dict["response"]["temperature"]["comfort"]["C"]
    return (f"Сейчас на улице {response_description}\nТемпература {response_temp_air} °C\nОщущается как {response_temp_comfort} °C")


def get_1d_weather_by_geo(latitude, longitude):
    headers = {"X-Gismeteo-Token": GISMETEO_TOKEN,
               "Accept-Encoding": "gzip, deflate"}
    params = {"latitude": latitude, "longitude": longitude, "days": 1}
    response = requests.get(
        "https://api.gismeteo.net/v2/weather/forecast/", params=params, headers=headers)
    # трансформируем ответ в виде json в словарь python'a
    response_dict = response.json()
    message = "Прогноз погоды на день:\n"
    for i in response_dict["response"]:
        message += "===============================\n"
        message += f'На момент {i["date"]["local"]}\n'
        message += f'Будет {i["description"]["full"]}\n'
        message += f'Температура {i["temperature"]["air"]["C"]} °C\n'
        message += f'Ощущается как {i["temperature"]["comfort"]["C"]} °C\n'
    return message
