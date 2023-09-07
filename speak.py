from vars import *


# Play an audio file (import playsound)
# drasti = "voicerecs/drasti.mp3"
# playsound.playsound(drasti)


# listens for keyword
def parse_command():
    print("Listening")
    with sr.Microphone() as source:
        listener.pause_threshold = 1  # how long before the listening is canceled
        listener.energy_threshold = 500
        input_speech = listener.listen(source)
    try:
        print('Recognizing speech...')
        query = listener.recognize_google(input_speech, language='en_us')
        query = query.lower()
        #speak("Got you!")
        #speak(f"You said: {query}")
        print(query)
    except Exception as e:
        speak("I didn't understand what you've said")
        print(f"Error: {e}")
        return 'None'
    return query.lower()


def open_edge():
    print("I am listening for a command")
    speak("I am listening for a command")
    with sr.Microphone() as source:
        listener.pause_threshold = 1  # how long before the listening is canceled
        listener.energy_threshold = 500
        command = listener.listen(source)
    try:
        print('Recognizing speech...')
        query = listener.recognize_google(command, language='en_us')
        query = query.lower()
        print(f"You said: {query}")
        if query == 'open chrome':
            subprocess.run(["start", "microsoft-edge:https://thenextweb.com/news/google-chrome-sucks-heres-why-you-should-stop-using-it"], shell=True)
            speak("Take diz")

        else:
            speak("Command not recognized")
            open_edge()

    except Exception as e:
        speak("I didn't understand what you've said")
        print(f"Error: {e}")
        open_edge()
        return 'None'
    return query


def listening():
    print("I am listening for a command")
    speak("I am listening for a command")
    with sr.Microphone() as source:
        listener.pause_threshold = 1  # how long before the listening is canceled
        listener.energy_threshold = 500
        command = listener.listen(source)
    try:
        print('Recognizing speech...')
        query = listener.recognize_google(command, language='en_us')
        query = query.lower()
        print(f"You said: {query}")

        if query == 'open chrome':
            subprocess.run(["start", "microsoft-edge:https://thenextweb.com/news/google-chrome-sucks-heres-why-you-should-stop-using-it"], shell=True)
            speak("Take diz")

        if query == 'open chrome':
            # start the Riot Client in the background and open the League of Legends client
            subprocess.run(["D:\Games\Riot Games\Riot Client\RiotClientServices.exe", "--headless",
                            "--launch-product=league_of_legends", "--launch-patchline=live"])
            speak("Wait a sec")


        elif any(word in query for word in stopWord):
            speak("oke")
            print("oke")

        else:
            speak("Command not recognized")
            listening()

        #test
    except Exception as e:
        speak("I didn't understand what you've said")
        print(f"Error: {e}")
        open_edge()
        return 'None'
    return query






# def parse_command():
#     print("Listening for activation word...")
#     with sr.Microphone() as source:
#         listener.pause_threshold = 4
#         listener.energy_threshold = 200
#         audio = listener.listen(source)
#
#     try:
#         query = listener.recognize_google(audio, language='en_us')
#         query = query.lower()
#         if activationWord in query :
#             print("Activation word heard")
#             print("Recognizing speech...")
#             with sr.Microphone() as source:
#                 audio = listener.listen(source)
#             query = listener.recognize_google(audio, language='en_us')
#             query = query.lower()
#             speak("got you!")
#             speak(f"You said: {query}")
#             print(query)
#             return query
#         else:
#             print("Activation word not heard, listening again...")
#             return 'None'
#     except Exception as e:
#         speak("I didn't understand what you've said")
#         print(f"Error: {e}")
#         return 'None'




# engine.say("command")
# engine.runAndWait()
#
#
# with sr.Microphone() as source:
#     print('listening...')
#     voice = listener.listen(source)
#     command = listener.recognize_google(voice)
#     commands = command.lower()
#     print('asdlistening...')
#     engine.say(command)
#     engine.runAndWait()
#
#     print(commands)



