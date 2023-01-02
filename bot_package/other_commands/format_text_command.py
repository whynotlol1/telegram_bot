from bot_package.starter.initializer import bot


def format_text(text: str) -> str:
    symbols = [',', '!', '?', '.', ':', ';']
    text_to_be_formatted = []
    for i in text:
        text_to_be_formatted.append(i)
    text_returned = ''
    for i in range(len(text_to_be_formatted)):
        try:
            if i == 0 or (text_to_be_formatted[i - 2] == '.' and text_to_be_formatted[i - 1] == ' '):
                text_returned += text_to_be_formatted[i].capitalize()
            elif i + 1 < len(text_to_be_formatted) and text_to_be_formatted[i] == ' ' and text_to_be_formatted[i + 1] in symbols:
                text_returned += text_to_be_formatted[i + 1]
                text_to_be_formatted[i + 1] = None
            else:
                text_returned += text_to_be_formatted[i]
        except TypeError:
            pass
    return text_returned


def text_formatter(message):
    msg = bot.send_message(message.chat.id, 'What text do you want to format?')
    bot.register_next_step_handler(msg, text_formatter_step_2)


def text_formatter_step_2(message):
    try:
        text = message.text
        send = format_text(text)
        bot.send_message(message.chat.id, f'Result: {send}')
    except IndexError:
        bot.send_message(message.chat.id, 'Invalid argument. Please try again.')
