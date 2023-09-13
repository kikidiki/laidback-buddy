import subprocess
import threading
import time
import threading
import time

process = None

def lol_matchup_finder():
    global process

    process = subprocess.Popen(["venv\\Scripts\\python.exe", "asd2.py"])  # run the other file as a command
    process.wait()

thread_lol_matchup_finder = threading.Thread(target=lol_matchup_finder)
def asd():
    while True:
        print("asd")
        time.sleep(13)

def dsa():
    while True:
        print("dsa")
        time.sleep(13)

thread_lol_matchup_finder.start()
print("start")

asdd = threading.Thread(target=asd)
dsaa = threading.Thread(target=dsa)

asdd.start()
dsaa.start()
time.sleep(3)

# Use a flag to gracefully exit the lol_matchup_finder thread
exit_thread_flag = True

# Define a function to stop the lol_matchup_finder thread
def stop_lol_matchup_finder():
    global process
    if process:
        process.terminate()  # Terminate the subprocess
    exit_thread_flag = False

# Schedule the stop_lol_matchup_finder function to run after 3 seconds
timer = threading.Timer(3, stop_lol_matchup_finder)
timer.start()

# Wait for the lol_matchup_finder thread to finish
thread_lol_matchup_finder.join()

print("stop")
