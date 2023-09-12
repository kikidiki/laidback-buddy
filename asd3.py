# import subprocess
# print("asd")
# def launch_lol():
#     print("asd2")
#     p = subprocess.Popen(["D:\Games\Riot Games\Riot Client\RiotClientServices.exe", "--headless",
#                           "--launch-product=league_of_legends", "--launch-patchline=live"])
#     # subprocess.run(["D:\Games\Riot Games\Riot Client\RiotClientServices.exe", "--headless",
#     #                 "--launch-product=league_of_legends", "--launch-patchline=live"])
#     print("asd3")
#     # do something else while the game is running
#     # p.terminate() # if you want to stop the game
# launch_lol()
# subprocess.run(["python", "asd.py"]) # run the other file as a command
import requests
import time
import urllib3
import os
import subprocess

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

client_ready = False  # Added a flag to check if the client is ready

def wait_for_client_ready():
    global client_ready
    while not client_ready:
        try:
            # Use a different command depending on the operating system
            if os.name == "nt": # Windows
                command = ["wmic", "PROCESS", "WHERE", "name='LeagueClientUx.exe'", "GET", "commandline"]
            else: # Mac
                command = ["ps", "-A", "|", "grep", "LeagueClientUx"]

            # Run the command and get its output as a string
            output = subprocess.check_output(command).decode()

            # Split the output by whitespace and look for the port number
            for word in output.split():
                if word.startswith("--app-port="):
                    # Get the port number from the word
                    port = word.split("=")[1]
                    # Construct the URL with the port number
                    url = f"https://127.0.0.1:{port}/alive"
                    # Break the loop
                    break

            # Send a GET request to the URL
            response = requests.get(url, verify=False)
            if response.status_code == 200:
                print("League of Legends client is ready.")
                client_ready = True
            else:
                print("Waiting for the League of Legends client to start...")
            time.sleep(2)
        except Exception as e:
            print(f"An error occurred while checking client readiness: {e}")
            time.sleep(2)


# Start waiting for the client to be ready in a separate thread
import threading

client_ready_thread = threading.Thread(target=wait_for_client_ready)
client_ready_thread.start()
