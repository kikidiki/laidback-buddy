import time
import urllib3
from vars import *
import threading
import pywinauto

import os

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

#async def launch_lol():
#speak("Wait a sec")

# Create the connector object
connector = lcu_driver.Connector()
# Define a function to be called when LCU API is ready to be used

p = subprocess.Popen(["D:\\Games\\Riot Games\\Riot Client\\RiotClientServices.exe", "--headless",
                      "--launch-product=league_of_legends", "--launch-patchline=live"])

# time.sleep(20)

while True:
    try:
        # Try to find the lol client window by its title
        app = pywinauto.Application().connect(title="League of Legends", found_index=0)
        print("The lol client is loaded and ready.")
        time.sleep(6.9)
        break
        pass
    except pywinauto.findwindows.ElementNotFoundError:
        # The window is not found, so the lol client is still loading
        print("The lol client is still loading...")
        time.sleep(1)
@connector.ready
async def connect(connection):

    # Create a lobby
    await connection.request('post', '/lol-lobby/v2/lobby', data={'queueId': 450})
    # Start matchmaking
    await connection.request('post', '/lol-lobby/v2/lobby/matchmaking/search')

@connector.ws.register('/lol-matchmaking/v1/ready-check', event_types=('UPDATE',))
async def ready_check_changed(connection, event):
    if event.data['state'] == 'InProgress' and event.data['playerResponse'] == 'None':
        await connection.request('post', '/lol-matchmaking/v1/ready-check/accept', data={})


# Register the connect function to be called on startup
#connector.ready(connect)
# Start the connector
connector.start()




