import re
from bot import WhatssAppBot

bot = WhatssAppBot("James")
bot.train_bot()
bot.start('Eric')
bot.greetings(['Bot: Hello! I am a robot and I just entered the group!','Bot: Use :: to speak with me!'])
last_message = ''
try:
    while True:
        text = bot.listen()
        if text != last_message and re.match(R'^::', text):
            last_message = text
            text = text.replace('::', '')
            text = text.lower()
            bot.responde(text)
except KeyboardInterrupt:
    print("Stopping James Robot...")
