import os

# Get the directory where the current script is located
current_dir = os.path.dirname(os.path.abspath(__file__))

# List all files in the current directory
for file in os.listdir(current_dir):
    if os.path.isfile(os.path.join(current_dir, file)):
        print(file)
