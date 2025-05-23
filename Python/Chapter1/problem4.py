
directory_path = 'C:\Users\Mahen\OneDrive\Desktop' 

 # Replace with your desired path

try:
    # Get the list of entries in the directory
    entries = os.listdir(directory_path)

    print(f"Contents of the directory '{directory_path}':")
    for entry in entries:
        print(entry)
except FileNotFoundError:
    print(f"The directory '{directory_path}' does not exist.")
except PermissionError:
    print(f"Permission denied to access '{directory_path}'.")

import os

# Get the list of entries in the current working directory
entries = os.listdir()

print("Contents of the current working directory:")
for entry in entries:
    print(entry)