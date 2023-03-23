#-*- coding: utf-8-sig -*-
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
import asyncio
import random
import requests
from config import TOKEN_API, WEATHER_TOKEN

count = 0
bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

async def sleep(sec):
    await asyncio.sleep(sec)

#Маршруты
Kaz_Nizh = {'start': 'Казань', 'stop': 'Нижнекамск', 'distance': 17}  #Ан-12
Mos_Irk = {'start': 'Москва', 'stop': 'Иркутск', 'distance': 50}  #Ту-104
Mos_Xab = {'start': 'Москва', 'stop': 'Хабаровск', 'distance': 27} #Ту-114
Frun_Zhuk = {'start': 'Центральный аэродром имени М. В. Фрунзе', 'stop': 'Жуковский', 'distance': 20} #Ил-18
#Маршруты

#Самолёты
An_2 = {'sec': 0.3}
An_12 = {'sec': 0.3}
Tu_104 = {'sec': 0.3}
Tu_114 = {'sec': 0.3}
Il_18 = {'sec': 0.3}
Yak_42 = {'sec': 0.2}
Il_86 = {'sec': 0.2}
Tu_144 = {'sec': 0.2}
An_124 = {'sec': 0.2}
An_225 = {'sec': 0.2}
#Самолёты
available = ['Ан-2']

@dp.message_handler(commands = ['about'])
async def about_command(message: types.Message):
    txt = '"Курс на авиацию!" - это захватывающая текстовая игра, которая позволяет игрокам окунуться в мир авиации и \
стать настоящими пилотами. Вы будете управлять различными типами самолетов, сможете почувствовать себя настоящим профессиональным \
пилотом, преодолевая все трудности и препятствия, которые встречаются на вашем пути. Откройте для себя мир авиации и станьте лучшим \
пилотом в "Курс на авиацию!".'
    await message.answer(txt)

@dp.message_handler(commands = ['interesting_fact'])
async def inter_facts(message: types.Message):
    phrases = open('facts.txt', 'r', encoding = 'utf-8')
    facts = phrases.readlines()
    await message.answer(random.choice(facts))

