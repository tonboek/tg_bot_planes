#-*- coding: utf-8-sig -*-
import requests
from config import WEATHER_TOKEN

async def get_weather(city, WEATHER_TOKEN):
    try:
        r = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={WEATHER_TOKEN}&units=metric&lang=ru')
        data = r.json()

        wd = data['weather'][0]['main']
        if wd in rus_desk:
            wd = rus_desk[wd]
        else:
            wd = 'Не совсем понятно что за погода...'

        city = data['name']
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        pressure = data['main']['pressure']
        wind = data['wind']['speed']
        visible = data['visibility']
        wind_deg = data['wind']['deg']

        await message.answer(f'<b>Погода в городе {city}:</b>\nТемпература: {temperature}°C, {wd}\nВлажность воздуха: {humidity}%\n\
Атмосферное давление: {pressure} мм.рт.ст\nВетер: {wind} м/с\nНаправление ветра: {wind_deg}°\nВидимость: {visible} м.', parse_mode='HTML')

    except:
        await message.answer('Проверь название введённого города. Если тебе до сих пор выходит это сообщение, то, скорее всего, твоего города нет в списке.')
