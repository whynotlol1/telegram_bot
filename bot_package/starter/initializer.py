from bot_package.text_files.read_files import read_first_line as read_file
from telebot import TeleBot


bot_data = {
    "version": "v1.3",
    "name": "Telegram Utils Bot"
}

token = read_file("token.txt")

bot = TeleBot(token=token)
