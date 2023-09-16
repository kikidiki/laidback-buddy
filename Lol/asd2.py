import subprocess
import os
import tkinter as tk
from tkinter import filedialog

# Define the path to the text file
config_file_path = "base_directory.txt"

# Check if the text file exists and is not empty
if os.path.exists(config_file_path) and os.path.getsize(config_file_path) > 0:
    with open(config_file_path, 'r') as file:
        base_directory = file.read().strip()
else:
    # If the file is empty or doesn't exist, show a file selection dialog to choose the base directory
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    # Set the file types filter to show all files (no specific extension filter)
    file_types = [("All Files", "*.*")]

    # Show the file selection dialog
    base_directory = filedialog.askopenfilename(
        title="Select the base directory where RiotClientServices.exe is located",
        filetypes=file_types
    )

    if not base_directory:
        raise ValueError("Base directory not selected. Exiting...")

    # Save the selected base directory to the text file for future use
    with open(config_file_path, 'w') as file:
        file.write(base_directory)

# Construct the full file path to RiotClientServices.exe using os.path.join
riot_client_path = os.path.join(base_directory)

# Check if the file exists at the constructed path
if not os.path.exists(riot_client_path):
    raise FileNotFoundError(f"RiotClientServices.exe not found at {riot_client_path}")

# Define the arguments for the subprocess.Popen
args = [riot_client_path, "--headless", "--launch-product=league_of_legends", "--launch-patchline=live"]

# Start the subprocess
#p = subprocess.Popen(args)

# Wait for the subprocess to complete, if needed
# p.wait()
