#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 18:00:02 2019

@author: manolo
"""
import time
from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.widget import Widget
import os
from kivy.core.window import Window

os.environ["KIVY_IMAGE"]="pil"

class ShowImage(Image):
    pass

class MyApp:
    def build(self):
        
        imagem = './gif/00_loading.gif'
        #return ShowImage(source=imagem, anim_delay= 0.1, 
                         #mipmap= True, allow_stretch= True)
        return ShowImage(source=imagem, anim_delay = 0.04)
        MyApp().run()
        #time.sleep(2)
        MyApp.on_stop()
        #return ShowImage(source='./gif/theta.jpeg',pos=(0,0),size=(512,512))
 
if __name__ == '__main__':
    #Window.clearcolor = (40, 40, 30, 20)
    MyApp().run()
    #time.sleep(2)
    MyApp.on_stop()
    
    def inicializa():
        MyApp().run()
        #time.sleep(2)
        MyApp.on_stop()