import telebot
import os
import re
import requests

bot = telebot.TeleBot(os.environ.get('BOT_TOKEN'))

# Commands


@bot.message_handler(commands=['start'])
def test(message):
    bot.send_message(message.chat.id, 'welcome to kakabot')
    video = open('utils/yoshi.mp4', 'rb')
    bot.send_video(message.chat.id, video)


@bot.message_handler(commands=['koala'])
def fox(message):
    url = get_image_url('https://some-random-api.ml/img/koala', 'link')
    chat_id = message.chat.id
    bot.send_photo(chat_id, url)

# Auxiliary methods


def get_url(url, key):
    contents = requests.get(url).json()
    url = contents[key]
    return url


def get_image_url(url, key):
    allowed_extension = ['jpg', 'jpeg', 'png']
    file_extension = ''
    while file_extension not in allowed_extension:
        url = get_url(url, key)
        file_extension = re.search("([^.]*)$", url).group(1).lower()
    return url


bot.polling()
