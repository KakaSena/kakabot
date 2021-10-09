import telebot  # pip install pyTelegramBotAPI

bot = telebot.TeleBot(environ.get('BOT_TOKEN'))


@bot.message_handler(commands=['oi'])
def test(message):
    bot.send_message(message.chat.id, 'oi')


bot.polling()
