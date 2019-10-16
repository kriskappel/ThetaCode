#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 11:21:28 2019

@author: manolo
"""
import speech_recognition as sr
from os import path
import pyttsx3
import time
from check_host import check
import threading
import time
from std_msgs.msg import String

import rospy
for index, name in enumerate(sr.Microphone.list_microphone_names()):
    print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))

pub = rospy.Publisher('speech_recognized', String, queue_size=10)
rospy.init_node('speech_rec', anonymous=True)

engine = pyttsx3.init()
voices = engine.getProperty('voices')
#engine.say('Hi, my name is Theta. I`m a domestic robot.')
#time.sleep(2)
#engine.runAndWait()
#engine.say('I was raised in cyphy lab for the UFPel, Freedom and IFSul')
#engine.runAndWait()
#time.sleep(2)
#engine.say('My command list is, GO AHEAD, TURN LEFT, TURN RIGHT, STOP, FOLLOW-ME and DANCE')
#engine.runAndWait()
#time.sleep(2)
#engine.say('I like dancing, and you?')
#engine.runAndWait()
#time.sleep(2)
#engine.say('Oh my god, it is very nice')
#engine.runAndWait()
#time.sleep(2)
engine.say('ARE YOU READY?')
engine.runAndWait()
time.sleep(2)
r = sr.Recognizer()
r2 = sr.Recognizer()
#help(r)
m = sr.Microphone()
n = sr.Microphone()

#help(r)

# #commented
# text = 'a'
# textconf = 'a'
# palavra = ''
# def palavrasiniciais():
#     with m as source:
#         engine.say('Would you like something?')
#         engine.runAndWait()
#         text = ''
#         textconf = ''
#         print('listen')
#         r.adjust_for_ambient_noise(source)
#         try:
#             audio = r.listen(source)
#         except sr.UnknownValueError:
#             print("Could not understand audio")
#         print('escutou')
#         #text = r.recognize_google_cloud(audio)
#         try:
#             text = r.recognize_sphinx(audio, grammar='palavras.gram')
#         except:
#             pass
#         print('text:', text)
#         return text
# def confirmacao(text):
#     engine.say('You said')
#     engine.runAndWait()
#     engine.say(text)
#     engine.runAndWait()
#     engine.say('You sure?')
#     engine.runAndWait()
#     time.sleep(1)
#     pubros = ''
#     with n as source2:
#         print('listen confirmed')
#         r2.adjust_for_ambient_noise(source2)
#         try:
#             audio2 = r2.listen(source2)
#         except sr.UnknownValueError:
#             print("Could not understand audio")
#         print('escutou confirmacao')
#         try:
#             textconf = r2.recognize_sphinx(audio2, grammar='confirma.gram')
#         except:
#             textconf = 'no'
#         print('textconf', textconf)
#         if textconf == 'yes':
#             if text == 'left':
#                 pubros = 'turnLeft 90'
#             elif text == 'right':
#                 pubros = 'turnRight 90'
#             elif text == 'go':
#                 pubros = 'goAhead 1 175'
#             elif text == 'follow':
#                 pubros = 'follow-me'
#             elif text == 'dance':
#                 pubros = 'dance'
#             elif text == 'stop':
#                 pubros = 'stop'
#             print('rostopic', pubros)
#             engine.say('You said')
#             engine.runAndWait()
            
#             try:
                
#                 pub.publish(pubros)
#                 #pub.publish(pubros)
#             except rospy.ROSInnterruptException:
#                 print("error")
# while palavra != 'closed':
#     rec1 = palavrasiniciais()
#     if rec1 == 'left' or rec1 =='right' or rec1 == 'go' or rec1 == 'follow' or rec1 == 'move' or rec1 == 'dance' or rec1 == 'stop':
#         rec2 = confirmacao(rec1)
        
        
        
#    with sr.Microphone() as source:
#        engine.say('Would you like something?')
#        engine.runAndWait()
#        text = ''
#        textconf = ''
#        print('listen')
#        r.adjust_for_ambient_noise(source)
#        try:
#            audio = r.listen(source)
#        except sr.UnknownValueError:
#            print("Could not understand audio")
#        print('escutou')
#        #text = r.recognize_google_cloud(audio)
#        try:
#            text = r.recognize_sphinx(audio, grammar='palavras.gram')
#        except:
#            pass
#        print('text:', text)
#        if text == 'left' or text =='right' or text == 'go' or text == 'follow' or text == 'move' or text == 'dance' or text == 'stop':
#            with sr.Microphone() as source:
#                engine.say('You said')
#                engine.runAndWait()
#                engine.say(text)
#                engine.runAndWait()
#                engine.say('You sure?')
#                engine.runAndWait()
#                
#                time.sleep(1)
#                print('listen confirmed')
#                r2.adjust_for_ambient_noise(source)
#                try:
#                    audio2 = r2.listen(source)
#                except sr.UnknownValueError:
#                    print("Could not understand audio")
#                print('escutou confirmacao')
#                try:
#                    textconf = r2.recognize_sphinx(audio2, grammar='confirma.gram')
#                except:
#                    pass
#                print('textconf', textconf)
#                if textconf == 'yes':
#                    print('rostopic')
#                    engine.say('You said')
#                    engine.runAndWait()
#                    """try:
#                        pub = rospy.Publisher('walk', String, queue_size=1)
#                        pub.publish(text)
#                    except rospy.ROSInnterruptException:
#                        pass"""
