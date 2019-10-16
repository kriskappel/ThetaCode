#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 20:28:50 2019

@author: manolo
"""

from kivy.base import EventLoop
from kivy.clock import Clock
from kivy.core.window import Window

import time

def callback2(*args):
    print ('2', time.time())

def callback1(*args):
    print ('1', time.time())
    Clock.schedule_once(callback2, 2.0)

print ('start', time.time())
Clock.schedule_once(callback1, 3.0)
EventLoop.run()