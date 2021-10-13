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


@bot.message_handler(commands=['bop'])
def bop(message):
    url = get_image_url('https://some-random-api.ml/animal/dog', 'image')
    chat_id = message.chat.id
    bot.send_photo(chat_id, url)


@bot.message_handler(commands=['cat'])
def cat(message):
    url = get_image_url('https://some-random-api.ml/animal/cat', 'image')
    chat_id = message.chat.id
    bot.send_photo(chat_id, url)


@bot.message_handler(commands=['koala'])
def koala(message):
    url = get_image_url('https://some-random-api.ml/img/koala', 'link')
    chat_id = message.chat.id
    bot.send_photo(chat_id, url)


@bot.message_handler(commands=['bird'])
def bird(message):
    url = get_image_url('https://some-random-api.ml/animal/birb', 'image')
    chat_id = message.chat.id
    bot.send_photo(chat_id, url)


@bot.message_handler(commands=['kangaroo'])
def kangaroo(message):
    url = get_image_url('https://some-random-api.ml/animal/kangaroo', 'image')
    chat_id = message.chat.id
    bot.send_photo(chat_id, url)


@bot.message_handler(commands=['panda'])
def panda(message):
    url = get_image_url('https://some-random-api.ml/animal/red_panda', 'image')
    chat_id = message.chat.id
    bot.send_photo(chat_id, url)


@bot.message_handler(commands=['raccoon'])
def raccoon(message):
    url = get_image_url('https://some-random-api.ml/animal/raccoon', 'image')
    chat_id = message.chat.id
    bot.send_photo(chat_id, url)


@bot.message_handler(commands=['fox'])
def fox(message):
    url = get_image_url('https://some-random-api.ml/animal/fox', 'image')
    chat_id = message.chat.id
    bot.send_photo(chat_id, url)


@bot.message_handler(commands=['help'])
def command_help(message):
    bot.send_message(message.chat.id, "🤖 /start - welcome message\n"
                     "🐨 /koala - random koala image\n"
                     "🐶 /bop - random dog image\n"
                     "🐱 /cat - random cat image\n"
                     "🦘 /kangaroo - random kangaroo image\n"
                     "🐼 /panda - random panda image\n"
                     "🦊 /fox - random fox image\n"
                     "🦝 /raccoon - random raccoon image\n"
                     "🐦 /bird - random bird image\n"
                     "😜 /meme - random meme image\n")


@bot.message_handler(commands=["ping"])
def on_ping(message):
    bot.reply_to(message, "Still alive and kicking!")


# Forbidden Commands - By Ja1

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
def bop(message):
    url = get_image_url('https://some-random-api.ml/meme', 'image')
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
