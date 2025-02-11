import os

# Get the directory where the script is located
current_dir = os.path.dirname(os.path.abspath(__file__))

# List and sort all files in the directory
files = sorted([f for f in os.listdir(current_dir) if os.path.isfile(os.path.join(current_dir, f))])

# Step 1: Rename all files to temporary names to avoid conflicts
temp_files = []
for index, file in enumerate(files):
    ext = os.path.splitext(file)[1]  # Get file extension
    temp_name = f"temp_{index}{ext}"  # Temporary name
    old_path = os.path.join(current_dir, file)
    temp_path = os.path.join(current_dir, temp_name)

    os.rename(old_path, temp_path)
    temp_files.append(temp_name)

# Step 2: Rename temp files to sequential names
for index, temp_file in enumerate(sorted(temp_files), start=1):
    ext = os.path.splitext(temp_file)[1]
    new_name = f"{index}{ext}"
    temp_path = os.path.join(current_dir, temp_file)
    new_path = os.path.join(current_dir, new_name)

    os.rename(temp_path, new_path)
    print(f'Renamed: {temp_file} -> {new_name}')
