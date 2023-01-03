from bot_package.starter.initializer import bot
from deep_translator import MyMemoryTranslator
from deep_translator import exceptions


def translate(message):
    msg = bot.send_message(message.chat.id, 'Please, enter the text you want to translate')
    bot.register_next_step_handler(msg, translate_step_2)


def translate_step_2(message):
    msg = bot.send_message(message.chat.id, 'Please, enter the languages you want the text to be translated to and from')
    text = message.text
    bot.register_next_step_handler(msg, translate_step_3, text)


def translate_step_3(message, text):
    languages = message.text.split(' ')
    try:
        bot.send_message(message.chat.id, f'Result:\n{MyMemoryTranslator(source=languages[0], target=languages[1]).translate(text)}')
    except exceptions.LanguageNotSupportedException:
        bot.send_message(message.chat.id, 'Seems like you entered the languages incorrectly. Please, try again!')
