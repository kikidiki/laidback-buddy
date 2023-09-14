import subprocess
import threading
import time
import threading
import time

def lol_matchup_finder():
    global process
    process = subprocess.Popen(["venv\\Scripts\\python.exe", "asd.py"])
    process.wait()


thread_lol_matchup_finder = threading.Thread(target=lol_matchup_finder)
thread_lol_matchup_finder.start()
print("start")

def stop_lol_matchup_finder():
    global process
    if process:
        process.terminate()

# Schedule the stop_lol_matchup_finder function to run after 3 seconds
timer = threading.Timer(20, stop_lol_matchup_finder)
timer.start()

# Wait for the lol_matchup_finder thread to finish
thread_lol_matchup_finder.join()

print("stop")
