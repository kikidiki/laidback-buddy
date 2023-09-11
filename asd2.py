import time

from vars import *
import os

connector = lcu_driver.Connector()

async def launch_lol():
    p = subprocess.Popen(["D:\Games\Riot Games\Riot Client\RiotClientServices.exe", "--headless",
                          "--launch-product=league_of_legends", "--launch-patchline=live"])

async def create_lobby(connection):
    await connection.request('post', '/lol-lobby/v2/lobby', data={'queueId': 420})
    await connection.request('post', '/lol-lobby/v2/lobby/matchmaking/search')

@connector.ws.register('/lol-service-status/v1/lcu-status', event_types=('UPDATE',))
async def client_status_changed(connection, event):
    if event.data['connectionState'] == 'Connected':
        task1 = asyncio.create_task(launch_lol())
        task2 = asyncio.create_task(create_lobby())
        await task1
        await task2

@connector.ready
async def connect(connection):
    pass

connector.start()



@connector.ws.register('/lol-matchmaking/v1/ready-check', event_types=('UPDATE',))
async def ready_check_changed(connection, event):
    if event.data['state'] == 'InProgress' and event.data['playerResponse'] == 'None':
        await connection.request('post', '/lol-matchmaking/v1/ready-check/accept', data={})
