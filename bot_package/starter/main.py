from bot_package.help_command import help_command, commands_list as cmd_list
from bot_package.starter import initializer
from telebot import types

bot = initializer.bot

from bot_package.other_commands import generate_password_command
from bot_package.other_commands import format_text_command
from bot_package.other_commands import cprice_command


@bot.message_handler(commands=['start'])
def start_handler(message):
    bot.send_message(message.chat.id, 'Starting...')
    bot.send_message(message.chat.id, f'Welcome to {initializer.bot_data["name"]}')


@bot.message_handler(commands=['help'])
def bot_help_command(message):
    bot.send_message(message.chat.id,
                     f'Welcome to {initializer.bot_data["name"]}\nBot version: {initializer.bot_data["version"]}')
    inline_keyboard = types.InlineKeyboardMarkup()
    for command in cmd_list.commands_list.keys():
        inline_keyboard.add(types.InlineKeyboardButton(text=f'/{command}', callback_data=command))
    inline_keyboard.add(types.InlineKeyboardButton(text='Full help list', callback_data='full_help_list'))
    bot.send_message(message.chat.id, 'What command do you need help with?', reply_markup=inline_keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    for command in cmd_list.commands_list.keys():
        if call.data == command:
            if cmd_list.commands_list[command]["arguments"] != 'none':
                bot.send_message(call.message.chat.id,
                                 f'/{command} :\n{cmd_list.commands_list[command]["description"]}\n{cmd_list.commands_list[command]["arguments"]}')
            else:
                bot.send_message(call.message.chat.id,
                                 f'/{command} :\n{cmd_list.commands_list[command]["description"]}\n')
    if call.data == 'full_help_list':
        bot.send_message(call.message.chat.id, help_command.send_full_help_list())


@bot.message_handler(commands=['generate_password'])
def call_password_generator(message):
    generate_password_command.password_generator(message)


@bot.message_handler(commands=['format_text'])
def call_text_format(message):
    format_text_command.text_formatter(message)


@bot.message_handler(commands=['cprice'])
def call_cprice_command(message):
    cprice_command.crypto_price(message)


if __name__ == '__main__':
    bot.polling(none_stop=True, interval=0)
