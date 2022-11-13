from bot_package.starter.initializer import bot
from bot_package import extras


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
