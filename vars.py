from logging.config import listen
import speech_recognition as sr
import pyttsx3
import playsound
import webbrowser
import subprocess
from time import sleep
import threading


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

activationWord = ['Cami', 'Yo Cami', 'OK', 'Hey Cami', 'Hey Camilla', 'Camilla',  'Hey Camila', 'Camila']
#activationWord = 'ok'
stopWord = ['stfu', 'stop', 'shut the fuck up', 'exit']


def speak(text):
    engine.say(text)
    engine.runAndWait()