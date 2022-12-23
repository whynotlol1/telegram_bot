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


def check(message):
    global correct_password
    password_guess = message.text[0:10]
    print(password_guess)
    if password_guess == correct_password:
        bot.send_message(message.chat.id, 'You guessed the password!')
        return
    else:
        bot.send_message(message.chat.id, 'You didn`t guess the password.')
        message_text = ''
        for symbol in password_guess:
            if symbol in correct_password and password_guess.index(symbol) == correct_password.index(symbol):
                message_text += symbol
            else:
                message_text += '*'
        if len(message_text) < 10:
            message_text += '*' * (10 - len(message_text))
        if message_text != '**********':
            message_text += '\n- these are the symbols you guessed correctly.'
            bot.send_message(message.chat.id, message_text)
        msg = bot.send_message(message.chat.id, 'Try again:')
        bot.register_next_step_handler(msg, guess_password)


def guess_password(message):
    global correct_password
    if message.text == 'stop':
        bot.send_message(message.chat.id, 'Stopping the game...')
        return
    else:
        check(message)
