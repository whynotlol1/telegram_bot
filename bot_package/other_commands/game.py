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
    bot.send_message(message.chat.id, 'To stop the game, type "stop". There are 10 symbols in the password.')
    msg = bot.send_message(message.chat.id, 'Guess the password:')
    bot.register_next_step_handler(msg, guess_password)


def wrong_password(message, text: str) -> None:
    global correct_password
    bot.send_message(message.chat.id, 'Wrong password, try again.')
    message_text = 'There are some tips:\n'
    for symbol in text:
        if symbol in correct_password and text.index(symbol) == correct_password.index(symbol):
            message_text += symbol
        else:
            message_text += '*'
    if len(message_text) < 10:
        message_text += '*' * (10 - len(message_text))
    message_text += '\n- these are the symbols you guessed correctly.'
    message_text += f'\n("*" - the symbols left to guess.)'
    bot.send_message(message.chat.id, message_text)
    message_text += f'\n{"-"*100}\nAnd these are the symbols you guessed, however they must be in the other places:\n'
    for symbol in text:
        if symbol in correct_password and text.index(symbol) != correct_password.index(symbol):
            message_text += f'"{symbol}"; '
    bot.send_message(message.chat.id, message_text)
    msg = bot.send_message(message.chat.id, 'Try again:')
    bot.register_next_step_handler(msg, guess_password)


def guess_password(message):
    global correct_password
    if message.text == 'stop':
        bot.send_message(message.chat.id, 'Stopping the game...')
        return
    if len(message.text) == 10:
        if message.text == correct_password:
            bot.send_message(message.chat.id, 'You guessed the password!')
            return
        else:
            wrong_password(message.text)
    elif len(message.text) > 10:
        if message.text[0:11] == correct_password:
            bot.send_message(message.chat.id, 'You guessed the password!')
            return
        else:
            wrong_password(message.text[0:11])

        bot.send_message(message.chat.id, 'The password must contain 10 symbols.')
        msg = bot.send_message(message.chat.id, 'Try again:')
        bot.register_next_step_handler(msg, guess_password)
