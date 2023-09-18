from Lol.lol_vars import *

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Create the connector object
connector = lcu_driver.Connector()

# Initialize global variables
global am_i_assigned, am_i_picking, am_i_banning, ban_number, phase, picks, bans, in_game
am_i_assigned = False
am_i_banning = False
am_i_picking = False
in_game = False
phase = ''
picks = []
bans = []
pick_number = 0
ban_number = 0

# Load picks and bans from external files

try:
    picks_file = open("Lol/picks.txt", "r").read().splitlines()
except:
    picks_file = open("picks.txt", "r").read().splitlines()

for line in picks_file:
    picks.append(line)


try:
    bans_file = open("Lol/bans.txt", "r").read().splitlines()
except:
    bans_file = open("bans.txt", "r").read().splitlines()


for line in bans_file:
    bans.append(line)


# Define a function to be executed when the connector is ready
@connector.ready
async def connect(connection):
    global summoner_id, champions_map
    temp_champions_map = {}

    # Get current summoner information
    summoner = await connection.request('get', '/lol-summoner/v1/current-summoner')
    summoner_to_json = await summoner.json()
    summoner_id = summoner_to_json['summonerId']

    # Get the list of champions
    champion_list = await connection.request('get', f'/lol-champions/v1/inventories/{summoner_id}/champions-minimal')
    champion_list_to_json = await champion_list.json()

    # Create a map of champion names to champion IDs
    for i in range(len(champion_list_to_json)):
        temp_champions_map.update({champion_list_to_json[i]['name']: champion_list_to_json[i]['id']})
    champions_map = temp_champions_map


# Start the League of Legends client using subprocess
from lol_directory import args

# p = subprocess.Popen(["D:\\Games\\Riot Games\\Riot Client\\RiotClientServices.exe", "--headless",
#                     "--launch-product=league_of_legends", "--launch-patchline=live"])

p = subprocess.Popen(args)

while True:
    try:
        # Try to find the League of Legends client window by its title
        app = pywinauto.Application().connect(title="League of Legends", found_index=0)
        print("The League of Legends client is loaded and ready.")
        time.sleep(13)
        break
    except pywinauto.findwindows.ElementNotFoundError:
        # The window is not found, so the League of Legends client is still loading
        print("The League of Legends client is still loading...")
        time.sleep(1)


# Define a function to be executed when the connector is ready
@connector.ready
async def connect(connection):
    # Create a lobby
    await connection.request('post', '/lol-lobby/v2/lobby', data={'queueId': 450})
    time.sleep(1)

    # Start matchmaking
    await connection.request('post', '/lol-lobby/v2/lobby/matchmaking/search')


# Register an event handler for the ready-check
@connector.ws.register('/lol-matchmaking/v1/ready-check', event_types=('UPDATE',))
async def ready_check_changed(connection, event):
    if event.data['state'] == 'InProgress' and event.data['playerResponse'] == 'None':
        await connection.request('post', '/lol-matchmaking/v1/ready-check/accept', data={})


# Register an event handler for the champion select phase
@connector.ws.register('/lol-champ-select/v1/session', event_types=('CREATE', 'UPDATE',))
async def champ_select_changed(connection, event):
    global am_i_assigned, pick_number, ban_number, am_i_banning, am_i_picking, phase, bans, picks, in_game, action_id

    # Get the current lobby phase from the event data
    lobby_phase = event.data['timer']['phase']

    # Get the local player's cell ID to identify their actions
    local_player_cell_id = event.data['localPlayerCellId']

    # Check if the local player is assigned to a position in the team
    for teammate in event.data['myTeam']:
        if teammate['cellId'] == local_player_cell_id:
            assigned_position = teammate['assignedPosition']
            am_i_assigned = True

    # Loop through the actions in the event data
    for action in event.data['actions']:
        for actionArr in action:
            # Check if the action is in progress and matches the local player's cell ID
            if actionArr['actorCellId'] == local_player_cell_id and actionArr['isInProgress'] == True:
                phase = actionArr['type']
                action_id = actionArr['id']
                if phase == 'ban':
                    am_i_banning = actionArr['isInProgress']
                if phase == 'pick':
                    am_i_picking = actionArr['isInProgress']

    # Handle banning phase
    if phase == 'ban' and lobby_phase == 'BAN_PICK' and am_i_banning:
        while am_i_banning:
            try:
                # Send a request to ban a champion based on the ban_number
                await connection.request('patch', '/lol-champ-select/v1/session/actions/%d' % action_id,
                                         data={"championId": champions_map[bans[ban_number]], "completed": True})
                ban_number += 1
                am_i_banning = False
                print("banned")

            except (Exception,):
                # Handle exceptions and wrap around if ban_number exceeds the number of bans
                ban_number += 1
                if ban_number > len(bans):
                    ban_number = 0

    # Handle picking phase
    if phase == 'pick' and lobby_phase == 'BAN_PICK' and am_i_picking:
        while am_i_picking:
            try:
                # Send a request to pick a champion based on the pick_number
                await connection.request('patch', '/lol-champ-select/v1/session/actions/%d' % action_id,
                                         data={"championId": champions_map[picks[pick_number]], "completed": True})
                pick_number += 1
                am_i_picking = False
                print("picked")

            except (Exception,):
                # Handle exceptions and wrap around if pick_number exceeds the number of picks
                pick_number += 1
                if pick_number > len(picks):
                    pick_number = 0

    # Check for the game starting phase
    if lobby_phase == 'GAME_STARTING':
        while not in_game:
            try:
                # Send a request to the local game client to get game data
                request_game_data = requests.get('https://127.0.0.1:2999/liveclientdata/allgamedata', verify=False)
                game_data = request_game_data.json()['gameData']['gameTime']
                if game_data > 0 and not in_game:
                    print("Game found!")
                    in_game = True

                # Sleep to avoid excessive requests
                time.sleep(2)

                # Stop the connector if the game starts
                await connector.stop()

            except (Exception,):
                # Handle exceptions and continue waiting
                print('Waiting for the game to start...')
                time.sleep(2)


# Start the connector
connector.start()