from bot_package.starter.initializer import bot
from random import choice
import string


def password_generator() -> str:
    password: str = ''
    for _ in range(10):
        password += choice(string.ascii_letters + string.digits + '-_.')
    return password


correct_password = ''


def game_realization(message):
    bot.send_message(message.chat.id, 'Starting "guess the password" game...')
    global correct_password
    correct_password = password_generator()
    print(correct_password)
    bot.send_message(message.chat.id, 'To stop the game, type "stop". There are 10 digits in the password.')
    msg = bot.send_message(message.chat.id, 'Guess the password:')
    bot.register_next_step_handler(msg, guess_password)


def guess_password(message):
    if message.text == 'stop':
        bot.send_message(message.chat.id, 'Stopping the game...')
        return
    if message.text == correct_password:
        bot.send_message(message.chat.id, 'You guessed the password!')
        return
    else:
        bot.send_message(message.chat.id, 'Wrong password, try again.')
        bot.send_message(message.chat.id, 'There are some tips:')
        message_text = ''
        for symbol in message.text:
            if symbol not in correct_password:
                message_text += f'"{symbol}" is not a correct symbol.\n'
            else:
                message_text += f'"{symbol}" is a correct symbol. But it might be in the wrong place\n'
        bot.send_message(message.chat.id, message_text)
        msg = bot.send_message(message.chat.id, 'Try again:')
        bot.register_next_step_handler(msg, guess_password)
