import os
import shutil
from pathlib import Path

def sort_files_by_extension(directory):
    # Ensure the directory exists
    if not os.path.exists(directory):
        print(f"Directory '{directory}' does not exist.")
        return
    
    # Loop through all items in the directory
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        
        # Skip directories
        if os.path.isdir(file_path):
            continue
        
        # Get file extension (without the dot, uppercase for consistency)
        extension = os.path.splitext(filename)[1][1:].upper()
        
        if extension:  # Only process files with extensions
            # Create a folder for this extension if it doesn't exist
            folder_path = os.path.join(directory, extension)
            os.makedirs(folder_path, exist_ok=True)
            
            # Move the file into the extension folder
            shutil.move(file_path, os.path.join(folder_path, filename))
            print(f"Moved: {filename} → {folder_path}")
        else:
            # Handle files without extensions
            no_ext_folder = os.path.join(directory, "NO_EXTENSION")
            os.makedirs(no_ext_folder, exist_ok=True)
            shutil.move(file_path, os.path.join(no_ext_folder, filename))
            print(f"Moved: {filename} → {no_ext_folder}")

# Automatically detect the current user's Downloads folder
downloads_folder = Path.home() / "Downloads"
sort_files_by_extension(str(downloads_folder))
