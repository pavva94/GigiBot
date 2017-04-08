import telebot
import re
import random

bot = telebot.TeleBot(token='367324257:AAGaPsh2OQB3QkwFeJ26U_dtfO3aW4z7cGc')

gnappate = [
    'insulta dotto',
    'Mai una gioia',
    'Ciao',
    'piu\' gigi per tutti',
    'Non capire is the new non capire',
    'Aaaaaawww!',
]

def minestra():
    return open('minestra.png', 'rb')


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Hai voglia di qualcosa?")


@bot.message_handler(regexp=re.compile(r'gigi', re.I))
def ho_fame(message):
    bot.send_message(message.chat.id, 'Andiamo al centro insieme?')
    bot.send_photo(message.chat.id, minestra())


@bot.message_handler(regexp=re.compile(r'buono', re.I))
def buono(message):
    bot.send_message(message.chat.id, 'Le cose più buone sono quelle diy, con lo zenzero e la carota viola.')
    bot.send_photo(message.chat.id, minestra())


@bot.message_handler(regexp=re.compile(r'dotto', re.I))
def fallito(message):
    bot.send_message(message.chat.id, 'insulta dotto')


@bot.message_handler(regexp=re.compile(r'acaso', re.I))
def fallito(message):
    bot.send_message(message.chat.id, random.choice(gnappate))

bot.polling()
