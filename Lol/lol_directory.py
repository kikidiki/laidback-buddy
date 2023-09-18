from lol_vars import *

# Define the path to the text file where the base directory is stored
config_file_path = "base_directory.txt"

# Check if the text file exists and is not empty
if os.path.exists(config_file_path) and os.path.getsize(config_file_path) > 0:
    # If the file exists and is not empty, read the base directory from it
    with open(config_file_path, 'r') as file:
        base_directory = file.read().strip()
else:
    # If the file is empty or doesn't exist, show a file selection dialog to choose the base directory
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    # Set the file types filter to show all files (no specific extension filter)
    file_types = [("All Files", "*.*")]

    # Show the file selection dialog and store the selected base directory
    base_directory = filedialog.askdirectory(
        title="Select the base directory where RiotClientServices.exe is located"
    )

    # Check if a directory was selected, and raise an error if not
    if not base_directory:
        raise ValueError("Base directory not selected. Exiting...")

    # Save the selected base directory to the text file for future use
    with open(config_file_path, 'w') as file:
        file.write(base_directory)

# Construct the full file path to RiotClientServices.exe using os.path.join
riot_client_path = os.path.join(base_directory)

# Check if RiotClientServices.exe exists at the constructed path
if not os.path.exists(riot_client_path):
    raise FileNotFoundError(f"RiotClientServices.exe not found at {riot_client_path}")

# Define the arguments for starting the subprocess using subprocess.Popen
args = [riot_client_path, "--headless", "--launch-product=league_of_legends", "--launch-patchline=live"]

# Start the subprocess (uncomment the following line when ready to start)
# p = subprocess.Popen(args)

# Optionally, you can wait for the subprocess to complete using p.wait()
# p.wait()

# In my case I launch Rito Gamas from another file, so I don't need this part
