#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 18:47:22 2019

@author: manolo
"""

import kivy 
import sys
kivy.require('1.9.0')

from kivy.app import App 
from kivy.uix.label import Label 
from kivy.uix.floatlayout import FloatLayout 
from kivy.uix.textinput import TextInput 
from kivy.uix.button import Button

class My(App):
    def build(self):
        return Myapp()

class Myapp(FloatLayout):
    def callback(self,instance):
        import pyttsx
        self.engine=pyttsx.init()
        if self.t1.text:
            self.engine.say("you wrote something")
        self.engine.runAndWait()

    def __init__(self, **kwargs):
        super(Myapp, self).__init__(**kwargs)
        self.t1=TextInput(multiline=True,size_hint_x=0.5, size_hint_y=0.5)
        btn1=Button(text='read',size_hint=(.1,.1),pos_hint= {'x': .5,'top': .2})
        self.add_widget(self.t1)
        self.add_widget(btn1)
        self.bind(on_press=self.callback)

if __name__=='__main__':
    My().run()