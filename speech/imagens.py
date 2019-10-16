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

os.environ["KIVY_IMAGE"]="pil"

#rgb 40, 40 30

class ShowImage(Image):
    pass

class MyApp(App):
    def build(self):
        
        imagem = './gif/00_loading.gif'
        #return ShowImage(source=imagem, anim_delay= 0.1, 
                         #mipmap= True, allow_stretch= True)
        
        return ShowImage(source=imagem, anim_delay = 0.04) 
        #return ShowImage(source='./gif/theta.jpeg',pos=(0,0),size=(512,512))
        
    def tradeimage(self):
        imagem = './gif/01_happy.gif'
        #return ShowImage(source=imagem, anim_delay= 0.1, 
                         #mipmap= True, allow_stretch= True)
        return ShowImage(source=imagem, anim_delay = 0.04) 
    
 
if __name__ == '__main__':
    MyApp().run()
    #time.sleep(2)
    MyApp.on_stop()
