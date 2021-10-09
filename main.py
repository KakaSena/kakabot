import telebot  # pip install pyTelegramBotAPI
import os

bot = telebot.TeleBot(os.environ.get('BOT_TOKEN'))


@bot.message_handler(commands=['oi'])
def test(message):
    bot.send_message(message.chat.id, 'oi')


print("Hello, World!")
bot.polling()
print("Hello, World!2")
