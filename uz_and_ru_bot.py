"""
27-dars davomi va tugadi. Telegramdagi uz and ru botning ko'dlari.
Created on Thu Oct  2 22:11:56 2025
@author: Sherjahongir.
"""

from transliterate import to_cyrillic, to_latin
import telebot

TOKEN = '7339638599:AAFkZnANjRl_VEZsDv6swR_C20UxRA4JvnQ'
bot = telebot.TeleBot(TOKEN, parse_mode=None)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    javob = "Assalomu alaykum, Xush kelibsiz!"
    javob += "\n\nRus so'zlarni va matnlarni O'zbek alifbosiga"
    javob += "\nO'zbek so'zlarni va matnlarni Rus alifbosiga o'giraman"
    javob += "\n\nHaydarova S.A ustoz"
    javob += "\nIstalgan tilda matn kiriting:"
    bot.reply_to(message, javob)
    
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    msg = message.text
    javob = lambda msg: to_cyrillic(msg) if msg.isascii() else to_latin(msg)
# Yuqoridagi lamda usul bu qisqaroq usul, pastidagi esa ham shu vazifani 
# bajaradi ammo uzunroq.
    # if msg.isascii():
    #     javob = to_cyrillic(msg)
    # else:
    #     javob = to_latin(msg)
    bot.reply_to(message, javob(msg))
    
bot.polling()




