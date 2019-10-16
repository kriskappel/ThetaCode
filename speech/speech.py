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

os.environ["KIVY_IMAGE"]="pil"

#rgb 40, 40 30

class ShowImage(Image):
   pass    

class MyApp(App):
    def build(self):
        print('aqui')
        imagem = './gif/00_loading.gif'
        #return ShowImage(source=imagem, anim_delay= 0.1, 
                         #mipmap= True, allow_stretch= True)
        return ShowImage(source=imagem, anim_delay = 0.04)
        

        #return ShowImage(source='./gif/theta.jpeg',pos=(0,0),size=(512,512))
 

if __name__ == '__main__':
    #Window.clearcolor = (40, 40, 30, 20)
    while True:
        MyApp().run()
        MyApp().on_pause()
        print('show')
        engine = pyttsx3.init()
        print('init')
        voices = engine.getProperty('voices')
        print('voice')
        engine.say('Hi, my name is Theta. I`m a domestic robot.')
        print('run')
        engine.runAndWait()
        
#    #time.sleep(2)
#    #MyApp.on_stop()
#    print('cacete')

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
engine.say('I was raised in cyphy lab for the UFPel, Freedom and IFSul')
engine.runAndWait()
time.sleep(2)
engine.say('My command list is, GO AHEAD, TURN LEFT, TURN RIGHT, STOP, MOVE, FOLLOW-ME and DANCE')
engine.runAndWait()
time.sleep(2)
engine.say('I like dancing, and you?')
engine.runAndWait()
time.sleep(2)
engine.say('Oh my god, it is very nice')
engine.runAndWait()
time.sleep(2)
engine.say('ARE YOU READ?')
engine.runAndWait()
time.sleep(2)
engine.say('Would you like something?')
engine.runAndWait()

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