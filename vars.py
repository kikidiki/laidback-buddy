from logging.config import listen
import speech_recognition as sr
import pyttsx3
#import playsound
import webbrowser
import subprocess
from time import sleep
import threading
import lcu_driver
import asyncio


# Define listener and engine
listener = sr.Recognizer()
engine = pyttsx3.init('sapi5') # initialize with SAPI5 driver

# Check proptieties
voices = engine.getProperty('voices') # 0- male; 1- female; 2- demon levâi kakoita xd
rate = engine.getProperty("rate") # 200 default
volume = engine.getProperty("volume") # 1.0 default

# print(voices)
# print(rate)

engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 169)

# print(voices)
# print(rate)

# print("Male Voice : {0}".format(voices[0].id))
# print("Female Voice : {0}".format(voices[1].id))
# print("Female Voice : {0}".format(voices[2].id))

activationWord = ['OK']
#activationWord = 'ok'
stopWord = ['stfu', 'stop', 'shut the fuck up', 'exit']

stock_api_key = '19EBHMC0OVJS12H9'
sstock_api_key = 'DZOSXW8TC3NDSMIG'


def speak(text):
    engine.say(text)
    engine.runAndWait()



    ##############



