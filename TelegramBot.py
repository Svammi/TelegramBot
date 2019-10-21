import requests
import telebot
import pprint

TOKEN = '876764820:AAG6CgmuzPhef3fv8uemTjW2wLNU1NE7oEU'
TOKEN_WEATHER = '6ef6f2d12f81546bec39e6ab15f2c89e' #API keys in openweathermap.org
bot = telebot.TeleBot(TOKEN)
'''
# Обработка комманды от пользователя
@bot.message_handler(commands=['city'])
def send_welcome(message):
    bot.reply_to(message, 'Для какого города будем смотреть погоду?')
'''
@bot.message_handler(regexp = 'Привет')
def uppper(message):
    bot.reply_to(message, 'Привет, я бот, который будет уведомлять тебя о погоде в твоем городе. Для какого города будем смотреть погоду?')

def search_weather(city = 'city'):
    r = requests.get("http://api.openweathermap.org/data/2.5/weather", params={'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': TOKEN_WEATHER}) #'q': city,
    data = r.json()
    return data

@bot.message_handler(func = lambda mesage:True)
def uppper(message):
    weather = search_weather(message.text)
    message_about_weather = 'Температура ' + str(weather['main']['temp']) + 'C' + '\n' + \
                            'Облачность - ' + str(weather['weather'][0]['description']) + '\n' + \
                            'Скорость ветра - ' + str(weather['wind']['speed']) + 'м/с'
    bot.reply_to(message, message_about_weather)

bot.polling()# запускаем бота для прослушивания