import time
import lcu_driver
import asyncio
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

from vars import *
import os

connector = lcu_driver.Connector()

async def launch_lol():
    p = subprocess.Popen(["D:\\Games\\Riot Games\\Riot Client\\RiotClientServices.exe", "--headless",
                          "--launch-product=league_of_legends", "--launch-patchline=live"])


@connector.ws.register('/lol-service-status/v1/lcu-status', event_types=('UPDATE',))
async def ready_check_changed(connection, event):
    if event.data['connectionState'] == 'Connected':
        await connection.request('post', '/lol-lobby/v2/lobby', data={'queueId': 420})
        await connection.request('post', '/lol-lobby/v2/lobby/matchmaking/search')


@connector.ws.register('/lol-matchmaking/v1/ready-check', event_types=('UPDATE',))
async def ready_check_changed(connection, event):
    if event.data['state'] == 'InProgress' and event.data['playerResponse'] == 'None':
        await connection.request('post', '/lol-matchmaking/v1/ready-check/accept', data={})


connector.start()




asyncio.run(launch_lol())