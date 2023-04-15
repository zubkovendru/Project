import requests
from bs4 import BeautifulSoup as b
import telebot
import datetime
from datetime import date
from telebot import types
import random
from googletrans import Translator
import json

translator = Translator()

bot = telebot.TeleBot('6139415345:AAGonPJU-HHKSjOSkdgTDYCpz-q8axdycCI')

URL = 'https://стопкоронавирус.рф/'
API = "94b88c7b0f17917119dc61bfa1545722"

def gosp_people(url):
    r = requests.get(url)
    soup = b(r.text, 'html.parser')
    green = soup.find_all('div', class_='cv-countdown__item-value _accent')
    green_t = green[0].text
    return green_t

def green_people(url):
    r = requests.get(url)
    soup = b(r.text, 'html.parser')
    green = soup.find_all('div', class_='cv-countdown__item-value _accent-green')
    green_t = green[0].text
    return green_t


def ill_people(url):
    r = requests.get(url)
    soup = b(r.text, 'html.parser')
    green = soup.find_all('div', class_='cv-countdown__item-value _accent')
    green_t = green[1].text
    return green_t


@bot.message_handler(commands=['we'])
def starter(message):
    bot.send_message(message.chat.id, "Привет, я бот для получения информации о погоде. Введите название города:")
    bot.register_next_step_handler(message, wee)


@bot.message_handler(regexp='[we]')
def wee(message):
    city = message.text.strip().lower()
    res = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric")
    if res.status_code == 200:
        data = json.loads(res.text)
        temperature = data["main"]["temp"]
        bot.reply_to(message, f"Сейчас в городе {temperature} градусов")
        image = "солнышко.png" if temperature >= 17.5 else "пасмурно.jpg"
        file = open("./" + image, "rb")
        bot.send_photo(message.chat.id, file)
    else:
        bot.send_message(message.chat.id, "Введите город!")

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("🔶 Рандомное число")
    item2 = types.KeyboardButton("🕓 Время")
    item3 = types.KeyboardButton("🛠 Создатель")
    item4 = types.KeyboardButton("📄 id")
    item5 = types.KeyboardButton("🎂 Сколько мне лет")
    item6 = types.KeyboardButton("🦠 Коронавирус в РФ")
    item7 = types.KeyboardButton("Погода")
    markup.add(item1, item2, item3, item4, item5, item6, item7)
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}!', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.chat.type == 'private':
        if message.text == '🔶 Рандомное число':
            bot.send_message(message.chat.id, f'Ваше число: {random.randint(0, 1000000000)}', parse_mode='html')
        elif message.text == '🕓 Время':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            it0 = types.KeyboardButton("🇷🇺 Санкт-Петербург")
            it1 = types.KeyboardButton("🗽 Нью-Йорк")
            it2 = types.KeyboardButton("🏯 Токио")
            it3 = types.KeyboardButton("🗼 Париж")
            it4 = types.KeyboardButton("⬅ Назад")

            markup.add(it0, it1, it2, it3, it4)
            bot.send_message(message.chat.id, '🕓 Время', reply_markup=markup)

        elif message.text == '🇷🇺 Санкт-Петербург':
            time_now = datetime.datetime.now()
            bot.send_message(message.chat.id, f"Сейчас в Санкт-Петербурге {str(time_now.hour)} часов " f"{str(time_now.minute)} минут и " f"{str(time_now.second)} секунд", parse_mode='html')

        elif message.text == '🗽 Нью-Йорк':
            time_now = datetime.datetime.now()
            time_change = datetime.timedelta(hours=8)
            new_time = time_now - time_change
            bot.send_message(message.chat.id, f"Сейчас в Нью-Йорке {str(new_time.hour)} часов " f"{str(new_time.minute)} минут и " f"{str(new_time.second)} секунд", parse_mode='html')

        elif message.text == '🏯 Токио':
            time_now = datetime.datetime.now()
            time_change = datetime.timedelta(hours=6)
            new_time = time_now + time_change
            bot.send_message(message.chat.id, f"Сейчас в Токио {str(new_time.hour)} часов " f"{str(new_time.minute)} минут и " f"{str(new_time.second)} секунд", parse_mode='html')

        elif message.text == '🗼 Париж':
            time_now = datetime.datetime.now()
            time_change = datetime.timedelta(hours=2)
            new_time = time_now - time_change
            bot.send_message(message.chat.id, f"Сейчас в Париже {str(new_time.hour)} часов " f"{str(new_time.minute)} минут и " f"{str(new_time.second)} секунд", parse_mode='html')

        elif message.text == '🦠 Коронавирус в РФ':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("🤒 Госпитализировано")
            item2 = types.KeyboardButton("💪 Выздоровело")
            item3 = types.KeyboardButton("😷 Заболело")
            item4 = types.KeyboardButton("⬅ Назад")

            markup.add(item1, item2, item3, item4)
            bot.send_message(message.chat.id, '🦠 Коронавирус в РФ', reply_markup=markup)

        elif message.text == '🤒 Госпитализировано':
            bot.send_message(message.chat.id, gosp_people(URL))

        elif message.text == '💪 Выздоровело':
            bot.send_message(message.chat.id, green_people(URL))

        elif message.text == '😷 Заболело':
            bot.send_message(message.chat.id, ill_people(URL))

        elif message.text == '⬅ Назад':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("🔶 Рандомное число")
            item2 = types.KeyboardButton("🕓 Время")
            item3 = types.KeyboardButton("🛠 Создатель")
            item4 = types.KeyboardButton("📄 id")
            item5 = types.KeyboardButton("🎂 Сколько мне лет")
            item6 = types.KeyboardButton("🦠 Коронавирус в РФ")
            item7 = types.KeyboardButton("Погода")
            markup.add(item1, item2, item3, item4, item5, item6, item7)
            bot.send_message(message.chat.id, '⬅ Назад', reply_markup=markup)

        elif message.text == '🛠 Создатель':
            bot.send_message(message.chat.id, 'Andrey Zubkov', parse_mode='html')

        elif message.text == 'Погода':
            starter(message)

        elif message.text == '📄 id':
            bot.send_message(message.chat.id, f"Твой ID: <u>{message.from_user.id}</u>", parse_mode='html')

        elif message.text == '🎂 Сколько мне лет':
            today_date = date.today()
            bot_birthday = date(2023, 2, 4)
            bot_years = today_date - bot_birthday
            bot.send_message(message.chat.id, f"Мне {bot_years}")


bot.polling(none_stop=True)
