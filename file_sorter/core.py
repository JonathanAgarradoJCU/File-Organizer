import os
import shutil
from datetime import datetime
from pathlib import Path


def _get_extension(filename):
    return os.path.splitext(filename)[1][1:].upper()


def _write_log(directory, log_file, filename, destination_folder):
    log_path = os.path.join(directory, log_file)
    timestamp = datetime.now().strftime("%d/%m/%Y %H:%M")
    with open(log_path, "a", encoding="utf-8") as log:
        log.write(f"[{timestamp}] Moved '{filename}' to '{destination_folder}'\n")


def sort_files_by_extension(directory, log_file="file_sort_log.txt"):
    if not os.path.exists(directory):
        print(f"Directory '{directory}' does not exist.")
        return False

    moved_any = False

    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        if os.path.isdir(file_path) or filename == log_file:
            continue

        extension = _get_extension(filename)
        destination_folder = extension or "NO_EXTENSION"
        folder_path = os.path.join(directory, destination_folder)

        os.makedirs(folder_path, exist_ok=True)

        dest_path = os.path.join(folder_path, filename)

        if file_path != dest_path:
            shutil.move(file_path, dest_path)
            moved_any = True
            print(f"Moved: {filename} → {folder_path}")
            _write_log(directory, log_file, filename, destination_folder)
        else:
            print(f"Skipped (already sorted): {filename}")

    if not moved_any:
        print("No files needed to be moved — everything is already sorted.")

    return moved_any
