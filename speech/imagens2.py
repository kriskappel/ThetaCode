#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 20:47:42 2019

@author: manolo
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 14:49:58 2019

@author: manolo
"""
import time
from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.widget import Widget
import os
from kivy.base import EventLoop
from kivy.clock import Clock
import pyttsx3
from kivy.graphics import Color, Rectangle
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout


os.environ["KIVY_IMAGE"]="pil"

#rgb 40, 40 30]


class ShowImage(Image):
    pass

def callback2(*args):
    print ('2', time.time())
    Clock.schedule_once(callback3, 2.0)
    MyApp.source = './gif/07_smile.gif'

def callback3(*args):
    print('callback 3')    
    imagem = './gif/07_smile.gif'
    #return ShowImage(source=imagem, anim_delay= 0.1, 
                     #mipmap= True, allow_stretch= True)
    return ShowImage(source=imagem, anim_delay = 0.04) 
    #return ShowImage(source='./gif/theta.jpeg',pos=(0,0),size=(512,512))

def callback1(*args):
    print ('1', time.time())
    engine = pyttsx3.init()
    print('init')
    #voices = engine.getProperty('voices')
    print('voice')
    engine.say('Hi, my name is Theta. I`m a domestic robot.')
    print('run')
    engine.runAndWait()
    Clock.schedule_once(callback2, 2.0)

class MyApp(App):
    
    def build(self):
        
        imagem = './gif/00_loading.gif'
        #return ShowImage(source=imagem, anim_delay= 0.1, 
                         #mipmap= True, allow_stretch= True)
        Clock.schedule_once(self.callback, 3.0)
        return ShowImage(source=imagem, anim_delay = 0.04) 
        #return ShowImage(source='./gif/theta.jpeg',pos=(0,0),size=(512,512))
    def callback(self, value):
        #self.im.source =im2
        print('caraca')
        #engine = pyttsx3.init()
        #engine.say('Hi, my name is Theta. I`m a domestic robot.')
        #engine.runAndWait()
        
        #Clock.schedule_once(self.callback4, 3.0)

if __name__ == '__main__':
    Clock.schedule_once(callback1, 3.0)
    #EventLoop.run()
    MyApp().run()
    #time.sleep(2)
    MyApp.on_stop()
