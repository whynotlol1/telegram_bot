from bot.help_command import help_command, commands_list as cmd_list
from bot.starter import initializer
from telebot import types
from bot import extras
import secrets
import string

bot = initializer.bot


@bot.message_handler(commands=['start'])
def start_handler(message):
    bot.send_message(message.chat.id, 'Starting...')
    bot.send_message(message.chat.id, f'Welcome to {initializer.bot_data["name"]}')


@bot.message_handler(commands=['help'])
def bot_help_command(message):
    bot.send_message(message.chat.id, f'Welcome to {initializer.bot_data["name"]}\nBot version: {initializer.bot_data["version"]}')
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
                bot.send_message(call.message.chat.id, f'/{command} :\n{cmd_list.commands_list[command]["description"]}\n{cmd_list.commands_list[command]["arguments"]}')
            else:
                bot.send_message(call.message.chat.id, f'/{command} :\n{cmd_list.commands_list[command]["description"]}\n')
    if call.data == 'full_help_list':
        bot.send_message(call.message.chat.id, help_command.send_full_help_list())


@bot.message_handler(commands=['generate_password'])
def password_generator(message):
    msg = bot.send_message(message.chat.id, 'How many characters do you want your password(s) to be?')
    bot.register_next_step_handler(msg, password_generator_step_2)


def password_generator_step_2(message):
    try:
        char_limit = int(message.text)
        msg = bot.send_message(message.chat.id, 'How many passwords do you want to generate?')
        bot.register_next_step_handler(msg, password_generator_step_3, char_limit)
    except IndexError:
        bot.send_message(message.chat.id, 'Invalid argument. Please try again.')


def password_generator_step_3(message, char_limit):
    try:
        passwords_limit = int(message.text)
        for _ in range(passwords_limit):
            alphabet = string.ascii_letters + string.digits + '_-.'
            password = ''.join(secrets.choice(alphabet) for _ in range(char_limit))
            bot.send_message(message.chat.id, f'Password generated: {password}')
    except IndexError:
        bot.send_message(message.chat.id, 'Invalid argument. Please try again.')


@bot.message_handler(commands=['format_text'])
def text_formatter(message):
    msg = bot.send_message(message.chat.id, 'What text do you want to format?')
    bot.register_next_step_handler(msg, text_formatter_step_2)


def text_formatter_step_2(message):
    try:
        text = message.text
        send = extras.format_text(text)
        bot.send_message(message.chat.id, f'Result: {send}')
    except IndexError:
        bot.send_message(message.chat.id, 'Invalid argument. Please try again.')


@bot.message_handler(commands=['cprice'])
def crypto_price(message):
    msg = bot.send_message(message.chat.id, 'What crypto do you want to check?')
    bot.register_next_step_handler(msg, crypto_price_step_2)


def crypto_price_step_2(message):
    try:
        crypto = message.text
        price = extras.get_crypto_price(crypto)
        bot.send_message(message.chat.id, f'Current price of {crypto}: ${extras.to_fixed(float(price), 2)}')
    except IndexError:
        bot.send_message(message.chat.id, 'Please enter a valid crypto name.')


if __name__ == '__main__':
    bot.polling(none_stop=True, interval=0)
