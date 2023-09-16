import subprocess
import os
import tkinter as tk
from tkinter import filedialog, simpledialog
import json

# Define the path to the JSON configuration file
config_file_path = "config.json"

# Check if the JSON file exists
if os.path.exists(config_file_path):
    with open(config_file_path, 'r') as file:
        config_data = json.load(file)
else:
    # If the file doesn't exist, create an empty dictionary
    config_data = {}

    # Create a dialog box for the first-time setup
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    # Show a message to the user
    tk.messagebox.showinfo("First Time Setup",
                           "Looks like it's the first time you are asking for my assistance. Let's declare some picks and bans.")

    # Use simpledialog to get user input for "Pick" and "Ban"
    config_data["Pick"] = simpledialog.askstring("First Time Setup", "Enter your pick:")
    config_data["Ban"] = simpledialog.askstring("First Time Setup", "Enter your ban:")

    # Check if the user canceled input
    if config_data["Pick"] is None or config_data["Ban"] is None:
        raise ValueError("Pick and Ban not defined. Exiting...")

    # Show the file selection dialog for Riot Client path
    file_types = [("All Files", "*.*")]
    base_directory = filedialog.askopenfilename(
        title="Select the base directory where RiotClientServices.exe is located",
        filetypes=file_types
    )

    if not base_directory:
        raise ValueError("Base directory not selected. Exiting...")

    config_data["Path"] = base_directory

    # Write the updated configuration data to the JSON file
    with open(config_file_path, 'w') as file:
        json.dump(config_data, file, indent=4)

# Construct the full file path to RiotClientServices.exe using os.path.join
riot_client_path = os.path.join(config_data["Path"])

# Check if the file exists at the constructed path
if not os.path.exists(riot_client_path):
    raise FileNotFoundError(f"RiotClientServices.exe not found at {riot_client_path}")

# Define the arguments for the subprocess.Popen
args = [riot_client_path, "--headless", "--launch-product=league_of_legends", "--launch-patchline=live"]

# Start the subprocess
# p = subprocess.Popen(args)

# Wait for the subprocess to complete, if needed
# p.wait()
