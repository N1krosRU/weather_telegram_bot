# Как работать с Докером

# 1) Перейти в папку с файлом Dockerfile
# cd /root/weather_telegram_bot

# 2) Создать образ из Dockerfile
# docker build -t weatherbot_image .

# 3) Проверить созданный образ 
# docker images

# 4) Создаём и запускаем контейнер 
# docker run -d --rm --name weatherbot_container weatherbot_image

# 5) Проверить созданный контейнер
# docker ps -a

# 6) Зайти в контейнер
# docker exec -it weatherbot_container /bin/sh

# Используем образ Python версии 3.10.11
FROM python:3.10.11-alpine

# Задаём рабочую директорию и переходим в неё
WORKDIR ./bots/weather-telegram-bot

# Копируем requirements.txt в образ и устанавливаем зависимости
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

#Копируем все файлы в рабочую директорию
COPY . .

# Запускаем бота
CMD [ "python", "./bot.py" ]