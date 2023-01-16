# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 12:06:58 2023

@author: Sh_Jurayeff
"""
from transliterate import to_cyrillic, to_latin 
import telebot
TOKEN="5774021711:AAF7xvG-Gb_3YyMg-jzCHDLwjxZQM0LvGrE"
bot = telebot.TeleBot(TOKEN, parse_mode=None) # You can set parse_mode by default. HTML or MARKDOWN

@bot.message_handler(commands=['start'])
def send_welcome(message):
    javob="Assalomu alaykum , Xush kelibsiz."
    javob+="\nMatn kiriting: "
    bot.reply_to(message, javob )
    

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    msg=message.text
    if msg.isascii():
        javob=to_cyrillic(msg)
    else:
        javob=to_latin(msg)
    bot.reply_to(message, javob)

bot.infinity_polling()



































