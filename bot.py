import telebot

TOKEN = "8026121784:AAGAdmFxiay4fnTxRSIfMtImX6OJEzLJJAc"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Привіт! Я буду повідомляти про великі покупки криптовалют!")

bot.polling()
