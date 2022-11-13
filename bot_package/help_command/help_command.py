from bot_package.help_command import commands_list as cmd_list
from bot_package.starter.initializer import bot
from bot_package.starter import initializer
from telebot import types

separate = '-' * 30


def send_full_help_list() -> str:
    message_returned = 'Full help list:\n'
    for command in cmd_list.commands_list.keys():
        message_returned += f'{separate}\n/{command}\n{cmd_list.commands_list[command]["description"]}\n'
        if cmd_list.commands_list[command]["arguments"] != 'none':
            message_returned += f'{cmd_list.commands_list[command]["arguments"]}\n'
    message_returned += '\n\nSupport: https://discord.gg/23mrnTkTX4'
    return message_returned


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
        bot.send_message(call.message.chat.id, send_full_help_list())
