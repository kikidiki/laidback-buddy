from vars import *
def lol_matchup_file():
    global lol_thread
    # Start the League of Legends matchup finder process
    lol_thread = subprocess.Popen(["python", "Lol/lol_threads.py"], shell=True)

    # Wait for the process to finish
    lol_thread.wait()


