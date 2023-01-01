from bot_package.text_files.__read_files__ import read_all_lines as read_everything
from bot_package.text_files.__read_files__ import read_first_line as read_token
from telebot import TeleBot


bot_data = {
    "version": "v1.3",
    "name": "Telegram Utils Bot",
    "contacts": read_everything("contacts.txt")
}

token = read_token("token.txt")

bot = TeleBot(token=token)
