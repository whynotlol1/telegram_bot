from bot_package.text_files.read_files import read_file as read
from telebot import TeleBot


bot_data = {
    "version": "v1.0.2",
    "name": "Telegram Utils Bot"
}

token = read("token.txt")

bot = TeleBot(token=token)
