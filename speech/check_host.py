#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 15:16:38 2019

@author: manolo
"""
import socket


confiaveis = ['www.google.com']

class check:     
    def check_host(self):
       global confiaveis
       for host in confiaveis:
         a=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
         a.settimeout(.5)
         try:
           b=a.connect_ex((host, 80))
           if b==0: #ok, conectado
             return True
         except:
           pass
         a.close()
       return False