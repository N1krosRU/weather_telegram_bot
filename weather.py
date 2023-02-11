#!venv/bin/python
import requests

params_for_location = {
    'format': '',  # погода одной строкой
    'M': '',  # скорость ветра в "м/с"
    'lang': 'ru',  # язык
    '1': ''  # на один день
}

params_for_weather = {
    'format': '2',  # погода одной строкой
    'M': '',  # скорость ветра в "м/с"
    'lang': 'ru',  # язык
}


def make_url(place):
    # в URL задаём место, в котором узнаем погоду
    return f'http://wttr.in/{place}'


def what_weather(place):
    try:
        url = make_url(place)
        response = requests.get(url, params_for_weather)
        if response.status_code == 200:
            return response.text
        else:
            return '<ошибка на сервере погоды>'
    except requests.ConnectionError:
        return '<сетевая ошибка>'


def what_location(place):
    try:
        url = make_url(place)
        response = requests.get(url, params_for_location)
        if response.status_code == 200:
            my_response = response.text
            start_index = my_response.find("Местоположение:")
            location_str = my_response[start_index:]
            end_index = location_str.find("]")
            location_str = location_str[:end_index + 1]
            return location_str
        else:
            return '<ошибка на сервере погоды>'
    except requests.ConnectionError:
        return '<сетевая ошибка>'
