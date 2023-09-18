from Lol.lol_vars import *
new_pids = []
# Function to get the list of Python PIDs
def get_python_pids():
    python_pids = []
    for process in psutil.process_iter(attrs=['pid', 'name']):
        if "python" in process.info['name'].lower():
            python_pids.append(process.info['pid'])
    return python_pids

# Get the list of Python PIDs before starting the thread
initial_python_pids = get_python_pids()

# Print the initial Python PIDs
print(initial_python_pids)

# Function to start the League of Legends matchup finder process
def lol_matchup_finder():
    global process
    # Start the League of Legends matchup finder process
    process = subprocess.Popen(["python", "Lol/lol_match.py"], shell=True)

    # Wait for the process to finish
    process.wait()

# Create a thread for the lol_matchup_finder function
thread_lol_matchup_finder = threading.Thread(target=lol_matchup_finder)
thread_lol_matchup_finder.start()
print("Matchup finder started")

# Function to check for new Python processes
def check_new_python_processes():
    global new_pids
    time.sleep(2)  # Adjust the sleep duration as needed

    # Get the current list of Python PIDs
    current_python_pids = get_python_pids()

    # Calculate the difference to find new PIDs
    new_pids = set(current_python_pids) - set(initial_python_pids)

    if new_pids:
        print(f"New Python process(es) detected with PID(s): {new_pids}")

# Create a thread for checking new Python processes
thread_check_new_processes = threading.Thread(target=check_new_python_processes)
thread_check_new_processes.start()

# Function to stop the League of Legends matchup finder process
def stop_lol_matchup_finder():
    global process
    if process:
        process.terminate()

# Schedule the stop_lol_matchup_finder function to run after 200 seconds (adjust as needed)
# This part is useful in case when you manually cancel the queue
# It will stop the thread that is still running, because lcu_driver connector didn't finish the execution
# and it is waiting for the champion to pick and ban
timer = threading.Timer(200, stop_lol_matchup_finder)
timer.start()

# Wait for the lol_matchup_finder thread to finish
thread_lol_matchup_finder.join()

# Function to terminate newly created Python processes
# In case there are leftovers from the thread above such as zombie processes
def pid_killer():
    global new_pids
    for pid in new_pids:
        try:
            process = psutil.Process(pid)
            process.terminate()
            print(f"Killed process with PID: {pid}")
        except psutil.NoSuchProcess:
            print(f"Process with PID {pid} not found.")

# Create a thread for terminating new Python processes
thread_check_new_processes = threading.Thread(target=pid_killer)
thread_check_new_processes.start()

# Print a message to indicate the program has completed
print("Program completed")