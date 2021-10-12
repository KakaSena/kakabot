import telebot
import os
import re
import requests

bot = telebot.TeleBot(os.environ.get('BOT_TOKEN'))

# Commands


@bot.message_handler(commands=['start'])

def test(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, 'welcome to kakabot')
    video = open('utils/yoshi.mp4', 'rb')
    bot.send_video(chat_id, video)
    audio = open('utils/yoshi-audio.mp3', 'rb')
    bot.send_audio(chat_id, audio)


@bot.message_handler(commands=['koala'])
def fox(message):
    url = get_image_url('https://some-random-api.ml/img/koala', 'link')
    chat_id = message.chat.id
    bot.send_photo(chat_id, url)

@bot.message_handler(commands=['bop'])
def bop(message):
    url = get_image_url('https://random.dog/woof.json','url')
    chat_id = message.chat.id
    bot.send_photo(chat_id,url)


@bot.message_handler(commands=["ping"])
def on_ping(message):
    bot.reply_to(message, "Still alive and kicking!")


#Forbidden Commands - By Ja1

@bot.message_handler(commands=["destroy"])
def destroy(message):
    for x in range(42):
        chat_id = message.chat.id
        bot.send_message(chat_id, 'welcome to kakabot')
        video = open('utils/yoshi.mp4', 'rb')
        bot.send_video(chat_id, video)
        audio = open('utils/yoshi-audio.mp3', 'rb')
        bot.send_audio(chat_id, audio)

@bot.message_handler(commands=['meme'])
def bop(meme):
    url = get_image_url('https://some-random-api.ml/meme.json','url')
    chat_id = message.chat.id
    bot.send_photo(chat_id,url)


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
