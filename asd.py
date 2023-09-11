import time
import urllib3
from vars import *
import threading

import os



urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

#async def launch_lol():
#speak("Wait a sec")

# Create the connector object
connector = lcu_driver.Connector()
# Define a function to be called when LCU API is ready to be used
@connector.ready
async def connect(connection):

    # Create a lobby
    await connection.request('post', '/lol-lobby/v2/lobby', data={'queueId': 420})
    # Start matchmaking
    await connection.request('post', '/lol-lobby/v2/lobby/matchmaking/search')


# Register the connect function to be called on startup
#connector.ready(connect)
# Start the connector
connector.start()




