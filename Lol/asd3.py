import subprocess
import threading
import time
import threading
import time
import psutil


def get_python_pids():
    python_pids = []
    for process in psutil.process_iter(attrs=['pid', 'name']):
        if "python" in process.info['name'].lower():
            python_pids.append(process.info['pid'])
    return python_pids




# Get the list of Python PIDs before starting the thread
initial_python_pids = get_python_pids()

print(initial_python_pids)



def lol_matchup_finder():
    global process
    #process = subprocess.Popen(["venv\Scripts\python.exe", "asd.py"], shell=True)
    process = subprocess.Popen(["python", "asd.py"], shell=True)

    process.wait()


thread_lol_matchup_finder = threading.Thread(target=lol_matchup_finder)
thread_lol_matchup_finder.start()
print("start")



def check_new_python_processes():
    global new_pids
    time.sleep(3)  # Adjust the sleep duration as needed
    current_python_pids = get_python_pids()
    new_pids = set(current_python_pids) - set(initial_python_pids)

    if new_pids:
        print(f"New Python process(es) detected with PID(s): {new_pids}")

thread_check_new_processes = threading.Thread(target=check_new_python_processes)
thread_check_new_processes.start()



def stop_lol_matchup_finder():
    global process
    if process:
        process.terminate()




# Schedule the stop_lol_matchup_finder function to run after 3 seconds
timer = threading.Timer(20, stop_lol_matchup_finder)
timer.start()

# Wait for the lol_matchup_finder thread to finish
thread_lol_matchup_finder.join()

def pid_killer():
    global new_pids
    for pid in new_pids:
        try:
            process = psutil.Process(pid)
            process.terminate()
            print(f"Killed process with PID: {pid}")
        except psutil.NoSuchProcess:
            print(f"Process with PID {pid} not found.")

thread_check_new_processes = threading.Thread(target=pid_killer)
thread_check_new_processes.start()


print("stop")
