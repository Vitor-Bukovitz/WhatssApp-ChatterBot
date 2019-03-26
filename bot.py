#!usr/bin/env python3
import os 
import time
import re
import chatterbot
from chatterbot.trainers import ListTrainer 
from chatterbot import ChatBot
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from chatterbot.trainers import ChatterBotCorpusTrainer

class WhatssAppBot:
    dir_path = os.getcwd()
    def __init__(self, bot_name):
        self.bot = ChatBot(
            bot_name,
            storage_adapter='chatterbot.storage.SQLStorageAdapter',
            logic_adapters=[
                'chatterbot.logic.MathematicalEvaluation',
                'chatterbot_weather.WeatherLogicAdapter',
                'chatterbot.logic.BestMatch',
                'chatterbot.logic.TimeLogicAdapter'
            ],
            database_uri='sqlite:///database.sqlite3'
        )
        self.driver = webdriver.Firefox()
    def start(self,contact_name):
        self.driver.get("https://web.whatsapp.com/")
        self.driver.implicitly_wait(10)
        time.sleep(20)
        self.search_box = self.driver.find_element_by_class_name('jN-F5')
        self.search_box.send_keys(contact_name)
        time.sleep(2)
        self.contact = self.driver.find_element_by_xpath('//span[@title = "{}"]'.format(contact_name))
        self.contact.click()
        time.sleep(2)
    def greetings(self, inicial_sentence):
        self.message_box = self.driver.find_element_by_class_name('_2S1VP')
        if type(inicial_sentence) == list:
            for sentence in inicial_sentence:
                self.message_box.send_keys(sentence)
                time.sleep(1)
                self.send_button = self.driver.find_element_by_class_name('_35EW6')
                self.send_button.click()
                time.sleep(1)
        else:
            return False

    def listen(self):
        post = self.driver.find_elements_by_class_name('_3_7SH')
        last = len(post) - 1
        text = post[last].find_element_by_css_selector('span.selectable-text').text
        return text

    def response(self, text):
        response = self.bot.get_response(text)
        response = str(response)
        response = 'Bot James: ' + response
        self.message_box = self.driver.find_element_by_class_name('_2S1VP')
        self.message_box.send_keys(response)
        time.sleep(1)
        self.send_button = self.driver.find_element_by_class_name('_35EW6')
        self.send_button.click()

    def train_bot(self):
         trainer = ListTrainer(self.bot)
         for chat in os.listdir("train."):
             conversations = open("train."+'/'+chat, 'r', encoding="utf8").readlines()
             trainer.train(conversations)
    
    def train_bot2(self):
        trainer = ChatterBotCorpusTrainer(self.bot)
        trainer.train("chatterbot.corpus.english")
        trainer.train("chatterbot.corpus.portuguese")        
        trainer.train("chatterbot.corpus.japanese")
        trainer.train("chatterbot.corpus.spanish")
