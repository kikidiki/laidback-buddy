import subprocess

# start the Riot Client in the background and open the League of Legends client
subprocess.run(["D:\Games\Riot Games\Riot Client\RiotClientServices.exe", "--headless",
                "--launch-product=league_of_legends", "--launch-patchline=live"])
