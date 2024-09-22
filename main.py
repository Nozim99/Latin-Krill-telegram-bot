from transliterate import to_cyrillic, to_latin
import telebot

TOKEN = "7682704978:AAEs8Ao0kiLbg8qK5ARdcHA5E2z7ujLwSJM"

bot = telebot.TeleBot(TOKEN, parse_mode=None)


@bot.message_handler(commands=["start"])
def send_welcome(message):
    javob = "Assalomu Alaykum, Xush kelibsiz!"
    javob += "\nMatn kiriting:"
    bot.reply_to(message, javob)


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    msg = message.text

    javob = (lambda: to_cyrillic(msg) if msg.isascii() else to_latin(msg))()

    bot.reply_to(message, javob)

bot.infinity_polling()
