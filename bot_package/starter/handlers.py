from bot_package.starter.initializer import bot
from telebot import types


def text_handler(message):
    markup = types.InlineKeyboardMarkup()
    item1 = types.InlineKeyboardButton("Get help", callback_data='help')
    item2 = types.InlineKeyboardButton("Just chat with the bot", callback_data='other')
    markup.add(item1, item2)
    bot.send_message(message.chat.id, 'Sorry, bot does not understand you. Could please specify your request?',
                     reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data == 'help':
        bot.send_message(call.message.chat.id, 'You should use /help command to get help, '
                                               'please do not use commands without "/"')
    elif call.data == 'other':
        bot.send_message(call.message.chat.id, 'Though it is not a problem, but please do not send useless messages to the bot!')
