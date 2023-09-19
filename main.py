from speak import *

if __name__ == '__main__':
    speak('Waiting for instructions.')

    while True:
        query = parse_command()

        for word in activationWord:
            if word.lower() in query:
                listening()

        for word in stopWord:
            if word.lower() in query:
                speak('Stopping the program.')
                exit(0)  # Exit the program when the stop word is detected





##################### implement threading and canceling on listening



    # while True:
    #     # Parse as a list
    #     query = parse_command().lower().split()
    #
    #     if activationWord in query:
    #         query.pop(0)
    #
    #         #List commands
    #         if query[0] == 'google':
    #             if '' in query:
    #                 speak("Heya, m'Lord!!")
    #             else:
    #                 query.pop(0) #remove 'say'
    #                 speech = ''.join(query)
    #                 speak(speech)