from bot_package.starter.main import bot
import secrets
import string


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
