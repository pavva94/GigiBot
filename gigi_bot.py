# coding: utf-8
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

gigi = [
    'Andiamo al noce?',
    'Andiamo al centro insieme?',
    'Chiama il ciccione!',
    'Omar di merda..'
]

def minestra():
    return open('minestra.png', 'rb')

@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message, "Secondo te ti dovrei aiutare?")


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Hai voglia di qualcosa?")


@bot.message_handler(regexp=re.compile(r'gigi', re.I))
def ho_fame(message):
    bot.send_message(message.chat.id, random.choice(gigi))
    # bot.send_photo(message.chat.id, minestra())


@bot.message_handler(regexp=re.compile(r'buono', re.I))
def buono(message):
    bot.send_message(message.chat.id, 'NO')
    bot.send_photo(message.chat.id, minestra())


@bot.message_handler(regexp=re.compile(r'dotto', re.I))
def fallito(message):
    bot.send_message(message.chat.id, 'DottoDimmerda')


@bot.message_handler(regexp=re.compile(r'acaso', re.I))
def fallito(message):
    bot.send_message(message.chat.id, random.choice(gnappate))

bot.polling()
