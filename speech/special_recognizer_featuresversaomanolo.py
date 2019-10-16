#!/usr/bin/env python3

import speech_recognition as sr
from os import path
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
    
#en_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
#engine.setProperty('voice', en_voice_id)
engine.say('Hi, my name is Theta. I`m a domestic robot.')
#engine.say('I was raised in cyphy lab for the UFPel, Freedom and IFSul')
#engine.say('My command list is, GO AHEAD, TURN LEFT, TURN RIGHT, STOP, MOVE, FOLLOW-ME and DANCE')
#engine.say('I like dance, and you?')
#engine.say('Oh my god, it is very nice')
#engine.say('ARE YOU READ?')
#engine.say('Would you like something?')

engine.runAndWait()
r = sr.Recognizer()
m = sr.Microphone()
with m as source:
    r.adjust_for_ambient_noise(source)
#help(r)
palavra = ''
while palavra != 'closed':
    with sr.Microphone() as source:
        audio = r.listen(source)
        text = r.recognize_sphinx(audio)
        #text = r.recognize_sphinx(audio)
        #text = r.recognize_google(audio)
        engine.say(text)
        engine.runAndWait()
        print(text)
        if text == 'closed':
            palavra = text
       # print(g)
