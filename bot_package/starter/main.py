from bot_package.other_commands import generate_password_command
from bot_package.other_commands import format_text_command
from bot_package.other_commands import translate_command
from bot_package.other_commands import cprice_command
from bot_package.help_command import help_command
from bot_package.starter import initializer
from telebot import types

bot = initializer.bot


@bot.message_handler(commands=['start'])
def start_handler(message):
    contact_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    contact_keyboard.add(types.KeyboardButton(text="Contacts"))
    bot.send_message(message.chat.id, 'Starting...')
    bot.send_message(message.chat.id, f'Welcome to {initializer.bot_data["name"]}', reply_markup=contact_keyboard)


@bot.message_handler(commands=['help'])
def call_bot_help_command(message):
    help_command.bot_help_command(message)


@bot.message_handler(commands=['generate_password'])
def call_password_generator(message):
    generate_password_command.password_generator(message)


@bot.message_handler(commands=['format_text'])
def call_text_format(message):
    format_text_command.text_formatter(message)


@bot.message_handler(commands=['cprice'])
def call_cprice_command(message):
    cprice_command.crypto_price(message)


@bot.message_handler(commands=['translate'])
def call_translate_command(message):
    translate_command.translate(message)


@bot.message_handler(content_types=['text'])
def text_handler(message):
    if message.text == 'Contacts':
        bot.send_message(message.chat.id, initializer.bot_data['contacts'])


if __name__ == '__main__':
    bot.polling(none_stop=True, interval=0)
    print('Bot is running...')
