from vars import *


def open_lol():
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
            # start the Riot Client in the background and open the League of Legends client
            subprocess.run(["D:\Games\Riot Games\Riot Client\RiotClientServices.exe", "--headless",
                            "--launch-product=league_of_legends", "--launch-patchline=live"])
            speak("Wait a sec")

        else:
            speak("Command not recognized")
            open_lol()

    except Exception as e:
        speak("I didn't understand what you've said")
        print(f"Error: {e}")
        open_lol()
        return 'None'
    return query