@dp.message_handler(commands = ['start'])
async def start_command(message: types.Message):
    ########  1  АН - 2  ########
    global count
    global available
    while count != 10:
        count += 1
        username = message.from_user.first_name
        txt = f'Приветствую тебя, {username}! На данный момент ты у штурвала лёгкого самолёта Ан-2, на <b>1</b> уровне и у тебя на балансе <b>70 монет!</b> \
Давай расскажу тебе более подробно про этот самолёт. \n\nАн-2, либо же как его ещё называют "Кукурузник" - без преувеличения легенда \
советской авиации. Первый полёт он совершил 21 августа 1948 года. Его умения действительно поражают, ведь Ан-2 используется в спортивных, \
сельскохозяйственных, гражданских целях, к тому же он состоит на вооружении ВВС многих стран. К слову, этот самолёт до сих пор \
выпускают в Китае.'
        await message.answer(txt, parse_mode='HTML')
        async def gotovo(sec):
            msg = await message.answer('Проверка документов')
            dots = '.'
            for i in range(41):
                if i % 3 == 0:
                    dots = '.'
                    await msg.edit_text(f'Проверка документов{dots}  ({i}%)')
                else:
                    dots += '.'
                    await asyncio.sleep(sec)
                    await msg.edit_text(f'Проверка документов{dots}  ({i}%)')

            for i in range(41, 81):
                if i % 3 == 0:
                    dots = '.'
                    await msg.edit_text(f'Проверка багажей пассажиров{dots}  ({i}%)')
                else:
                    dots += '.'
                    await asyncio.sleep(sec)
                    await msg.edit_text(f'Проверка багажей пассажиров{dots}  ({i}%)')

            for i in range(80, 101):
                if i % 3 == 0:
                    dots = '.'
                    await msg.edit_text(f'Посадка пассажиров{dots}  ({i}%)')
                else:
                    dots += '.'
                    await asyncio.sleep(sec)
                    await msg.edit_text(f'Посадка пассажиров{dots}  ({i}%)')
                if i == 100:
                    await msg.edit_text('Самолёт готов ко взлёту!')
        async def flight(start, stop, distance, sec):
            cht = '🛫' + '-' * (distance - 1)
            flight_process = start + '\n' + cht + '\n' + stop
            msg = await bot.send_message(message.from_user.id,
                                            f'{flight_process}')
            for i in range(1, distance):
                cht = '- ' * distance
                if i == distance - 1:
                    cht = cht.split()
                    cht[i] = '🛬'
                    cht = ''.join(cht)
                else:
                    cht = cht.split()
                    cht[i] = '✈️'
                    cht = ''.join(cht)
                flight_process = start + '\n' + cht + '\n' + stop
                await asyncio.sleep(sec)
                await msg.edit_text(f'{flight_process}')

        await sleep(15)
        txt = 'А теперь давай попробуем сделать первый перелёт. Маршрут следующий: Казань - Нижнекамск.'
        await message.answer(txt)
        await sleep(3)
        await gotovo(An_2['sec'])
        await flight(Kaz_Nizh['start'], Kaz_Nizh['stop'], Kaz_Nizh['distance'], An_2['sec'])
        await sleep(1)
    
        ########  2  АН - 12  ########
        async def flight_cancel(start, stop, distance, sec):
            cht = '🛫' + '-' * (distance - 1)
            flight_process = start + '\n' + cht + '\n' + stop
            msg = await bot.send_message(message.from_user.id,
                                            f'{flight_process}')
            flag = True
            for i in range(1, distance):
                cht = '- ' * distance
                if i == distance // 2:
                    cht = cht.split()
                    cht[i] = '✈️'
                    cht = ''.join(cht)
                    flight_process = start + '\n' + cht + '\n' + '❗️Возникли поломки. Необходимо вернуться обратно.❗️' + '\n' + stop
                    await asyncio.sleep(sec)
                    await msg.edit_text(f'{flight_process}')
                    await sleep(3)
                    for x in range(distance // 2, -1, -1):
                        cht = '- ' * distance
                        cht = cht.split()
                        cht[x] = '✈️'
                        cht = ''.join(cht)
                        flight_process = start + '\n' + cht + '\n' + stop
                        await asyncio.sleep(sec)
                        await msg.edit_text(f'{flight_process}')
                        if x == 0:
                            cht = '- ' * distance
                            cht = cht.split()
                            cht[x] = '🛬'
                            cht = ''.join(cht)
                            flight_process = start + '\n' + cht + '\n' + stop
                            await asyncio.sleep(sec)
                            await msg.edit_text(f'{flight_process}')
                            flag = False
                            break
                else:
                    cht = cht.split()
                    cht[i] = '✈️'
                    cht = ''.join(cht)
                    flight_process = start + '\n' + cht + '\n' + stop
                    await asyncio.sleep(sec)
                    await msg.edit_text(f'{flight_process}')
                if flag == False:
                    break
        txt = 'Великолепная посадка и отличная работа экипажа! Твой уровень повысился до <b>2</b>, а баланс равен <b>150 монетам</b>. Ты действительно заслужил этого, поэтому встречай в своём новый самолёт - <b>Ан-12</b>. \
\n\n<b>Ан-12</b> - настоящая легенда авиации, которая продолжает летать и по сей день, несмотря на свой почтенный возраст. Он прост в эксплуатации, \
разработан на хорошем техническом уровне. Самое то для тебя!'
        available.append('Ан-12')
        await message.answer(txt, parse_mode='HTML')
        await sleep(15)
        await gotovo(An_12['sec'])
        await flight_cancel(start = 'Иркутск', stop = 'Москва', distance = 40, sec = An_12['sec'])

        ########  3  ТУ-104, ТУ-114, ИЛ-18  ########
        await sleep(1)
        txt = f'{username}, во время полёта самолёт начал вибрировать, поэтому пришлось возвращаться на базу. За проявление мужества и высокой ответственности в сложившейся ситуации \
твой уровень повысился до <b>3,</b> а баланс стал равен <b>300 монетам.</b> Так давай же тогда выберем аппарат покрупнее и попробуем совершить на нём полёт! \
Но перед этим я тебе немного расскажу про них. \n\n<b>Ту-104</b> - первый реактивный двухдвигательный самолёт, сделанный в СССР. За основу разработки взяли \
бомбардировщик Ту-16. Конструктор: Д.С.Марков. Первый полёт совершил 17 июня 1955 года. \n<b>Ту-114</b> - за основу создания был взят бомбардировщик Ту-95. На борту имеет четыре турбовинтовых двигателя.\
Конструктор: Н.И. Базенков. Первый полёт совершил 15 ноября 1957. \n<b>Ил-18</b> - советский четырёхмоторный самолёт. Первый полёт был совершён 4 июля 1957 года. Конструктор: С.В.Ильюшин'
        await message.answer(txt, parse_mode='HTML')
        kb = ReplyKeyboardMarkup(resize_keyboard = True,
                                    one_time_keyboard=True)
        b1 = KeyboardButton('Ту-104 - 50 монет')
        b2 = KeyboardButton('Ту-114 - 50 монет')
        b3 = KeyboardButton('Ил-18 - 50 монет')
        kb.add(b1).add(b2).add(b3)
        await sleep(20)
        await message.answer('Все они стоят по 50 монет, какой из них ты хочешь приобрести?', reply_markup=kb) 
        await sleep(2)

@dp.message_handler(commands = ['weather'])
async def send_weather(message: types.Message):  
    rus_desk = {
        "Clear": "Ясно \U00002600",
        "Clouds": "Облачно \U00002601",
        "Rain": "Дождь \U00002614",
        "Drizzle": "Дождь \U00002614",
        "Thunderstorm": "Гроза \U000026A1",
        "Snow": "Снег \U0001F328",
        "Mist": "Туман \U0001F32B"
    }

    try:
        r = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={message.text[9::]}&appid={WEATHER_TOKEN}&units=metric&lang=ru')
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
        

@dp.message_handler(content_types = ['text'])
async def main_part(message: types.Message):
    username = message.from_user.first_name
    async def gotovo(sec):
        msg = await message.answer('Проверка документов')
        dots = '.'
        for i in range(41):
            if i % 3 == 0:
                dots = '.'
                await msg.edit_text(f'Проверка документов{dots}  ({i}%)')
            else:
                dots += '.'
                await asyncio.sleep(sec)
                await msg.edit_text(f'Проверка документов{dots}  ({i}%)')

        for i in range(41, 81):
            if i % 3 == 0:
                dots = '.'
                await msg.edit_text(f'Проверка багажей пассажиров{dots}  ({i}%)')
            else:
                dots += '.'
                await asyncio.sleep(sec)
                await msg.edit_text(f'Проверка багажей пассажиров{dots}  ({i}%)')

        for i in range(80, 101):
            if i % 3 == 0:
                dots = '.'
                await msg.edit_text(f'Посадка пассажиров{dots}  ({i}%)')
            else:
                dots += '.'
                await asyncio.sleep(sec)
                await msg.edit_text(f'Посадка пассажиров{dots}  ({i}%)')
            if i == 100:
                await msg.edit_text('Самолёт готов ко взлёту!')
    async def flight(start, stop, distance, sec):
        cht = '🛫' + '-' * (distance - 1)
        flight_process = start + '\n' + cht + '\n' + stop
        msg = await bot.send_message(message.from_user.id,
                                        f'{flight_process}')
        for i in range(1, distance):
            cht = '- ' * distance
            if i == distance - 1:
                cht = cht.split()
                cht[i] = '🛬'
                cht = ''.join(cht)
            else:
                cht = cht.split()
                cht[i] = '✈️'
                cht = ''.join(cht)
            flight_process = start + '\n' + cht + '\n' + stop
            await asyncio.sleep(sec)
            await msg.edit_text(f'{flight_process}')

    if message.text == 'Ту-104 - 50 монет':
        available.append('Ту-104')
        await message.answer('Баланс: 250 монет', reply_markup=ReplyKeyboardRemove())
        await sleep(2)
        await gotovo(Tu_104['sec'])
        await flight(Mos_Irk['start'], Mos_Irk['stop'], Mos_Irk['distance'], Tu_104['sec'])
    elif message.text == 'Ту-114 - 50 монет':
        available.append('Ту-114')
        await message.answer('Баланс: 250 монет', reply_markup=ReplyKeyboardRemove())
        await sleep(2)
        await gotovo(Tu_114['sec'])
        await flight(Mos_Xab['start'], Mos_Xab['stop'], Mos_Xab['distance'], Tu_114['sec'])
    elif message.text == 'Ил-18 - 50 монет':
        available.append('Ил-18')
        await message.answer('Баланс: 250 монет', reply_markup=ReplyKeyboardRemove())
        await sleep(2)
        await gotovo(Il_18['sec'])
        await flight(Frun_Zhuk['start'], Frun_Zhuk['stop'], Frun_Zhuk['distance'], Il_18['sec'])

    ########  4  ЯК-42, ИЛ-86, ТУ-144  ########
    await sleep(1)
    if message.text == 'Ту-104 - 50 монет' or message.text == 'Ту-114 - 50 монет' or message.text == 'Ил-18 - 50 монет':
        await message.answer(f'Спешу поздравить с удачным приземлением и повышением, ведь ты теперь на <b>4</b> уровне, а на твоём счету \
<b>400 монет.</b> А пробовал ли ты когда-нибудь совершать рейс с дозаправками? Нет?! Ну так давай исправим! По традиции \
предложу тебе пару вариантов, а дальше - дело твоё. \n\n<b>Як-42</b> — среднемагистральный трехдвигательный пассажирский самолет, который пришел \
на смену технически устаревшего Ту-134. Як-42 стал первым советским пассажирским самолетом, оснащенным турбовентиляторными двигателями с высокой \
степенью двухконтурности(степень двухконтурности - отношение расхода воздуха во внешнем контуре к расходу воздуха во внутреннем). \
Считается, что чем выше это показание, тем выше и КПД. \n<b>Ил-86</b> стал первым и самым массовым советским широкофюзеляжным пассажирским самолетом. \
Эта четырехдвигательная машина была спроектирована инженерами КБ Ильюшина. Из преимуществ можно выделить увеличенную вместительность и высокую безопасность. \
\n<b>Ту-144</b> - первый в мире сверхзвуковой самолёт, который использовался для перевозки пассажиров. Первый испытательный полёт этот советский \
лайнер совершил 31 декабря 1968 года, на два месяца раньше «Конкорда» - своего знаменитого конкурента.', parse_mode='HTML')
    await sleep(25)

    #функция дозаправки
    async def flight_dozap(start, stop, distance, sec):
        cht = '🛫' + '-' * (distance - 1)
        flight_process = start + '\n' + cht + '\n' + stop
        msg = await bot.send_message(message.from_user.id,
                                        f'{flight_process}')
        count = 0
        for i in range(1, distance):
            cht = '- ' * distance
            if i == distance - 1:
                cht = cht.split()
                cht[i] = '🛬'
                cht = ''.join(cht)
            elif i == distance // 2:
                if count == 0:
                    count += 1
                    cht = cht.split()
                    cht[i] = '✈️'
                    cht = ''.join(cht)
                    await msg.edit_text(f'{start} \n {cht} \n У самолёта осталось мало топлива! Необходимо совершить посадку! \n {stop}')
                    await sleep(2)
                    cht = '- ' * distance
                    cht = cht.split()
                    cht[i + 1] = '🛬'
                    cht = ''.join(cht)
                    await msg.edit_text(f'{start} \n{cht} \n{stop}')
                    await sleep(1)
                    cht = '- ' * distance
                    cht = cht.split()
                    cht[i + 2] = '⛽️'
                    cht = ''.join(cht)
                    x = random.randrange(7, 58)
                    while x != 101:
                        await msg.edit_text(f'{start} \n{cht} \nИдёт заправка! {x}% из 100%. \n{stop}')
                        x += 1
                    await sleep(1)
                    cht = '- ' * distance
                    cht = cht.split()
                    cht[i + 3] = '🛫'
                    cht = ''.join(cht)
                    await msg.edit_text(f'{start} \n{cht} \n{stop}')
            else:
                cht = cht.split()
                cht[i] = '✈️'
                cht = ''.join(cht)
            flight_process = start + '\n' + cht + '\n' + stop
            await asyncio.sleep(sec)
            await msg.edit_text(f'{flight_process}')

    Yak_Il_Tu = ReplyKeyboardMarkup(resize_keyboard=True,
                                    one_time_keyboard=True)
    yak = KeyboardButton('Як-42 - 100 монет')
    il = KeyboardButton('Ил-86 - 100 монет')
    tu = KeyboardButton('Ту-144 - 100 монет')
    Yak_Il_Tu.add(yak).add(il).add(tu)
    if message.text == 'Ту-104 - 50 монет' or message.text == 'Ту-114 - 50 монет' or message.text == 'Ил-18 - 50 монет':
        await message.answer('100 монет - и один из них твой!',
                             reply_markup=Yak_Il_Tu)
        await sleep(1)
    if message.text == 'Як-42 - 100 монет':
        available.append('Як-42')
        await message.answer('Баланс: 300 монет', reply_markup=ReplyKeyboardRemove())
        await gotovo(Yak_42['sec'])
        await flight_dozap(Mos_Irk['start'], Mos_Irk['stop'], Mos_Irk['distance'], Yak_42['sec'])
        await sleep(1)
    elif message.text == 'Ил-86 - 100 монет':
        available.append('Ил-86')
        await message.answer('Баланс: 300 монет', reply_markup=ReplyKeyboardRemove())
        await gotovo(Il_86['sec'])
        await flight_dozap(Mos_Irk['start'], Mos_Irk['stop'], Mos_Irk['distance'], Yak_42['sec'])
        await sleep(1)
    elif message.text == 'Ту-144 - 100 монет':
        available.append('Ту-144')
        await message.answer('Баланс: 300 монет', reply_markup=ReplyKeyboardRemove())
        await gotovo(Tu_144['sec'])
        await flight_dozap(Mos_Irk['start'], Mos_Irk['stop'], Mos_Irk['distance'], Yak_42['sec'])
        await sleep(1)

    ########  5  АН-124  АН-225  ########
    #функция возвращения на базу
    async def flight_return(start, distance, sec):
        cht = '🛫' + '-' * (distance - 1)
        flight_process = start + '\n' + cht
        msg = await bot.send_message(message.from_user.id,
                                        f'{flight_process}')
        for i in range(1, distance):
            cht = '- ' * distance
            if i == distance - 1:
                for x in range(19, -1, -1):
                    cht = '- ' * distance
                    cht = cht.split()
                    cht[x] = '✈️'
                    cht = ''.join(cht)
                    flight_process = start + '\n' + cht
                    await asyncio.sleep(sec)
                    await msg.edit_text(f'{flight_process}')
                    if x == 0:
                        cht = '- ' * distance
                        cht = cht.split()
                        cht[x] = '🛬'
                        cht = ''.join(cht)
                        flight_process = start + '\n' + cht
                        await asyncio.sleep(sec)
                        await msg.edit_text(f'{flight_process}')
            else:
                cht = cht.split()
                cht[i] = '✈️'
                cht = ''.join(cht)
                flight_process = start + '\n' + cht
                await asyncio.sleep(sec)
                await msg.edit_text(f'{flight_process}')
    
    txt = f'{username}, пассажиры чувствовали себя в полной безопасности благодаря твоей профессиональной работе. Не это ли повод для гордости и для повышения? \
Да-да, встречай <b>5</b> уровень и +200 монет в карман! Что ж, неплохо было бы и на транспортных самолётах полетать, так что выбирай один из предложенных самолётов и готовься к полёту, пока мы пригоняем его к твоему ангару. \
\n\n<b>Ан-124</b> – это тяжелый дальний транспортный самолет. Он сумел вернуть СССР передовые места в области транспортной авиации. Следует отметить, что в 1985 году \
на «Руслане» был установлен 21 мировой рекорд. А в 87-м шестого мая экипаж В.И. Терского побил старый и установил новый мировой рекорд по полетной дальности в замкнутом маршруте. \
Самолет имеет уникальное многостоечное шасси, состоящее из 24 колес. Особенностью Ан-124 является наличие двух грузовых люков: в передней и задней части самолета. \
Максимальная взлётная масса: 392т. \n<b>Ан-225 «Мечта»</b> является самым тяжёлым грузоподъёмным самолётом, когда-либо поднимавшимся в воздух. \
Максимальный взлётный вес воздушного судна составляет 640 тонн. Самолет был спроектирован в СССР и построен в 1988 году на Киевском механическом заводе. \
«Мрия» установила мировой рекорд взлётного веса и грузоподъёмности. 22 марта 1989 года Ан-225 совершил полёт с грузом 156,3 тонны, побив тем самым одновременно 110 мировых авиационных \
рекордов, что является рекордом само по себе.'
    if message.text == 'Як-42 - 100 монет' or message.text == 'Ил-86 - 100 монет' or message.text == 'Ту-144 - 100 монет':  #остэге текст чыга
        await message.answer(txt, parse_mode='HTML')
        await sleep(20)
    An_Transport = ReplyKeyboardMarkup(resize_keyboard = True, 
                                       one_time_keyboard=True)
    An_124 = KeyboardButton('Ан-124 - 200 монет')
    An_225 = KeyboardButton('Ан-225 - 200 монет')
    An_Transport.add(An_124).add(An_225)
    if message.text == 'Ту-144 - 100 монет' or message.text == 'Ту-144 - 100 монет' or message.text == 'Ту-144 - 100 монет':  #кнопкаларны чыгарырга
        await message.answer('Твой баланс равен 500 монетам. Кого?', reply_markup=An_Transport)
    if message.text == 'Ан-124 - 200 монет':
        available.append('Ан-124')
        await message.answer('Принято! Баланс: 300 монет.', reply_markup=ReplyKeyboardRemove())
        await gotovo(sec = 0.2)
        await sleep(1)
        await flight_return(start = 'Ростов-на-Дону', distance = 27, sec = 0.2)
    if message.text == 'Ан-225 - 200 монет':
        available.append('Ан-225')
        await message.answer('Принято! Баланс: 300 монет.', reply_markup=ReplyKeyboardRemove())
        await gotovo(sec = 0.2)
        await sleep(1)
        await flight_return(start = 'Ростов-на-Дону', distance = 27, sec = 0.2)

    ########  6  Бе-200  Ту-214Р  ########
    if message.text == 'Ан-124 - 200 монет' or message.text == 'Ан-225 - 200 монет':   #Ан124 хэм Ан225 тошкэч мактау
        await message.answer('Ты заслуживаешь похвалы за свою профессиональную работу, ведь столкнулся со сложными задачами, \
такими как обеспечение целостности грузов и безопасной посадки. Твой уровень: <b>6</b>, баланс: <b>550 монет.</b> Идём дальше! На очереди \
<b>Бе-200 и Ту-214Р.</b>\n\n<b>Бе-200</b> - это российский самолет-амфибия, последняя разработка ТАНТК им. Г. М. Бериева. Первый полет машина совершила в 1998 году. \
Самолет-амфибия Бе-200 может взлетать и садиться как с водной поверхности, так и с земли. Сегодня самолет-амфибия Бе-200 используется российским МЧС, одна машина построена для МЧС Азербайджана.\n\
<b>Ту-214Р</b> - разведывательный самолет, разработанный компанией Туполев на основе пассажирского Ту-214. Он оснащен средствами электронной разведки и радиолокационным оборудованием. \
Впервые полетел в 2009 году и используется Воздушно-космическими силами России.', parse_mode='HTML')
        await sleep(20)
    Pred_Planes = ReplyKeyboardMarkup(resize_keyboard = True,
                                      one_time_keyboard=True)
    Be_200 = KeyboardButton('Бе-200 - 250 монет')
    Tu_214P = KeyboardButton('Ту-214Р - 250 монет')
    Pred_Planes.add(Be_200).add(Tu_214P)
    if message.text == 'Ан-124 - 200 монет' or message.text == 'Ан-225 - 200 монет': #тэкъдим итэбез
        await message.answer('Поехали, выбирай!', reply_markup = Pred_Planes)
    
    if message.text == 'Бе-200 - 250 монет':
        available.append('Бе-200')
        await gotovo(sec = 0.2)
        await sleep(1)
        await flight_return('Иркутск', distance = 35, sec = 0.2)
    if message.text == 'Ту-214Р - 250 монет':
        available.append('Ту-214Р')
        await gotovo(sec = 0.2)
        await sleep(1)
        await flight('Новосибирск', 'Сочи', distance = 35, sec = 0.2)

    ########  7 наконец!!!  Сухой 100  МС-21 ########
    if message.text == 'Бе-200 - 250 монет' or message.text == 'Ту-214Р - 250 монет':
        await message.answer('Вот, собственно, и прилетели! Как тебе полёт? Ха-ха, я знаю, что тебе понравилось! А знаешь что тебе понравится ещё кроме <b>7</b>\
уровня и <b>700 монет</b> на балансе? \
Ну конечно же новенький Sukhoi Superjet 100 или MC-21! Прошу любить и жаловать!\n\n\
<b>Sukhoi Superjet 100</b> - гордость российской авиапромышленности, инновационная разработка, на которую правительство возлагает большие планы. \
Это региональный пассажирский самолет, разработанный компанией Сухой в сотрудничестве с иностранными партнерами. Впервые полетел в 2008 году и начал \
коммерческие полеты в 2011 году. Он предназначен для перевозки до 108 пассажиров на расстояние до 4578 км. \n\
<b>MC-21</b> расшифровывается как магистральный самолёт двадцать первого века. Именно на него рассчитывает большинство российских авиакомпаний в ближайшие годы. \
Одна из главных особенностей МС-21 - композитное крыло. Композитное крыло, говоря простыми словами, это пластик, только с некоторыми модификациями. \
Он более прочный и лёгкий, ввиду чего уменьшается масса самолёта, затраты на бензин. По основным характеристикам он совсем не уступает прославленным Boeing и Airbus в своём классе. \
Предельная лётная дальность самолёта – 6000 км, а количество пассажирских мест равно 211.', parse_mode = 'HTML')
    Last_Planes = ReplyKeyboardMarkup(resize_keyboard = True,
                                      one_time_keyboard = True)
    Sukhoi = KeyboardButton('Sukhoi Superjet 100 - 300 монет')
    MC_21 = KeyboardButton('MC-21 - 300 монет')
    Last_Planes.add(Sukhoi).add(MC_21)
    if message.text == 'Бе-200 - 250 монет' or message.text == 'Ту-214Р - 250 монет':
        await message.answer('Напоминаю, баланс: 700 монет.', reply_markup=Last_Planes)
    if message.text == 'Sukhoi Superjet 100 - 300 монет':
        available.append('Sukhoi Superjet 100')
        await message.answer('Заправляемся и полетели!', reply_markup=ReplyKeyboardRemove())
        await sleep(1)
        await gotovo(sec = 0.1)
        await sleep(0.5)
        await flight('Екатеринбург', 'Санкт-Петербург', 25, 0.1)
        await sleep(0.5)
        await message.answer('Баланс: 1000 монет. Ну что ж, уважаемый представитель молодежи. Вот и подошло к концу наше с тобой путешествие, однако я с тобой ещё не прощаюсь. \
        Теперь ты сможешь сам покупать самолёты, пролетать по новым маршрутам и узнавать больше об авиации. Всё это доступно по команде /белмимукымадым.')


    if message.text == 'MC-21 - 300 монет':
        available.append('МС-21')
        await message.answer('Заправляемся и полетели!', reply_markup=ReplyKeyboardRemove())
        await sleep(1)
        await gotovo(sec = 0.1)
        await sleep(0.5)
        await flight('Калининград', 'Пермь', 30, 0.1)
        await sleep(0.5)
        await message.answer('Баланс: 1000 монет. \nНу что ж, уважаемый представитель молодежи. Вот и подошло к концу наше с тобой путешествие, однако я с тобой ещё не прощаюсь. \
Теперь ты сможешь сам покупать самолёты, пролетать по новым маршрутам и узнавать больше об авиации. Всё это доступно по команде /белмимукымадым.')


        

if __name__ == '__main__':
    executor.start_polling(dp)

