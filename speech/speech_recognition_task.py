import speech_recognition as sr
from os import path
import pyttsx3
import time
from check_host import check
import threading
import time
from std_msgs.msg import String
from std_msgs.msg import Int16

import rospy
for index, name in enumerate(sr.Microphone.list_microphone_names()):
    print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))

speech_pub = rospy.Publisher('speech_recognized', String, queue_size=10)
turn_pub = rospy.Publisher('channel_x', Int16, queue_size=10)

rospy.init_node('speech_rec', anonymous=True)

engine = pyttsx3.init()
voices = engine.getProperty('voices')

engine.say('Hello world!')
engine.runAndWait()
engine.say('I am Theta!')
engine.runAndWait()
r = sr.Recognizer()
r2 = sr.Recognizer()

m = sr.Microphone()
n = sr.Microphone()
engine.say('I want to play riddles')
engine.runAndWait()
#help(r)
time.sleep(10)

turn_pub.publish(170)

time.sleep(4)

turn_pub.publish(135)

