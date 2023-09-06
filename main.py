from speak import *

# Main Loop

if __name__ == '__main__':
    speak('Waiting for instructions.')


    while True:
        query = parse_command()

        for word in activationWord:
            if word.lower() in query:
                # instructions
                listening()





#
# while True:
#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         print("Listening...")
#         audio = r.listen(source)
#     try:
#         query = r.recognize_google(audio)
#         print(f"You said: {query}")
#         if query == 'open chrome':
#             subprocess.run(["start", "microsoft-edge:https://thenextweb.com/news/google-chrome-sucks-heres-why-you-should-stop-using-it"], shell=True)
#             speak("Take diz")
#         elif query in stopWord:
#             speak("oke")
#             print("oke")
#             break
#         else:
#             speak("Command not recognized")
#     except Exception as e:
#         print(e)



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