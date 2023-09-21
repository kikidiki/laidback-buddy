
# List of applications to open
keyword = ["chrome", "powerpoint", "teams"]



import os
import fnmatch

def find_app(keyword):
    # List of directories to search
    dirs = ['C:\\Program Files', 'C:\\Program Files (x86)']

    for dir in dirs:
        for root, dirnames, filenames in os.walk(dir):
            for filename in fnmatch.filter(filenames, keyword):
                return os.path.join(root, filename)

    return None
find_app(keyword)