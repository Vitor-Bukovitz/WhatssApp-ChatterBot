import re
from bot import WhatssAppBot

bot = WhatssAppBot("James")
bot.train_bot()
bot.train_bot2()
bot.start('[Name of the contact]')
bot.greetings(['Bot James: Hello! I am a robot and I just entered the group!','Bot James: Use "::" to speak with me!'])
last_message = ''
try:
    while True:
        text = bot.listen()
        if text != last_message and re.match(R'^::', text):
            last_message = text
            text = text.replace('::', '')
            text = text.lower()
            bot.response(text)
except KeyboardInterrupt:
    print("Stopping James Robot...")
