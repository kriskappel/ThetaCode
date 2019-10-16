#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 13:41:58 2019

@author: manolo
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 13:41:19 2019

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
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
import os

os.environ["KIVY_IMAGE"]="pil"

#rgb 40, 40 30

class ShowImage(Image):
    pass

class MyApp(App):
    def build(self):
        root = BoxLayout()
        
        root.add_widget(self.c)

        self.im.keep_ratio= False
        self.im.keep_data= True
        self.im.anim_delay = 0.2
        
        imagem = './gif/00_loading.gif'
        #return ShowImage(source=imagem, anim_delay= 0.1, 
                         #mipmap= True, allow_stretch= True)
        return ShowImage(source=imagem, anim_delay = 0.04) 
        #return ShowImage(source='./gif/theta.jpeg',pos=(0,0),size=(512,512))
    
        Clock.schedule_once(self.callback, 3.0)
 
    def callback(self, value):
        
        self.im.source='./gif/novos/07_smile.gif'
        self.im.keep_ratio= False
        self.im.keep_data= True
        self.im.anim_delay = 0.004
        #self.c.add_widget(self.im2)
        #Clock.schedule_once(self.apresentacao, 2.0)
        #self.c.clear_widgets()
        #Clock.schedule_once(self.callback1, 2.0)
        print('caraca')
 
if __name__ == '__main__':
    MyApp().run()
    #time.sleep(2)
    MyApp.on_stop()
