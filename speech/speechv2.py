#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 19:20:47 2019

@author: manolo
"""

#!/usr/bin/env python3

import speech_recognition as sr
from os import path
import pyttsx3
import time
from check_host import check
from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.widget import Widget
import os
from kivy.core.window import Window
import threading
from kivy.clock import Clock
import time

for index, name in enumerate(sr.Microphone.list_microphone_names()):
    print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))

print('aqui')
engine = pyttsx3.init()
voices = engine.getProperty('voices')

#for voice in voices:
 #   print("Voice:")
  #  print(" - ID: %s" % voice.id)
   # print(" - Name: %s" % voice.name)
   # print(" - Languages: %s" % voice.languages)
   # print(" - Gender: %s" % voice.gender)
   # print(" - Age: %s" % voice.age)



engine.say('Hi, my name is Theta. I`m a domestic robot.')
time.sleep(2)
engine.runAndWait()
#engine.say('I was raised in cyphy lab for the UFPel, Freedom and IFSul')
#engine.runAndWait()
#time.sleep(2)
#engine.say('My command list is, GO AHEAD, TURN LEFT, TURN RIGHT, STOP, MOVE, FOLLOW-ME and DANCE')
#engine.runAndWait()
#time.sleep(2)
#engine.say('I like dancing, and you?')
#engine.runAndWait()
#time.sleep(2)
#engine.say('Oh my god, it is very nice')
#engine.runAndWait()
#time.sleep(2)
#engine.say('ARE YOU READ?')
#engine.runAndWait()
#time.sleep(2)
#engine.say('Would you like something?')

r = sr.Recognizer()
#help(r)
m = sr.Microphone()
with m as source:
    r.adjust_for_ambient_noise(source)
#help(r)
palavra = ''
while palavra != 'closed':
    with sr.Microphone() as source:
        ck = check()
        teste_conexao = ck.check_host()
        print(teste_conexao)
        audio = r.listen(source)
        print('escutou')
        if teste_conexao:
            #se on line
            print("google")
            try:
                text = r.recognize_google(audio)
            except:
                pass
        else:
            #se off line
            print("pocket")
            try:
                text = r.recognize_sphinx(audio, grammar='palavras.gram')
            except:
                pass
        print("Speech")
        
        """
        switch (text)
            case 1:  text = "January"
                break
            case 2:  text = "February"
                     break
            case 3:  text = "March"
                     break
            case 4:  text = "April"
                     break
            case 5:  text = "May"
                     break
            default: text = "Invalid month"
                     break
        """
        
        
        engine.say(text)
        engine.runAndWait()
        print(text)
        if text == 'closed':
            palavra = text
       # print(g)
