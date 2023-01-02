from bot_package.starter.initializer import bot
import gtts
import os


def text_to_speech(message):
    bot.send_message(message.chat.id, 'Enter text to convert to speech (first word will be deleted):')
    bot.register_next_step_handler(message, text_to_speech_step_2)


def text_to_speech_step_2(message):
    text = message.text.split(' ', 1)[1]
    tts = gtts.gTTS(text)
    tts.save('message.mp3')
    audio = open('message.mp3', 'rb')
    bot.send_audio(message.chat.id, audio)
    os.remove('message.mp3')
