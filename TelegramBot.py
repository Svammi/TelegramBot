import requests
import telebot

TOKEN = '876764820:AAG6CgmuzPhef3fv8uemTjW2wLNU1NE7oEU'
bot = telebot.TeleBot(TOKEN)


#возвращает полученной сообщение в capselocke
@bot.message_handler(func=lambda message:True)#декоратор????
def uppper(message): # особенность питона 3.5 - аннотации типов, которые позволяют определить тип переменной - что позволяет подсказывать какие методы есть у данной переменной
    bot.reply_to(message, message.text.upper())

bot.polling()# запускаем бота для прослушивания