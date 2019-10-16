#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 18:44:38 2019

@author: manolo
"""

from kivy.app import App 
from kivy.uix.screenmanager import ScreenManager, Screen 
from kivy.clock import Clock, mainthread 
import speech_recognition as sr 
 
class Principal(Screen): 
    def BtnEscuchar(self): 
        self.ids.lblMensaje.text = "Say something!" 
        Clock.schedule_once(lambda d: self.GetAudio(), 0) 
 
    def GetAudio(self): 
        r = sr.Recognizer() 
        with sr.Microphone() as source: 
            audio = r.listen(source) 
        self.audio = audio 
        try: 
            self.ids.lblMensaje.text = "Google Speech Recognition thinks you said " + r.recognize_google(audio, language = 'es') 
        except sr.UnknownValueError: 
            print("Google Speech Recognition could not understand audio") 
        except sr.RequestError as e: 
            print("Could not request results from Google Speech Recognition service; {0}".format(e)) 
 
class testspkApp(App): 
 
    def build(self): 
        sm = ScreenManager() 
        self.sm = sm 
        sm.add_widget(Principal(name='Principal')) 
        return sm 
 
    def on_pause(self): 
        return False 
 
 
main = testspkApp() 
main.run()



testspk.kv
