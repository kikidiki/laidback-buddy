from funcs import *
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



def listening():
    print("I am listening for a command")
    speak("I am listening for a command")
    with sr.Microphone() as source:
        listener.pause_threshold = 1  # how long before the listening is canceled
        listener.energy_threshold = 500
        command = listener.listen(source)
    try:
        print('sRecognizing speech...')
        query = listener.recognize_google(command, language='en_us')
        query = query.lower()
        print(f"You said: {query}")

        if query == 'open chrome':
            subprocess.run(["start", "microsoft-edge:https://thenextweb.com/news/google-chrome-sucks-heres-why-you-should-stop-using-it"], shell=True)
            speak("Take diz")
            listening()

        elif query == 'open league':
            print("ads")
            thread_lol_matchup_file = threading.Thread(target=lol_matchup_file)
            thread_lol_matchup_file.start()
            listening()

        elif any(word in query for word in stopWord):
            speak("oke")
            print("oke")
            exit(0)  # Exit the program when the stop word is detected
        else:
            speak("Command not recognized")
            listening()

    except Exception as e:
        speak("I didn't understand what you've said")
        print(f"Error: {e}")
        listening()
        return 'None'
    return query.lower






