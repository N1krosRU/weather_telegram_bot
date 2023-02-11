## Иструкция по созданию Telegram Bot'а в Linux

### 0) Подготовка Linux к работе
Обновляем Linux:
```
$ apt update
$ apt upgrade
```
### 1) Установка Python
Установка библиотек для сборки Python:
```
$ sudo apt-get install wget build-essential checkinstall
$ sudo apt-get install libreadline-gplv2-dev libncursesw5-dev libssl-dev
$ sudo apt-get install libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev libffi-dev zlib1g-dev
$ sudo apt install libssl-dev libncurses5-dev libsqlite3-dev libreadline-dev libtk8.6 libgdm-dev libdb4o-cil-dev libpcap-dev
```
    
Создаём и переходим в папку куда скачаем нужную версию Python:
```   
$ mkdir python_interpreter
$ cd python_interpreter
```

Загружаем и распаковываем Python:
```   
$ sudo wget https://www.python.org/ftp/python/3.11.0/Python-3.11.0.tgz
$ sudo tar xzf Python-3.11.0.tgz
```

Переходим в распакованную папку Python и запускаем установку:
```
$ cd Python-3.11.0
$ sudo ./configure --enable-optimizations
$ sudo make altinstall
```

### 2) Создание виртуального окружения Python (копия интерпретатора, чтобы не засирать базовый различными библиотеками)
Создаём папку проекта и виртуальное окружение в ней:
```
$ mkdir python_project
$ cd python_project
$ mkdir weather_telegram_bot
$ cd weather_telegram_bot
$ python3.11 -m venv venv
```

Активируем виртуальное окружение, обновляем/устанавливаем необходимые пакеты:
```
$ source venv/bin/activate
$ pip -V
$ pip install -U pip
$ pip install pytelegrambotapi
$ pip install ...
$ pip install ...
$ pip list
$ deactivate
```
Окружение готово к работе!

### 3) Пример запуска Python скрипта
Копируем файл `bot.py`		в папку `python_project/weather_telegram_bot`
Копируем файл `weather.py`	в папку `python_project/weather_telegram_bot`

Активируем виртуальное окружение с установленными пакетами и запускаем скрипт.
```
$ cd python_project/weather_telegram_bot
$ source venv/bin/activate
$ python bot.py
```

### 4) Пример запуска сервиса который исполняет Python скрипт

Делаем файлы исполняемым:
```
$ cd python_project/weather_telegram_bot
$ chmod +x bot.py
$ chmod +x weather.py
```

Копируем файл `weather_telegram_bot.service` в папку `/etc/systemd/system`.

Содержимое файла weather_telegram_bot.service
```
[Unit]
Description=weather_telegram_bot
After=network.target

[Service]
Type=simple
ExecStart=/home/n1kros/python_project/weather_telegram_bot/venv/bin/python /home/n1kros/python_project/weather_telegram_bot/bot.py
KillMode=process
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

Пояснение к ExecStart
```
/home/n1kros/python_project/weather_telegram_bot/venv/bin/python - путь к интерпретатору Python
/home/n1kros/python_project/weather_telegram_bot/bot.py          - путь к исполняемому файлу Python
```

Далее перезапускаем демона `systemctl` и запускаем сервис:
```
$ sudo systemctl daemon-reload			
$ sudo systemctl enable weather_telegram_bot.service
$ sudo systemctl start weather_telegram_bot.service  
$ sudo systemctl status weather_telegram_bot.service  
```
Теперь сервис будет автоматически запускаться после запуска системы, и исполнять наш Python скрипт!



## Полезные ссылки
1. [Настройка Ubuntu](https://losst.ru/nastrojka-ubuntu-server-posle-ustanovki#1_%D0%9E%D0%B1%D0%BD%D0%BE%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5_%D1%81%D0%B8%D1%81%D1%82%D0%B5%D0%BC%D1%8B)
2. [Настройка сети в Ubuntu](https://losst.ru/nastrojka-seti-iz-konsoli-ubuntu#%D0%A0%D1%83%D1%87%D0%BD%D0%B0%D1%8F_%D0%BD%D0%B0%D1%81%D1%82%D1%80%D0%BE%D0%B9%D0%BA%D0%B0_%D1%81%D0%B5%D1%82%D0%B8_%D0%B2_Ubuntu)
3. [Установка Python на Linux](https://tecadmin.net/install-python-3-7-on-ubuntu-linuxmint/)
4. [Автозапуск Python скриптов](https://mirivlad.ru/kak-ustanovit-v-avtozapusk-python-skript-ispolzuya-systemd/)
5. [Бот для начинающих](https://mastergroosha.github.io/telegram-tutorial/)
