from bot_package.starter.main import bot
from bot_package import extras


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
