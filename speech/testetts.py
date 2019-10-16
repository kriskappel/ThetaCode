# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 19:18:30 2019

@author: Emanuel
"""

import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
for voice in voices:
    print("Voice:")
    print(" - ID: %s" % voice.id)
    print(" - Name: %s" % voice.name)
    print(" - Languages: %s" % voice.languages)
    print(" - Gender: %s" % voice.gender)
    print(" - Age: %s" % voice.age)
    
en_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
engine.setProperty('voice', en_voice_id)
engine.say('Hi, my name is Theta. I`m a domestic robot.')
engine.say('I was raised in cyphy lab for the UFPel, Freedom and IFSul')
engine.say('My command list is, GO AHEAD, TURN LEFT, TURN RIGHT, STOP, MOVE, FOLLOW-ME and DANCE')
engine.say('I like dance, and you?')
engine.say('Oh my god, it is very nice')
engine.say('ARE YOU READ?')
engine.say('Would you like something?')

engine.runAndWait()