import os
import shutil
from pathlib import Path
from datetime import datetime

def sort_files_by_extension(directory, log_file="file_sort_log.txt"):
    if not os.path.exists(directory):
        print(f"Directory '{directory}' does not exist.")
        return
    
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        # Skip directories (including extension folders already created)
        if os.path.isdir(file_path):
            continue

        # Get file extension (uppercase, no dot)
        extension = os.path.splitext(filename)[1][1:].upper()

        if extension:
            folder_path = os.path.join(directory, extension)
        else:
            folder_path = os.path.join(directory, "NO_EXTENSION")

        os.makedirs(folder_path, exist_ok=True)

        # Destination path
        dest_path = os.path.join(folder_path, filename)

        # Only move if not already in the right place
        if file_path != dest_path:
            shutil.move(file_path, dest_path)
            print(f"Moved: {filename} → {folder_path}")

            # Log the move with timestamp
            with open(os.path.join(directory, log_file), "a", encoding="utf-8") as log:
                timestamp = datetime.now().strftime("%d/%m/%Y %H:%M")
                log.write(f"[{timestamp}] Moved '{filename}' to '{extension if extension else 'NO_EXTENSION'}'\n")
        else:
            print(f"Skipped (already sorted): {filename}")

# Automatically detect the current user's Downloads folder
downloads_folder = Path.home() / "Downloads"
sort_files_by_extension(str(downloads_folder))
